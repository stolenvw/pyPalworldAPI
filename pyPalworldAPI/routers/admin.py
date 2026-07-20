r"""Provide admin helpers."""

from typing import Annotated

from fastapi import APIRouter, Depends, Form, Security, status
from sqlmodel.ext.asyncio.session import AsyncSession

from pyPalworldAPI.models import auth_models
from pyPalworldAPI.query import auth as auth_query
from pyPalworldAPI.utils.auth import get_auth_session, get_current_active_user, get_password_hash
from pyPalworldAPI.utils.customexception import APIError
from pyPalworldAPI.utils.custompage import Page
from pyPalworldAPI.utils.customresponses import PalworldAPIErrorResponses
from pyPalworldAPI.utils.examples import PalworldAPIExamples

router = APIRouter(
    prefix="/admin",
    tags=["Admin"],
    dependencies=[Security(get_current_active_user, scopes=["APIAdmin:Write"])],
)


@router.post(
    "/adduser/",
    status_code=status.HTTP_201_CREATED,
    response_model=auth_models.RegistrationUserResponse,
    summary="Add User",
    responses=PalworldAPIErrorResponses.response_401_409,
    openapi_extra={"x-codeSamples": PalworldAPIExamples.add_user},
)
async def adduser(
    new_user: auth_models.UserInput,
    db: AsyncSession = Depends(get_auth_session),
):
    r"""Create a user.

    \f.

    Parameters
    ----------
    username : str
        User to add
    password : str
        Users password
    scopes: list of str
        List of scopes to give the user
    disabled : bool
        Mark users account as disabled


    .. note::
        Valid Scopes
            - **APIAdmin:Write**: Can add users.
            - **APIUser:Read**: Read API items.
            - **APIUser:ChangePassword**: User can change there password.

    Returns
    -------
    json
        ::

        {
            "message": "User added successful",
            "data": {
                "username": "Bob123",
                "password": "SomePass",
                "scopes": [
                    "APIUser:Read",
                    "APIUser:ChangePassword"
                ],
                "disabled": "False"
            }
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

        curl -X 'Post' \\
            'http://127.0.0.0/admin/adduser/' \\
            -H 'Accept: application/json' \\
            -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3' \\
            -H 'Content-Type: application/json' \\
            -d '{
                  "username": "Bob123",
                  "password": "SomePass",
                  "scopes": [
                    "APIUser:Read",
                    "APIUser:ChangePassword"
                  ],
                  "disabled": false
                }'

    Python::

        import asyncio
        import json

        import aiohttp
        from aiohttp.client_exceptions import ClientConnectorError


        async def post_add_user(
            access_token: str, username: str, password: str, scopes: list, disabled: bool
        ):
            url = f"http://127.0.0.0/admin/adduser/"
            headers = {
                "Accept": "application/json",
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json",
            }
            json_body = {
                "username": username,
                "password": password,
                "scopes": scopes,
                "disabled": disabled,
            }
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=headers, json=json_body) as result:
                        data = await result.json()
            except ClientConnectorError as e:
                print(f"ClientConnectorError: {e}")
            else:
                print(json.dumps(data, indent=2))


        if __name__ == "__main__":
            asyncio.run(
                post_add_user(
                    access_token="kajfe0983qjaf309ajj3w8j3aij3a3",
                    username="Bob123",
                    password="SomePass",
                    scopes=["APIUser:Read", "APIUser:ChangePassword"],
                    disabled=False,
                )
            )


    """
    user = await auth_query.get_user(db, new_user.username)
    if user:
        raise APIError(
            status_code=status.HTTP_409_CONFLICT,
            content={
                "status": status.HTTP_409_CONFLICT,
                "message": "Username is taken.",
            },
            headers=None,
        )
    hashed_password = await get_password_hash(new_user.password)
    new_user.password = hashed_password
    add_user = auth_models.User(
        username=new_user.username,
        password=new_user.password,
        scopes=new_user.scopes,
        disabled=new_user.disabled,
    )
    db.add(add_user)
    await db.commit()
    await db.refresh(add_user)
    return {"message": "User added successful", "data": add_user}


@router.put(
    "/chpass/",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Change Users Password",
    responses=PalworldAPIErrorResponses.response_401_404,
    response_model=auth_models.MessageStatus,
    openapi_extra={"x-codeSamples": PalworldAPIExamples.admin_change_password},
)
async def changepassword(
    username: str = Form(),
    new_password: str = Form(max_length=256, min_length=6),
    db: AsyncSession = Depends(get_auth_session),
):
    r"""Change users password.

    .. important:: Changing users password will make any access/refresh token they currently have invalid.
    \f

    Parameters
    ----------
    username : str
        User to change password for
    new_password : str
        Users new password

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
            'http://127.0.0.0/admin/chpass/' \\
            -H 'Accept: application/json' \\
            -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3' \\
            -H 'Content-Type: application/x-www-form-urlencoded' \\
            -d 'username=Bob123&new_password=SomeNewPass'

    Python::

        import asyncio
        import json

        import aiohttp
        from aiohttp.client_exceptions import ClientConnectorError


        async def put_admin_change_password(
            username: str, new_password: str, access_token: str
        ):
            url = f"http://127.0.0.0/admin/chpass/"
            headers = {
                "Accept": "application/json",
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/x-www-form-urlencoded",
            }
            body = {"username": username, "new_password": new_password}
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
                put_admin_change_password(
                    username="Bob123",
                    new_password="SomeNewPass",
                    access_token="kajfe0983qjaf309ajj3w8j3aij3a3",
                )
            )


    """
    pass_reset = auth_models.PassReset(username=username, new_password=new_password)
    user = await auth_query.get_user(db, pass_reset.username)
    if not user:
        raise APIError(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "status": status.HTTP_404_NOT_FOUND,
                "message": "Username not found.",
            },
            headers=None,
        )
    hashed_password = await get_password_hash(pass_reset.new_password)
    await auth_query.change_password(db=db, user=user, new_password=hashed_password)
    return {
        "message": "Password Changed Successfully.",
        "status": status.HTTP_202_ACCEPTED,
    }


@router.delete(
    "/deleteuser/",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Delete User",
    responses=PalworldAPIErrorResponses.response_401_403_404,
    response_model=auth_models.MessageStatus,
    openapi_extra={"x-codeSamples": PalworldAPIExamples.delete_user},
)
async def deleteuser(
    current_user: Annotated[
        auth_models.User, Security(get_current_active_user, scopes=["APIAdmin:Write"])
    ],
    username: str,
    db: AsyncSession = Depends(get_auth_session),
):
    r"""Delete a user.

    \f.

    Parameters
    ----------
    username : str
        User to delete

    Returns
    -------
    json
        ::

        {
            "message": "User Deleted Successfully.",
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

        curl -X 'PUT' \\
            'http://127.0.0.0/admin/deleteuser/?username=Bob123' \\
            -H 'Accept: application/json' \\
            -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'

    Python::

        import asyncio
        import json

        import aiohttp
        from aiohttp.client_exceptions import ClientConnectorError


        async def delete_admin_delete_user(access_token: str, username: str):
            url = "http://127.0.0.0/admin/deleteuser/"
            headers = {
                "Accept": "application/json",
                "Authorization": f"Bearer {access_token}",
            }
            params = {"username": username}
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.delete(url, headers=headers, params=params) as result:
                        data = await result.json()
            except ClientConnectorError as e:
                print(f"ClientConnectorError: {e}")
            else:
                print(json.dumps(data, indent=2))


        if __name__ == "__main__":
            asyncio.run(
                delete_admin_delete_user(
                    access_token="kajfe0983qjaf309ajj3w8j3aij3a3", username="Bob123"
                )
            )


    """
    user_credentials = auth_models.UserName(username=username)
    if user_credentials.username.lower() == current_user.username.lower():
        raise APIError(
            status_code=status.HTTP_403_FORBIDDEN,
            content={
                "status": status.HTTP_403_FORBIDDEN,
                "message": "You can not delete your own admin account.",
            },
            headers=None,
        )
    user = await auth_query.get_user(db, user_credentials.username)
    if not user:
        raise APIError(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "status": status.HTTP_404_NOT_FOUND,
                "message": "Username not found.",
            },
            headers=None,
        )
    await auth_query.delete_user(db=db, user=user)
    return {
        "message": "User Deleted Successfully.",
        "status": status.HTTP_202_ACCEPTED,
    }


@router.get(
    "/users/",
    response_model=Page[auth_models.UserResponse],
    summary="List Users",
    responses=PalworldAPIErrorResponses.response_401_404,
    openapi_extra={"x-codeSamples": PalworldAPIExamples.list_users},
)
async def list_user(
    db: AsyncSession = Depends(get_auth_session),
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
            'http://127.0.0.0/admin/users/?page=1&size=50' \\
            -H 'Accept: application/json' \\
            -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'

    Python::

        import asyncio
        import json

        import aiohttp
        from aiohttp.client_exceptions import ClientConnectorError


        async def get_admin_users(access_token: str):
            url = "http://127.0.0.0/admin/users/"
            headers = {
                "Accept": "application/json",
                "Authorization": f"Bearer {access_token}",
            }
            params = {"page": 1, "size": 50}
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(url, headers=headers, params=params) as result:
                        data = await result.json()
            except ClientConnectorError as e:
                print(f"ClientConnectorError: {e}")
            else:
                print(json.dumps(data, indent=2))


        if __name__ == "__main__":
            asyncio.run(get_admin_users(access_token="kajfe0983qjaf309ajj3w8j3aij3a3"))


    """
    item = await auth_query.list_users(db)
    if len(item.items) != 0:
        return item
    else:
        raise APIError(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "status": status.HTTP_404_NOT_FOUND,
                "message": "Nothing Found.",
            },
            headers=None,
        )


@router.put(
    "/userdisable/",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Disable/Enable User",
    responses=PalworldAPIErrorResponses.response_401_403_404,
    response_model=auth_models.MessageStatus,
    openapi_extra={"x-codeSamples": PalworldAPIExamples.user_disable},
)
async def userdisable(
    current_user: Annotated[
        auth_models.User, Security(get_current_active_user, scopes=["APIAdmin:Write"])
    ],
    username: Annotated[str, Form()],
    disabled: Annotated[bool, Form()],
    db: AsyncSession = Depends(get_auth_session),
):
    r"""Disable / Enable a users account.

    \f.

    Parameters
    ----------
    username : str
        User to disable
    disabled : bool
        Mark users account as disabled

    Returns
    -------
    json
        ::

        {
            "message": "Username Disabled: True",
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

        curl -X 'PUT' \\
            'http://127.0.0.0/admin/userdisable/' \\
            -H 'Accept: application/json' \\
            -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3' \\
            -H 'Content-Type: application/x-www-form-urlencoded' \\
            -d 'username=Bob123&disabled=True'

    Python::

        import asyncio
        import json

        import aiohttp
        from aiohttp.client_exceptions import ClientConnectorError


        async def put_admin_user_disable(access_token: str, username: str, disabled: bool):
            url = f"http://127.0.0.0/admin/userdisable/"
            headers = {
                "Accept": "application/json",
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/x-www-form-urlencoded",
            }
            body = {"username": username, "disabled": disabled}
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
                put_admin_user_disable(
                    access_token="kajfe0983qjaf309ajj3w8j3aij3a3",
                    username="Bob123",
                    disabled=True,
                )
            )


    """
    if username.lower() == current_user.username.lower():
        raise APIError(
            status_code=status.HTTP_403_FORBIDDEN,
            content={
                "status": status.HTTP_403_FORBIDDEN,
                "message": "You can not change the disabled status of your own account.",
            },
            headers=None,
        )
    user = await auth_query.get_user(db, username)
    if not user:
        raise APIError(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "status": status.HTTP_404_NOT_FOUND,
                "message": "Username not found.",
            },
            headers=None,
        )
    await auth_query.change_user_status(db, user, disabled)
    return {
        "message": f"Username Disabled: {disabled}.",
        "status": status.HTTP_202_ACCEPTED,
    }


@router.put(
    "/chscope/",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Change Users Scopes",
    responses=PalworldAPIErrorResponses.response_401_403_404,
    response_model=auth_models.MessageStatus,
    openapi_extra={"x-codeSamples": PalworldAPIExamples.change_scopes},
)
async def scope_change(
    current_user: Annotated[
        auth_models.User, Security(get_current_active_user, scopes=["APIAdmin:Write"])
    ],
    update_user: auth_models.UserScopeChange,
    db: AsyncSession = Depends(get_auth_session),
):
    r"""Change Users Scopes.

    \f.

    Parameters
    ----------
    username : str
        User to change scope for
    scopes: list of str
        List of scopes to give the user

    Returns
    -------
    json
        ::

        {
            "message": "Scopes Changed Successfully",
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
            'http://127.0.0.0/admin/chscope/' \\
            -H 'Accept: application/json' \\
            -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3' \\
            -H 'Content-Type: application/json' \\
            -d '{
                  "username": "Bob123",
                  "scopes": [
                    "APIUser:Read",
                    "APIUser:ChangePassword"
                  ],
                }'

    Python::

        import asyncio
        import json

        import aiohttp
        from aiohttp.client_exceptions import ClientConnectorError


        async def put_admin_change_scope(access_token: str, username: str, scopes: list):
            url = f"http://127.0.0.0/admin/chscope/"
            headers = {
                "Accept": "application/json",
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json",
            }
            json_body = {
                "username": username,
                "scopes": scopes,
            }
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.put(url, headers=headers, json=json_body) as result:
                        data = await result.json()
            except ClientConnectorError as e:
                print(f"ClientConnectorError: {e}")
            else:
                print(json.dumps(data, indent=2))


        if __name__ == "__main__":
            asyncio.run(
                put_admin_change_scope(
                    access_token="kajfe0983qjaf309ajj3w8j3aij3a3",
                    username="Bob123",
                    scopes=["APIUser:Read", "APIUser:ChangePassword"],
                )
            )


    """
    if (
        update_user.username.lower() == current_user.username.lower()
        and "APIAdmin:Write" not in update_user.scopes
    ):
        raise APIError(
            status_code=status.HTTP_403_FORBIDDEN,
            content={
                "status": status.HTTP_403_FORBIDDEN,
                "message": "You can not remove the 'APIAdmin:Write' scope from your account.",
            },
            headers=None,
        )
    user = await auth_query.get_user(db, update_user.username)
    if not user:
        raise APIError(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "status": status.HTTP_404_NOT_FOUND,
                "message": "Username not found.",
            },
            headers=None,
        )
    await auth_query.change_scope(db=db, user=user, new_scope=update_user.scopes)
    return {
        "message": "Scopes Changed Successfully.",
        "status": status.HTTP_202_ACCEPTED,
    }
