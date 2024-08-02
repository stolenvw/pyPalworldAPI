import os
from datetime import datetime, timedelta, timezone
from typing import Annotated, Optional

import bcrypt
import jwt
from dotenv import load_dotenv
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, SecurityScopes
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from models.auth_models import TokenData, User
from pydantic import ValidationError
from query import auth as AuthQuery
from sqlmodel.ext.asyncio.session import AsyncSession
from utils.database import auth_engine

load_dotenv(dotenv_path=".env")

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS"))

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="oauth2/login",
)


async def get_auth_session():
    async with AsyncSession(auth_engine) as auth_session:
        yield auth_session


async def verify_password(plain_password, hashed_password):
    password_byte_enc = plain_password.encode("utf-8")
    return bcrypt.checkpw(
        password=password_byte_enc, hashed_password=str.encode(hashed_password)
    )


async def get_password_hash(password):
    pwd_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)
    return hashed_password


async def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def create_refresh_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(days=7)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def verify_refresh_token(db, token: str):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid refresh token",
        headers={"WWW-Authenticate": "refresh_token"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        username: str = payload.get("sub")
        scopes: str = payload.get("scopes")
        exp: str = payload.get("exp")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username, scopes=scopes, exp=exp)
    except InvalidTokenError:
        raise credential_exception
    else:
        token_valid = await AuthQuery.check_refresh_token(db, username)
        if token != token_valid.refresh_token:
            token_invalid = HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid refresh token",
                headers={"WWW-Authenticate": "refresh_token"},
            )
            raise token_invalid
    return token_data


async def get_current_user(
    security_scopes: SecurityScopes,
    token: Annotated[str, Depends(oauth2_scheme)],
    db: AsyncSession = Depends(get_auth_session),
):
    if security_scopes.scopes:
        authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
    else:
        authenticate_value = "Bearer"
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
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
    except (InvalidTokenError, ValidationError):
        raise credentials_exception
    user = await AuthQuery.get_user(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    token_valid = await AuthQuery.token_valid(db=db, token=token)
    if not token_valid:
        raise credentials_exception
    for scope in security_scopes.scopes:
        if scope not in token_data.scopes:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not enough permissions",
                headers={"WWW-Authenticate": authenticate_value},
            )
    return user


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


async def remove_old_tokens(db: AsyncSession):
    token_list = await AuthQuery.list_tokens(db=db)
    delete_tokens_list = []
    for token in token_list:
        try:
            jwt.decode(token.token, SECRET_KEY, algorithms=ALGORITHM)
        except ExpiredSignatureError:
            delete_tokens_list.append(token)
    if delete_tokens_list:
        await AuthQuery.delete_old_tokens(db=db, tokens=delete_tokens_list)
    await db.close()
