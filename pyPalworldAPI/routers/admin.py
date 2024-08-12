from typing import Annotated

from fastapi import APIRouter, Depends, Form, Security, status
from models import auth_models as AuthModel
from query import auth as AuthQuery
from sqlmodel.ext.asyncio.session import AsyncSession
from utils.auth import get_auth_session, get_current_active_user, get_password_hash
from utils.customexception import APIException
from utils.custompage import Page
from utils.customresponses import pyPalworldAPIErrorResponses
from utils.examples import pyPalworldAPIExamples

router = APIRouter(
    prefix="/admin",
    tags=["Admin"],
    dependencies=[Security(get_current_active_user, scopes=["APIAdmin:Write"])],
)


@router.post(
    "/adduser/",
    status_code=status.HTTP_201_CREATED,
    response_model=AuthModel.RegistrationUserResponse,
    summary="Add User",
    responses=pyPalworldAPIErrorResponses.response_401_409,
    openapi_extra={"x-codeSamples": pyPalworldAPIExamples.add_user},
)
async def adduser(
    new_user: AuthModel.UserInput,
    db: AsyncSession = Depends(get_auth_session),
):
    """
    ### Add API User:

    - **username**: Username.
    - **password**: Password.
    - **scopes**: List of scopes.
      - ***Valid Scopes***
        - **APIAdmin:Write**: Can add users.
        - **APIUser:Read**: Read API items.
        - **APIUser:ChangePassword**: User can change there password.
    - **disabled**: Bool.

    ```
    curl -X 'POST'
        'http://**APIURL**/admin/adduser/'
        -H 'accept: application/json'
        -H 'Authorization: Bearer **ACCESS TOKEN**'
        -H 'Content-Type: application/json'
        -d '{
                "username": "**USERNAME**",
                "password": "**PASSWORD**",
                "scopes": [
                  "APIUser:Read"
                ],
                "disabled": false
            }'
    ```
    """
    user = await AuthQuery.get_user(db, new_user.username)
    if user:
        raise APIException(
            status_code=status.HTTP_409_CONFLICT,
            content={
                "status": status.HTTP_409_CONFLICT,
                "message": "Username is taken.",
            },
            headers=None,
        )
    hashed_password = await get_password_hash(new_user.password)
    new_user.password = hashed_password
    add_user = AuthModel.User(
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
    responses=pyPalworldAPIErrorResponses.response_401_404,
    response_model=AuthModel.MessageStatus,
    openapi_extra={"x-codeSamples": pyPalworldAPIExamples.admin_change_password},
)
async def changepassword(
    username: str = Form(),
    new_password: str = Form(max_length=256, min_length=6),
    db: AsyncSession = Depends(get_auth_session),
):
    """
    ### Change users password:

    *_Changing password will make any access/refresh token the user currently has invalid._

    - **username**: Username.
    - **password**: Password.

    ```
    curl -X 'PUT'
        'http://**APIURL**/admin/chpass/'
        -H 'accept: application/json'
        -H 'Authorization: Bearer **ACCESS TOKEN**'
        -H 'Content-Type: application/x-www-form-urlencoded'
        -d 'username=**USERNAME**&new_password=**PASSWORD**'
    ```
    """
    pass_reset = AuthModel.PassReset(username=username, new_password=new_password)
    user = await AuthQuery.get_user(db, pass_reset.username)
    if not user:
        raise APIException(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "status": status.HTTP_404_NOT_FOUND,
                "message": "Username not found.",
            },
            headers=None,
        )
    hashed_password = await get_password_hash(pass_reset.new_password)
    await AuthQuery.change_password(db=db, user=user, new_password=hashed_password)
    return {
        "message": "Password Changed Successfully.",
        "status": status.HTTP_202_ACCEPTED,
    }


@router.delete(
    "/deleteuser/",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Delete User",
    responses=pyPalworldAPIErrorResponses.response_401_403_404,
    response_model=AuthModel.MessageStatus,
    openapi_extra={"x-codeSamples": pyPalworldAPIExamples.delete_user},
)
async def deleteuser(
    current_user: Annotated[
        AuthModel.User, Security(get_current_active_user, scopes=["APIAdmin:Write"])
    ],
    username: str,
    db: AsyncSession = Depends(get_auth_session),
):
    """
    ### Delete User:

    - **username**: Username.

    ```
    curl -X 'DELETE'
        'http://**APIURL**/admin/deleteuser/?username=**USERNAME**'
        -H 'Accept: application/json'
        -H 'Authorization: Bearer **ACCESS TOKEN**'
    ```
    """
    user_credentials = AuthModel.UserName(username=username)
    if user_credentials.username.lower() == current_user.username.lower():
        raise APIException(
            status_code=status.HTTP_403_FORBIDDEN,
            content={
                "status": status.HTTP_403_FORBIDDEN,
                "message": "You can not delete your own admin account.",
            },
            headers=None,
        )
    user = await AuthQuery.get_user(db, user_credentials.username)
    if not user:
        raise APIException(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "status": status.HTTP_404_NOT_FOUND,
                "message": "Username not found.",
            },
            headers=None,
        )
    await AuthQuery.delete_user(db=db, user=user)
    return {
        "message": "User Deleted Successfully.",
        "status": status.HTTP_202_ACCEPTED,
    }


@router.get(
    "/users/",
    response_model=Page[AuthModel.UserResponse],
    summary="List Users",
    responses=pyPalworldAPIErrorResponses.response_401_404,
    openapi_extra={"x-codeSamples": pyPalworldAPIExamples.list_users},
)
async def list_user(
    db: AsyncSession = Depends(get_auth_session),
):
    """
    ### List All Users:

    ```
    curl -X 'GET'
        'http://**APIURL**/admin/users/'
        -H 'accept: application/json'
        -H 'Authorization: Bearer **ACCESS TOKEN**'
    ```
    """
    item = await AuthQuery.list_users(db)
    if len(item.items) != 0:
        return item
    else:
        raise APIException(
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
    responses=pyPalworldAPIErrorResponses.response_401_403_404,
    response_model=AuthModel.MessageStatus,
    openapi_extra={"x-codeSamples": pyPalworldAPIExamples.user_disable},
)
async def userdisable(
    current_user: Annotated[
        AuthModel.User, Security(get_current_active_user, scopes=["APIAdmin:Write"])
    ],
    username: Annotated[str, Form()],
    disabled: Annotated[bool, Form()],
    db: AsyncSession = Depends(get_auth_session),
):
    """
    ### Disable / Enable A Users Account:

    - **username**: Username.
    - **disabled**: Bool.

    ```
    curl -X 'PUT'
        'http://**APIURL**/admin/userdisable/'
        -H 'accept: application/json'
        -H 'Authorization: Bearer **ACCESS TOKEN**'
        -H 'Content-Type: application/x-www-form-urlencoded'
        -d 'username=**USERNAME**&disabled=**TRUE**'
    ```
    """
    if username.lower() == current_user.username.lower():
        raise APIException(
            status_code=status.HTTP_403_FORBIDDEN,
            content={
                "status": status.HTTP_403_FORBIDDEN,
                "message": "You can not change the disabled status of your own account.",
            },
            headers=None,
        )
    user = await AuthQuery.get_user(db, username)
    if not user:
        raise APIException(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "status": status.HTTP_404_NOT_FOUND,
                "message": "Username not found.",
            },
            headers=None,
        )
    await AuthQuery.change_user_status(db, user, disabled)
    return {
        "message": f"Username Disabled: {disabled}.",
        "status": status.HTTP_202_ACCEPTED,
    }


@router.put(
    "/chscope/",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Change Users Scopes",
    responses=pyPalworldAPIErrorResponses.response_401_403_404,
    response_model=AuthModel.MessageStatus,
    openapi_extra={"x-codeSamples": pyPalworldAPIExamples.change_scopes},
)
async def scope_change(
    current_user: Annotated[
        AuthModel.User, Security(get_current_active_user, scopes=["APIAdmin:Write"])
    ],
    update_user: AuthModel.UserScopeChange,
    db: AsyncSession = Depends(get_auth_session),
):
    """
    ### Change Users Scopes:

    - **username**: Username.
    - **scopes**: New list of scopes.
      - ***Valid Scopes***
        - **APIAdmin:Write**: Can add users.
        - **APIUser:Read**: Read API items.
        - **APIUser:ChangePassword**: User can change there password.

    ```
    curl -X 'PUT'
        'http://**APIURL**/admin/chscope/'
        -H 'accept: application/json'
        -H 'Authorization: Bearer **ACCESS TOKEN**'
        -H 'Content-Type: application/json'
        -d '{
                "username": "**USERNAME**",
                "scopes": [
                  "APIUser:Read"
                ],
            }'
    ```
    """
    if (
        update_user.username.lower() == current_user.username.lower()
        and "APIAdmin:Write" not in update_user.scopes
    ):
        raise APIException(
            status_code=status.HTTP_403_FORBIDDEN,
            content={
                "status": status.HTTP_403_FORBIDDEN,
                "message": "You can not remove the 'APIAdmin:Write' scope from your account.",
            },
            headers=None,
        )
    user = await AuthQuery.get_user(db, update_user.username)
    if not user:
        raise APIException(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "status": status.HTTP_404_NOT_FOUND,
                "message": "Username not found.",
            },
            headers=None,
        )
    await AuthQuery.change_scope(db=db, user=user, new_scope=update_user.scopes)
    return {
        "message": "Scopes Changed Successfully.",
        "status": status.HTTP_202_ACCEPTED,
    }
