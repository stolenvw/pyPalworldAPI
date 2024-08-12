from typing import Annotated

from fastapi import APIRouter, Depends, Form, Security, status
from models import auth_models as AuthModel
from query import auth as AuthQuery
from sqlmodel.ext.asyncio.session import AsyncSession
from utils.auth import (
    get_auth_session,
    get_current_active_user,
    get_password_hash,
    verify_password,
)
from utils.customexception import APIException
from utils.customresponses import pyPalworldAPIErrorResponses
from utils.examples import pyPalworldAPIExamples

router = APIRouter(
    prefix="/user",
    tags=["User"],
    responses=pyPalworldAPIErrorResponses.response_400_401,
)


@router.put(
    "/changepassword/",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Change your password.",
    response_model=AuthModel.MessageStatus,
    openapi_extra={"x-codeSamples": pyPalworldAPIExamples.user_change_password},
)
async def change_own_password(
    current_user: Annotated[
        AuthModel.User,
        Security(
            get_current_active_user, scopes=["APIUser:Read", "APIUser:ChangePassword"]
        ),
    ],
    current_password: str = Form(),
    new_password: str = Form(max_length=256, min_length=6),
    db: AsyncSession = Depends(get_auth_session),
):
    """
    ```Curl
    curl -X 'PUT' \ 
        'http://127.0.0.0/user/changepassword/' \ 
        -H 'Accept: application/json' \ 
        -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3' \ 
        -H 'Content-Type: application/x-www-form-urlencoded' \ 
        -d 'current_password=SomePass&new_password=SomeNewPass'
    ```
    """
    if not await verify_password(current_password, current_user.password):
        raise APIException(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Invalid Password.",
            },
            headers=None,
        )
    hashed_password = await get_password_hash(new_password)
    user = await AuthQuery.get_user(db, current_user.username)
    await AuthQuery.change_password(db=db, user=user, new_password=hashed_password)
    return {
        "message": "Password Changed Successfully.",
        "status": status.HTTP_202_ACCEPTED,
    }


@router.get(
    "/me/",
    response_model=AuthModel.UserResponse,
    summary="List User Info",
    openapi_extra={"x-codeSamples": pyPalworldAPIExamples.me},
)
async def get_user(
    current_user: Annotated[
        AuthModel.User, Security(get_current_active_user, scopes=["APIUser:Read"])
    ],
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
