r"""Provide user helpers."""

from typing import Annotated

from fastapi import APIRouter, Depends, Form, Security, status
from sqlmodel.ext.asyncio.session import AsyncSession

from pyPalworldAPI.models import auth_models
from pyPalworldAPI.query import auth as auth_query
from pyPalworldAPI.utils.auth import (
    get_auth_session,
    get_current_active_user,
    get_password_hash,
    verify_password,
)
from pyPalworldAPI.utils.customexception import APIError
from pyPalworldAPI.utils.customresponses import PalworldAPIErrorResponses
from pyPalworldAPI.utils.examples import PalworldAPIExamples

router = APIRouter(
    prefix="/user",
    tags=["User"],
    responses=PalworldAPIErrorResponses.response_400_401,
)


@router.put(
    "/changepassword/",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Change your password.",
    response_model=auth_models.MessageStatus,
    openapi_extra={"x-codeSamples": PalworldAPIExamples.user_change_password},
)
async def change_own_password(
    current_user: Annotated[
        auth_models.User,
        Security(get_current_active_user, scopes=["APIUser:Read", "APIUser:ChangePassword"]),
    ],
    current_password: str = Form(),
    new_password: str = Form(max_length=256, min_length=6),
    db: AsyncSession = Depends(get_auth_session),
):
    r"""Change your password.

    .. important:: Changing your password will make all your access/refresh invalid.
    \f

    Parameters
    ----------
    current_password : str
        Your current password
    new_password : str
        Your new password

    Returns
    -------
    json
        ::

        {
            "message": "Password Changed Successfully.",
            "status": 202
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

        curl -X 'PUT' \\
            'http://127.0.0.0/user/changepassword/' \\
            -H 'Accept: application/json' \\
            -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3' \\
            -H 'Content-Type: application/x-www-form-urlencoded' \\
            -d 'current_password=SomePass&new_password=SomeNewPass'

    Python::

        import asyncio
        import json

        import aiohttp
        from aiohttp.client_exceptions import ClientConnectorError


        async def put_user_change_password(
            current_password: str, new_password: str, access_token: str
        ):
            url = f"http://127.0.0.0/user/changepassword/"
            headers = {
                "Accept": "application/json",
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/x-www-form-urlencoded",
            }
            body = {"current_password": current_password, "new_password": new_password}
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.put(url, headers=headers, data=body) as result:
                        data = await result.json()
            except ClientConnectorError as e:
                print(f"ClientConnectorError: {e}")
            else:
                print(json.dumps(data, indent=2))


        if __name__ == "__main__":
            asyncio.run(
                put_user_change_password(
                    current_password="SomePass",
                    new_password="SomeNewPass",
                    access_token="kajfe0983qjaf309ajj3w8j3aij3a3",
                )
            )


    """
    if not await verify_password(current_password, current_user.password):
        raise APIError(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Invalid Password.",
            },
            headers=None,
        )
    hashed_password = await get_password_hash(new_password)
    user = await auth_query.get_user(db, current_user.username)
    await auth_query.change_password(db=db, user=user, new_password=hashed_password)
    return {
        "message": "Password Changed Successfully.",
        "status": status.HTTP_202_ACCEPTED,
    }


@router.get(
    "/me/",
    response_model=auth_models.UserResponse,
    summary="List User Info",
    openapi_extra={"x-codeSamples": PalworldAPIExamples.me},
)
async def get_user(
    current_user: Annotated[
        auth_models.User, Security(get_current_active_user, scopes=["APIUser:Read"])
    ],
):
    r"""List all users.

    \f.

    Returns
    -------
    json
        ::

        {
          "items": [
            {
              "username": "Bob123",
              "disabled": false,
              "created_at": "2024-08-02T20:48:43",
              "scopes": [
                "APIUser:Read",
                "APIUser:ChangePassword"
              ]
            }
          ],
          "total": 1,
          "page": 1,
          "size": 50,
          "pages": 1
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
            'http://127.0.0.0/user/me/' \\
            -H 'Accept: application/json' \\
            -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'

    Python::

        import asyncio
        import json

        import aiohttp
        from aiohttp.client_exceptions import ClientConnectorError


        async def get_user_me(access_token: str):
            url = f"http://127.0.0.0/user/me/"
            headers = {
                "Accept": "application/json",
                "Authorization": f"Bearer {access_token}",
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
    return current_user
