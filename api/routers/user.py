from typing import Annotated

from fastapi import APIRouter, Depends, Form, HTTPException, Security, status
from models import auth_models as AuthModel
from query import auth as AuthQuery
from sqlmodel.ext.asyncio.session import AsyncSession
from utils import customresponses as R
from utils.auth import (
    get_auth_session,
    get_current_active_user,
    get_password_hash,
    verify_password,
)

router = APIRouter(
    prefix="/user",
    tags=["User"],
    responses={404: {"description": "Not found"}},
)


@router.put(
    "/changepassword/",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Change your password.",
    responses=R.response_401_404,
    response_model=AuthModel.MessageStatus,
)
async def change_own_password(
    current_user: Annotated[AuthModel.User, Security(get_current_active_user, scopes=["APIUser:Read", "APIUser:ChangePassword"])],
    current_password: str = Form(),
    new_password: str = Form(max_length=256, min_length=6),
    db: AsyncSession = Depends(get_auth_session),
):
    """
    ```
    curl -X 'PUT'
        'http://**APIURL**/user/changepassword/'
        -H 'accept: application/json'
        -H 'Authorization: Bearer **ACCESS TOKEN**'
        -H 'Content-Type: application/x-www-form-urlencoded'
        -d 'current_password=**CURRENT-PASSWORD**&new_password=**NEW-PASSWORD**'
    ```
    """
    if not await verify_password(current_password, current_user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid Password",
        )
    hashed_password = await get_password_hash(new_password)
    user = await AuthQuery.get_user(db, current_user.username)
    await AuthQuery.change_password(
        db=db, user=user, new_password=hashed_password
    )
    return {
        "message": "Password Changed Successfully.",
        "status": status.HTTP_202_ACCEPTED,
    }


@router.get(
    "/me/",
    response_model=AuthModel.UserResponse,
    summary="List User Info",
    responses=R.responses,
)
async def get_user(
    current_user: Annotated[AuthModel.User, Security(get_current_active_user, scopes=["APIUser:Read"])],
):
    """
    ```
    curl -X 'GET'
        'http://**APIURL**/user/me/'
        -H 'accept: application/json'
        -H 'Authorization: Bearer **ACCESS TOKEN**'
    ```
    """
    return current_user
