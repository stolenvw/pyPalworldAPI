"""Provide authentication helpers for the API."""

import os
from datetime import datetime, timedelta, timezone
from typing import Annotated, Optional

import bcrypt
import jwt
from dotenv import load_dotenv
from fastapi import Depends, Request, status
from fastapi.security import OAuth2PasswordBearer, SecurityScopes
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from pydantic import ValidationError
from sqlmodel.ext.asyncio.session import AsyncSession

from pyPalworldAPI.models.auth_models import TokenData, User
from pyPalworldAPI.query import auth as auth_query
from pyPalworldAPI.utils.customexception import APIError
from pyPalworldAPI.utils.database import auth_engine

load_dotenv(dotenv_path=".env")

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS"))

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="oauth2/login",
    auto_error=False,
)


async def get_auth_session():
    """Yield an authentication database session."""
    async with AsyncSession(auth_engine) as auth_session:
        yield auth_session


async def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Check if users supplied password matches with there stored hashed password.

    Parameters
    ----------
    plain_password : str
        Users plain password.
    hashed_password : str
        Users hashed password.

    Returns
    -------
    bool
        True if passwords match else false

    """
    password_byte_enc = plain_password.encode("utf-8")
    return bcrypt.checkpw(password=password_byte_enc, hashed_password=str.encode(hashed_password))


async def get_password_hash(password: str) -> bytes:
    """Convert users supplied password to a hashed password.

    Parameters
    ----------
    password : str
        Users plain password.

    Returns
    -------
    hashed_password : bytes
        Hashed version of users password.

    """
    pwd_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)
    return hashed_password


async def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """Create a users access token.

    Parameters
    ----------
    data : dict
        Data to make access token with {"sub": "username", "scopes": "list of scopes"}
    expires_delta : timedelta, optional
        How long access token should be valid for.

    Returns
    -------
    access token : str
        Users access token.

    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def create_refresh_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """Create a users refresh token.

    Parameters
    ----------
    data : dict
        Data to make refresh token with {"sub": "username", "scopes": "list of scopes"}
    expires_delta : timedelta, optional
        How long refresh token should be valid for.

    Returns
    -------
    refresh token : str
        Users refresh token.

    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(days=7)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def verify_refresh_token(db: AsyncSession, token: str) -> TokenData:
    """Verify a users refresh token.

    Parameters
    ----------
    token : str
        Users refresh token.

    Returns
    -------
    tokenData : object
        Decrypted refresh token data.

    Raises
    ------
    APIError
        HTTP responses with errors.

    """
    credential_exception = APIError(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={
            "status": status.HTTP_401_UNAUTHORIZED,
            "message": "Invalid refresh token.",
        },
        headers={"WWW-Authenticate": "refresh_token"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        username: str = payload.get("sub")
        scopes: str = payload.get("scopes")
        exp: str = payload.get("exp")
        if username is None:
            raise credential_exception
        token_data = TokenData(username=username, scopes=scopes, exp=exp)
    except InvalidTokenError as err:
        raise credential_exception from err
    else:
        token_valid = await auth_query.check_refresh_token(db, username)
        if not token_valid or token != token_valid.refresh_token:
            raise credential_exception
    return token_data


async def get_current_user(
    security_scopes: SecurityScopes,
    token: Annotated[str, Depends(oauth2_scheme)],
    db: AsyncSession = Depends(get_auth_session),
) -> User:
    """Get current logged in user from access token.

    Parameters
    ----------
    security_scopes : SecurityScopes
        Object of needed router scopes.
    token : str
        Users access token.

    Returns
    -------
    User : object
        User object of logged in user.

    Raises
    ------
    APIError
        HTTP responses with errors.

    """
    if security_scopes.scopes:
        authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
    else:
        authenticate_value = "Bearer"
    credentials_exception = APIError(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={
            "status": status.HTTP_401_UNAUTHORIZED,
            "message": "Not authenticated.",
        },
        headers={"WWW-Authenticate": authenticate_value},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_scopes = payload.get("scopes", [])
        exp: str = payload.get("exp")
        token_data = TokenData(scopes=token_scopes, username=username, exp=exp)
    except (InvalidTokenError, ValidationError) as err:
        raise credentials_exception from err
    user = await auth_query.get_user(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    token_valid = await auth_query.token_valid(db=db, token=token)
    if not token_valid:
        raise credentials_exception
    for scope in security_scopes.scopes:
        if scope not in token_data.scopes:
            raise APIError(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={
                    "status": status.HTTP_401_UNAUTHORIZED,
                    "message": "Not enough permissions.",
                },
                headers={"WWW-Authenticate": authenticate_value},
            )
    return user


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
) -> User:
    """Get current logged in user from access token.

    Parameters
    ----------
    current_user : User
        Logged in user object.

    Returns
    -------
    User : object
        User object of logged in user.

    Raises
    ------
    APIError
        HTTP responses with errors.

    """
    if current_user.disabled:
        raise APIError(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={
                "status": status.HTTP_401_UNAUTHORIZED,
                "message": "Inactive user.",
            },
            headers=None,
        )
    return current_user


async def remove_old_tokens(db: AsyncSession) -> None:
    """Checks for and removes access tokens that have expired from the Tokens table.

    Parameters
    ----------
    db : AsyncSession
        SQL database connection session.

    Returns
    -------
    None

    """
    token_list = await auth_query.list_tokens(db=db)
    delete_tokens_list = []
    for token in token_list:
        try:
            jwt.decode(token.token, SECRET_KEY, algorithms=ALGORITHM)
        except ExpiredSignatureError:
            delete_tokens_list.append(token)
    if delete_tokens_list:
        await auth_query.delete_old_tokens(db=db, tokens=delete_tokens_list)
    await db.close()


async def verify_token(request: Request) -> TokenData:
    """Verify access token is still valid.

    Parameters
    ----------
    request : Request
        Request object from ``/oauth2/validate`` route.

    Returns
    -------
    TokenData : object
        Access token object.

    Raises
    ------
    APIError
        HTTP responses with errors.

    """
    auth_type = ""
    token = ""
    if "authorization" in request.headers:
        auth_type, _, token = request.headers["authorization"].partition(" ")
    else:
        raise APIError(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Missing authorization header.",
            },
            headers=None,
        )
    if auth_type.lower() == "oauth":
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            token_data = TokenData(
                username=payload.get("sub"),
                scopes=payload.get("scopes"),
                exp=payload.get("exp"),
            )
        except (InvalidTokenError, ValidationError) as err:
            raise APIError(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={
                    "status": status.HTTP_401_UNAUTHORIZED,
                    "message": "Invalid access token.",
                },
                headers=None,
            ) from err
        else:
            return token_data
    else:
        raise APIError(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Invalid authorization type.",
            },
            headers=None,
        )
