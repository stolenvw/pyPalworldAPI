import os

import models.models as M
import utils.examples as examples
from fastapi import APIRouter, Depends, Query, Request, Security, status
from query import palapi as Q
from sqlmodel.ext.asyncio.session import AsyncSession
from utils import customresponses as R
from utils.auth import get_current_active_user
from utils.customexception import APIException
from utils.custompage import Page
from utils.database import get_session

router = APIRouter(
    tags=["Pals"],
    responses=R.responses_400_401_404,
    dependencies=(
        [Security(get_current_active_user, scopes=["APIUser:Read"])]
        if os.getenv("COMPOSE_PROFILES") == "USE_OAUTH2"
        else None
    ),
)


@router.get(
    "/pals/",
    response_model=Page[M.Pals],
    response_model_exclude_none=True,
    summary="Lookup Pal[s] Information",
    openapi_extra={"x-codeSamples": examples.pals},
)
async def getpal(
    request: Request,
    name: str | None = Query(None, description="Pal name."),
    dexkey: str | None = Query(None, description="Paldex number."),
    typename: str | None = Query(None, alias="type"),
    suitability: str | None = None,
    drop: str | None = None,
    skill: str | None = None,
    nocturnal: bool | None = Query(
        None, description="False for day Pals, True for night Pals."
    ),
    db: AsyncSession = Depends(get_session),
):
    """
    Lookup Pal by options below:

    - **name**: Pal name to return information on.
    - **dexkey**: Paldex ID to return information on.
    - **type**: Returns Pals of this type.
    - **suitability**: Returns Pals with this suitability.
    - **drop**: Returns Pals that drop this item
    - **skill**: Returns Pals with this skill.
    - **nocturnal**: Return Pals that are daytime/nocturnal.
    """
    params = request.query_params
    item = await Q.get_pals(db, params)
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


@router.get(
    "/bosspals/",
    response_model=Page[M.BossPals],
    response_model_exclude_none=True,
    summary="Lookup Boss Pal[s] Information",
    openapi_extra={"x-codeSamples": examples.boss_pals},
)
async def getbosspal(
    request: Request,
    name: str | None = Query(None, description="Pal name."),
    typename: str | None = Query(None, alias="type"),
    suitability: str | None = None,
    drop: str | None = None,
    skill: str | None = None,
    nocturnal: bool | None = Query(
        None, description="False for day Pals, True for night Pals."
    ),
    db: AsyncSession = Depends(get_session),
):
    params = request.query_params
    item = await Q.get_bosspal(db, params)
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


@router.get(
    "/breeding/",
    response_model=Page[M.Breeding],
    response_model_exclude_none=True,
    summary="Lookup Breeding Information",
    openapi_extra={"x-codeSamples": examples.breeding},
)
async def getbreeding(
    name: str,
    db: AsyncSession = Depends(get_session),
):
    if name:
        item = await Q.get_breeding(db, name)
    else:
        raise APIException(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Missing one of the (name) params.",
            },
            headers=None,
        )
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


@router.get(
    "/sickness/",
    response_model=Page[M.SickPal],
    response_model_exclude_none=True,
    summary="Lookup Sickness Information",
    openapi_extra={"x-codeSamples": examples.sickness},
)
async def getsickness(
    name: str,
    db: AsyncSession = Depends(get_session),
):
    if name:
        item = await Q.get_sickness(db, name)
    else:
        raise APIException(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Missing one of the (name) params.",
            },
            headers=None,
        )
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


@router.get(
    "/passive/",
    response_model=Page[M.PassiveSkills],
    response_model_exclude_none=True,
    summary="Lookup Passive Skills Information",
    openapi_extra={"x-codeSamples": examples.passive},
)
async def getpassive(
    name: str | None = None,
    db: AsyncSession = Depends(get_session),
):
    if name:
        item = await Q.get_passive(db, name)
    else:
        raise APIException(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Missing one of the (name) params.",
            },
            headers=None,
        )
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
