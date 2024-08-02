from typing import Annotated

from fastapi import APIRouter, Depends, Form, HTTPException, Security, status
from models import auth_models as AuthModel
from query import auth as AuthQuery
from sqlmodel.ext.asyncio.session import AsyncSession
from utils import customresponses as R
from utils.auth import get_auth_session, get_current_active_user, get_password_hash
from utils.custompage import Page

router = APIRouter(
    prefix="/admin",
    tags=["Admin"],
    dependencies=[Security(get_current_active_user, scopes=["APIAdmin:Write"])],
    responses={404: {"description": "Not found"}},
)


@router.post(
    "/adduser/",
    status_code=status.HTTP_201_CREATED,
    response_model=AuthModel.RegistrationUserResponse,
    summary="Add User",
    responses=R.adduser_responses,
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
        raise HTTPException(
            detail="Username is taken", status_code=status.HTTP_409_CONFLICT
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
    responses=R.response_401_404,
    response_model=AuthModel.MessageStatus,
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
        raise HTTPException(
            detail="Username not found", status_code=status.HTTP_404_NOT_FOUND
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
    responses=R.response_401_404,
    response_model=AuthModel.MessageStatus,
)
async def deleteuser(
    current_user: Annotated[AuthModel.User, Security(get_current_active_user, scopes=["APIAdmin:Write"])],
    username: str = Form(),
    db: AsyncSession = Depends(get_auth_session),
):
    """
    ### Delete User:

    - **username**: Username.

    ```
    curl -X 'DELETE'
        'http://**APIURL**/admin/deleteuser/'
        -H 'accept: application/json'
        -H 'Authorization: Bearer **ACCESS TOKEN**'
        -H 'Content-Type: application/x-www-form-urlencoded'
        -d 'username=**USERNAME**'
    ```
    """
    user_credentials = AuthModel.UserName(username=username)
    if user_credentials.username.lower() == current_user.username.lower():
        raise HTTPException(
            detail="You can not delete your own admin account",
            status_code=status.HTTP_403_FORBIDDEN,
        )
    user = await AuthQuery.get_user(db, user_credentials.username)
    if not user:
        raise HTTPException(
            detail="Username not found", status_code=status.HTTP_404_NOT_FOUND
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
    responses=R.responses,
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
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Nothing Found"
        )


@router.put(
    "/userdisable/",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Disable/Enable User",
    responses=R.response_401_404,
    response_model=AuthModel.MessageStatus,
)
async def userdisable(
    current_user: Annotated[AuthModel.User, Security(get_current_active_user, scopes=["APIAdmin:Write"])],
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
        raise HTTPException(
            detail="You can not change the disabled status of your own account.",
            status_code=status.HTTP_403_FORBIDDEN,
        )
    user = await AuthQuery.get_user(db, username)
    if not user:
        raise HTTPException(
            detail="Username not found", status_code=status.HTTP_404_NOT_FOUND
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
    responses=R.response_401_404,
    response_model=AuthModel.MessageStatus,
)
async def scope_change(
    current_user: Annotated[AuthModel.User, Security(get_current_active_user, scopes=["APIAdmin:Write"])],
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
    if update_user.username.lower() == current_user.username.lower():
        raise HTTPException(
            detail="You can not change the scopes of your own account.",
            status_code=status.HTTP_403_FORBIDDEN,
        )
    user = await AuthQuery.get_user(db, update_user.username)
    if not user:
        raise HTTPException(
            detail="Username not found", status_code=status.HTTP_404_NOT_FOUND
        )
    await AuthQuery.change_scope(db=db, user=user, new_scope=update_user.scopes)
    return {
        "message": "Scopes Changed Successfully.",
        "status": status.HTTP_202_ACCEPTED,
    }
