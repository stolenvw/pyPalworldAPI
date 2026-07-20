r"""Provide oauth2 helpers."""

import random
from datetime import datetime, timedelta, timezone
from typing import Annotated

from fastapi import APIRouter, BackgroundTasks, Depends, Form, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel.ext.asyncio.session import AsyncSession

from pyPalworldAPI.models import auth_models
from pyPalworldAPI.query import auth as auth_query
from pyPalworldAPI.utils import auth as auth_utils
from pyPalworldAPI.utils.auth import verify_token
from pyPalworldAPI.utils.customexception import APIError
from pyPalworldAPI.utils.customresponses import PalworldAPIErrorResponses
from pyPalworldAPI.utils.examples import PalworldAPIExamples

router = APIRouter(
    prefix="/oauth2",
    tags=["Auth"],
    responses=PalworldAPIErrorResponses.response_400_401,
)


@router.post(
    "/login/",
    status_code=status.HTTP_200_OK,
    response_model=auth_models.LoginResponse,
    openapi_extra={"x-codeSamples": PalworldAPIExamples.login},
)
async def login(
    user_credentials: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(auth_utils.get_auth_session),
):
    r"""To login, send an HTTP POST request to ``https://127.0.0.1/oauth2/login``.

    When you get a access token, the `expires_in` field indicates how long, in seconds, the token is valid for.
    When a token expires, it becomes invalid. If you call the API with an invalid token, the request returns 401 Unauthorized.
    \f

    Parameters
    ----------
    username : str
        User to login as.
    password : str
        Users password.

    Returns
    -------
    json
        ::

        {
            "access_token": "kajfe0983qjaf309ajj3w8j3aij3a3",
            "token_type": "Bearer",
            "expires_in": 8200,
            "scopes": [
                "APIUser:Read",
                "APIUser:ChangePassword"
            ],
            "refresh_token": {
                "token": "kafaj083209jq904j8qjiaf39",
                "expires_in": 72000
            },
            "message": "User Logged in Successfully.",
            "status": 200
        }

    Raises
    ------
    APIError
        HTTP responses with errors.
    RequestValidationError
        When a request contains invalid data.

    Examples
    --------
    Curl::

        curl -X 'POST' \\
            'http://127.0.0.0/oauth2/login/' \\
            -H 'accept: application/json' \\
            -H 'Content-Type: application/x-www-form-urlencoded' \\
            -d 'username=Bob123&password=SomePass'

    Python::

        import asyncio
        import json

        import aiohttp
        from aiohttp.client_exceptions import ClientConnectorError


        async def post_login(username: str, password: str):
            url = f"http://127.0.0.0/oauth2/login/"
            headers = {
                "Accept": "application/json",
                "Content-Type": "application/x-www-form-urlencoded",
            }
            body = {"username": username, "password": password}
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=headers, data=body) as result:
                        data = await result.json()
            except ClientConnectorError as e:
                print(f"ClientConnectorError: {e}")
            else:
                print(json.dumps(data, indent=2))


        if __name__ == "__main__":
            asyncio.run(post_login(username="Bob123", password="SomePass"))


    """
    user = await auth_query.get_user(db, user_credentials.username)
    if not user:
        raise APIError(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={
                "status": status.HTTP_401_UNAUTHORIZED,
                "message": "Invalid Username or Password.",
            },
            headers={"WWW-Authenticate": "Bearer"},
        )
    if user.disabled:
        raise APIError(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={
                "status": status.HTTP_401_UNAUTHORIZED,
                "message": "Account Disabled.",
            },
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not await auth_utils.verify_password(user_credentials.password, user.password):
        raise APIError(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={
                "status": status.HTTP_401_UNAUTHORIZED,
                "message": "Invalid Username or Password.",
            },
            headers={"WWW-Authenticate": "Bearer"},
        )
    refresh_token_check = await auth_query.refresh_token_delete(db, user_id=user.ID)
    access_token_expires = timedelta(minutes=auth_utils.ACCESS_TOKEN_EXPIRE_MINUTES)
    refresh_token_expires = timedelta(days=auth_utils.REFRESH_TOKEN_EXPIRE_DAYS)
    access_token = await auth_utils.create_access_token(
        data={"sub": user.username, "scopes": user.scopes},
        expires_delta=access_token_expires,
    )
    refresh_token = await auth_utils.create_refresh_token(
        data={"sub": user.username, "scopes": user.scopes},
        expires_delta=refresh_token_expires,
    )
    refresh_token_dict = {
        "user_id": user.ID,
        "refresh_token": refresh_token,
    }
    user_scopes = user.scopes
    refresh_token_db_data = auth_models.RefreshToken(**refresh_token_dict)
    await auth_query.store_token(db=db, user_id=user.ID, token=access_token)
    if refresh_token_check:
        refresh_token_check.refresh_token = refresh_token
        refresh_token_check.created_at = datetime.now(timezone.utc)
        db.add(refresh_token_check)
        await db.commit()
    else:
        db.add(refresh_token_db_data)
        await db.commit()
    r_token = auth_models.RefreshTokenInfo(
        token=refresh_token, expires_in=int(refresh_token_expires.total_seconds())
    )
    return {
        "access_token": access_token,
        "token_type": "Bearer",
        "expires_in": int(access_token_expires.total_seconds()),
        "scopes": user_scopes,
        "refresh_token": r_token,
        "message": "User Logged in Successfully.",
        "status": status.HTTP_200_OK,
    }


@router.post(
    "/refresh/",
    status_code=status.HTTP_200_OK,
    response_model=auth_models.RefreshResponse,
    openapi_extra={"x-codeSamples": PalworldAPIExamples.refresh},
)
async def get_new_access_token(
    token: Annotated[str, Form()],
    grant_type: Annotated[str, Form()],
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(auth_utils.get_auth_session),
):
    r"""To refresh a access token, send an HTTP POST request to ``https://127.0.0.1/oauth2/refresh``.

    \f.

    Parameters
    ----------
    token : str
        The refresh token issued to the client.
    grant_type : str
        Must be set to ``refresh_token``.

    Returns
    -------
    json
        ::

        {
            "access_token": {
                "token_type": "Bearer",
                "access_token": "kajfe0983qjaf309ajj3w8j3aij3a3",
                "expires_in": 8200
            },
            "refresh_token": {
                "token": "kafaj083209jq904j8qjiaf39",
                "expires_in": 72000
            },
            "status": 200
        }

    Raises
    ------
    APIError
        HTTP responses with errors.
    RequestValidationError
        When a request contains invalid data.

    Examples
    --------
    Curl::

        curl -X 'POST' \\
            'https://127.0.0.1/oauth2/refresh' \\
            -H 'accept: application/json' \\
            -H 'Content-Type: application/x-www-form-urlencoded' \\
            -d 'token=kafaj083209jq904j8qjiaf39&grant_type=refresh_token'

    Python::

        import asyncio
        import json

        import aiohttp
        from aiohttp.client_exceptions import ClientConnectorError


        async def post_refresh(refresh_token: str):
            url = f"http://127.0.0.0/oauth2/refresh/"
            headers = {
                "Accept": "application/json",
                "Content-Type": "application/x-www-form-urlencoded",
            }
            body = {"token": refresh_token, "grant_type": "refresh_token"}
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=headers, data=body) as result:
                        data = await result.json()
            except ClientConnectorError as e:
                print(f"ClientConnectorError: {e}")
            else:
                print(json.dumps(data, indent=2))


        if __name__ == "__main__":
            asyncio.run(post_refresh(refresh_token="kafaj083209jq904j8qjiaf39"))


    """
    background_tasks.add_task(auth_utils.remove_old_tokens, db)
    if grant_type != "refresh_token":
        raise APIError(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Invalid Grant Type.",
            },
            headers={"WWW-Authenticate": "Bearer"},
        )
    refresh_data = await auth_utils.verify_refresh_token(db, token)
    access_token_expires = timedelta(minutes=auth_utils.ACCESS_TOKEN_EXPIRE_MINUTES)
    refresh_token_expires = timedelta(days=auth_utils.REFRESH_TOKEN_EXPIRE_DAYS)
    new_access_token = await auth_utils.create_access_token(
        {"sub": refresh_data.username, "scopes": refresh_data.scopes},
        expires_delta=access_token_expires,
    )
    user = await auth_query.get_user(db, refresh_data.username)
    if (
        random.randrange(int(refresh_token_expires.total_seconds()))
        > (
            datetime.fromtimestamp(refresh_data.exp, tz=timezone.utc) - datetime.now(timezone.utc)
        ).total_seconds()
    ):
        refresh_token_check = await auth_query.refresh_token_delete(db, user_id=user.ID)
        refresh_token = await auth_utils.create_refresh_token(
            data={"sub": user.username, "scopes": user.scopes},
            expires_delta=refresh_token_expires,
        )
        refresh_token_check.refresh_token = refresh_token
        refresh_token_check.created_at = datetime.now(timezone.utc)
        db.add(refresh_token_check)
        await db.commit()
        r_token = auth_models.RefreshTokenInfo(
            token=refresh_token, expires_in=int(refresh_token_expires.total_seconds())
        )
    else:
        refresh_token_expire_in = (
            datetime.fromtimestamp(refresh_data.exp, tz=timezone.utc) - datetime.now(timezone.utc)
        ).total_seconds()
        r_token = auth_models.RefreshTokenInfo(token=token, expires_in=int(refresh_token_expire_in))
    a_token = auth_models.AccessTokenInfo(
        token_type="Bearer",
        access_token=new_access_token,
        expires_in=int(access_token_expires.total_seconds()),
    )
    await auth_query.store_token(db=db, user_id=user.ID, token=new_access_token)
    return {
        "access_token": a_token,
        "refresh_token": r_token,
        "status": status.HTTP_200_OK,
    }


@router.get(
    "/validate",
    status_code=status.HTTP_200_OK,
    response_model=auth_models.ValidateResponse,
    summary="Validate token",
    openapi_extra={"x-codeSamples": PalworldAPIExamples.validate},
)
async def validate_token(
    payload: Annotated[str, Depends(verify_token)],
):
    r"""To validate a access token, send an HTTP GET request to ``https://127.0.0.1/oauth2/validate``.

    \f.

    Returns
    -------
    json
        ::

        {
            "username": "Bob123",
            "scopes": [
                "APIUser:Read",
                "APIUser:ChangePassword"
            ],
            "expires_in": 8200
        }

    Raises
    ------
    APIError
        HTTP responses with errors.
    RequestValidationError
        When a request contains invalid data.

    Examples
    --------
    Curl::

        curl -X 'GET' \\
            'http://127.0.0.0/oauth2/validate' \\
            -H 'Accept: application/json' \\
            -H 'Authorization: OAuth kajfe0983qjaf309ajj3w8j3aij3a3'

    Python::

        import asyncio
        import json

        import aiohttp
        from aiohttp.client_exceptions import ClientConnectorError


        async def get_user_me(access_token: str):
            url = "http://127.0.0.0/oauth2/validate"
            headers = {
                "Accept": "application/json",
                "Authorization": f"OAuth {access_token}",
            }
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(url, headers=headers) as result:
                        data = await result.json()
            except ClientConnectorError as e:
                print(f"ClientConnectorError: {e}")
            else:
                print(json.dumps(data, indent=2))


        if __name__ == "__main__":
            asyncio.run(get_user_me(access_token="kajfe0983qjaf309ajj3w8j3aij3a3"))


    """
    token_expire_in = (
        datetime.fromtimestamp(payload.exp, tz=timezone.utc) - datetime.now(timezone.utc)
    ).total_seconds()
    return {
        "username": payload.username,
        "scopes": payload.scopes,
        "expires_in": int(token_expire_in),
    }
