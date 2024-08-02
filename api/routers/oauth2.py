import random
from datetime import datetime, timedelta, timezone
from typing import Annotated

from fastapi import APIRouter, BackgroundTasks, Depends, Form, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from models import auth_models as AuthModel
from query import auth as AuthQuery
from sqlmodel.ext.asyncio.session import AsyncSession
from utils import auth as AuthUtils
from utils import customresponses as R

router = APIRouter(
    prefix="/oauth2",
    tags=["Auth"],
    responses=R.response_440_401,
)


@router.post(
    "/login/",
    status_code=status.HTTP_200_OK,
    response_model=AuthModel.LoginResponse,
)
async def login(
    user_credentials: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(AuthUtils.get_auth_session),
):
    """
    ```
    curl -X 'POST'
        'http://**APIURL**/oauth2/login/'
        -H 'accept: application/json'
        -H 'Content-Type: application/x-www-form-urlencoded'
        -d 'username=**USERNAME**&password=**PASSWORD**'
    ```
    """
    user = await AuthQuery.authenticate_user(db, user_credentials.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Username or Password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if user.disabled == True:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Account Disabled"
        )
    if not await AuthUtils.verify_password(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Username or Password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    refresh_token_check = await AuthQuery.refresh_token_delete(db, user_id=user.ID)
    access_token_expires = timedelta(minutes=AuthUtils.ACCESS_TOKEN_EXPIRE_MINUTES)
    refresh_token_expires = timedelta(days=AuthUtils.REFRESH_TOKEN_EXPIRE_DAYS)
    access_token = await AuthUtils.create_access_token(
        data={"sub": user.username, "scopes": user.scopes},
        expires_delta=access_token_expires,
    )
    refresh_token = await AuthUtils.create_refresh_token(
        data={"sub": user.username, "scopes": user.scopes},
        expires_delta=refresh_token_expires,
    )
    refresh_token_dict = {
        "user_id": user.ID,
        "refresh_token": refresh_token,
    }
    user_scopes = user.scopes
    refresh_token_db_data = AuthModel.RefreshToken(**refresh_token_dict)
    await AuthQuery.store_token(db=db, user_id=user.ID, token=access_token)
    if refresh_token_check:
        refresh_token_check.refresh_token = refresh_token
        refresh_token_check.created_at = datetime.now(timezone.utc)
        db.add(refresh_token_check)
        await db.commit()
    else:
        db.add(refresh_token_db_data)
        await db.commit()
    r_token = AuthModel.RefreshTokenInfo(
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
    response_model=AuthModel.RefreshResponse,
)
async def get_new_access_token(
    token: Annotated[str, Form()],
    grant_type: Annotated[str, Form()],
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(AuthUtils.get_auth_session),
):
    """
    ```
    curl -X 'POST'
        'http://**APIURL**/oauth2/refresh/'
        -H 'accept: application/json'
        -H 'Content-Type: application/x-www-form-urlencoded'
        -d 'token=**REFRESH TOKEN**&grant_type=refresh_token'
    ```
    """
    background_tasks.add_task(AuthUtils.remove_old_tokens, db)
    if grant_type != "refresh_token":
        credential_exception = HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid Grant Type",
        )
        raise credential_exception
    refresh_data = await AuthUtils.verify_refresh_token(db, token)
    access_token_expires = timedelta(minutes=AuthUtils.ACCESS_TOKEN_EXPIRE_MINUTES)
    refresh_token_expires = timedelta(days=AuthUtils.REFRESH_TOKEN_EXPIRE_DAYS)
    new_access_token = await AuthUtils.create_access_token(
        {"sub": refresh_data.username, "scopes": refresh_data.scopes},
        expires_delta=access_token_expires,
    )
    user = await AuthQuery.authenticate_user(db, refresh_data.username)
    if (
        random.randrange(refresh_token_expires.total_seconds())
        > (
            datetime.fromtimestamp(refresh_data.exp, tz=timezone.utc)
            - datetime.now(timezone.utc)
        ).total_seconds()
    ):
        refresh_token_check = await AuthQuery.refresh_token_delete(db, user_id=user.ID)
        refresh_token = await AuthUtils.create_refresh_token(
            data={"sub": user.username, "scopes": user.scopes},
            expires_delta=refresh_token_expires,
        )
        refresh_token_check.refresh_token = refresh_token
        refresh_token_check.created_at = datetime.now(timezone.utc)
        db.add(refresh_token_check)
        await db.commit()
        r_token = AuthModel.RefreshTokenInfo(
            token=refresh_token, expires_in=int(refresh_token_expires.total_seconds())
        )
    else:
        refresh_token_expire_in = (
            datetime.fromtimestamp(refresh_data.exp, tz=timezone.utc)
            - datetime.now(timezone.utc)
        ).total_seconds()
        r_token = AuthModel.RefreshTokenInfo(
            token=token, expires_in=int(refresh_token_expire_in)
        )
    a_token = AuthModel.AccessTokenInfo(
        token_type="Bearer",
        access_token=new_access_token,
        expires_in=int(access_token_expires.total_seconds()),
    )
    await AuthQuery.store_token(db=db, user_id=user.ID, token=new_access_token)
    return {
        "access_token": a_token,
        "refresh_token": r_token,
        "status": status.HTTP_200_OK,
    }
