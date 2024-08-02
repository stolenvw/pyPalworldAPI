import os

import models.models as M
from fastapi import APIRouter, Depends, HTTPException, Query, Request, Security, status
from query import palapi as Q
from sqlmodel.ext.asyncio.session import AsyncSession
from utils import customresponses as R
from utils.auth import get_current_active_user
from utils.custompage import Page
from utils.database import get_session

router = APIRouter(
    tags=["Items"],
    responses=R.responses,
    dependencies=(
        [Security(get_current_active_user, scopes=["APIUser:Read"])]
        if os.getenv("COMPOSE_PROFILES") == "USE_OAUTH2"
        else None
    ),
)


@router.get(
    "/items/",
    response_model=Page[M.Items],
    response_model_exclude_none=True,
    summary="Lookup Items Information",
)
async def getitems(
    request: Request,
    name: str | None = None,
    variety: str | None = Query(None, alias="type"),
    db: AsyncSession = Depends(get_session),
):
    """
    Lookup items options below:

    - **name**: item name to return information on.
    - **type**: item type.
    """
    params = request.query_params
    item = await Q.get_item(db, params)
    if len(item.items) != 0:
        return item
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Nothing Found"
        )


@router.get(
    "/crafting/",
    response_model=Page[M.Crafting],
    response_model_exclude_none=True,
    summary="Lookup Crafting Information",
)
async def getcrafting(
    name: str = Query(None, description="Item you want to make."),
    db: AsyncSession = Depends(get_session),
):
    if name:
        item = await Q.get_crafting(db, name)
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Missing one of the (name) params.",
        )
    if len(item.items) != 0:
        return item
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Nothing Found"
        )


@router.get(
    "/gear/",
    response_model=Page[M.Gear],
    response_model_exclude_none=True,
    summary="Lookup Gear Information",
)
async def getgear(
    name: str,
    db: AsyncSession = Depends(get_session),
):
    if name:
        item = await Q.get_gear(db, name)
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Missing one of the (name) params.",
        )
    if len(item.items) != 0:
        return item
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Nothing Found"
        )


@router.get(
    "/foodeffect/",
    response_model=Page[M.FoodEffect],
    response_model_exclude_none=True,
    summary="Lookup Food Effects Information",
)
async def getfoodeffect(
    name: str,
    db: AsyncSession = Depends(get_session),
):
    if name:
        item = await Q.get_foodeffects(db, name)
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Missing one of the (name) params.",
        )
    if len(item.items) != 0:
        return item
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Nothing Found"
        )


@router.get(
    "/tech/",
    response_model=Page[M.TechTree],
    response_model_exclude_none=True,
    summary="Lookup Tech Tree Information",
)
async def gettech(
    name: str | None = None,
    level: int | None = Query(None, ge=1, le=55),
    db: AsyncSession = Depends(get_session),
):
    if name:
        item = await Q.get_tech(db, name)
    elif level:
        item = await Q.get_tech_by_level(db, level)
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Missing one of the (name, level) params.",
        )
    if len(item.items) != 0:
        return item
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Nothing Found"
        )


@router.get(
    "/build/",
    response_model=Page[M.BuildObjects],
    response_model_exclude_none=True,
    summary="Lookup Build Objects Information",
)
async def getbuild(
    name: str | None = None,
    category: str | None = None,
    db: AsyncSession = Depends(get_session),
):
    if name:
        item = await Q.get_build(db, name)
    elif category:
        item = await Q.get_build_by_category(db, category)
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Missing one of the (name, category) params.",
        )
    if len(item.items) != 0:
        return item
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Nothing Found"
        )


@router.get(
    "/elixir/",
    response_model=Page[M.Elixir],
    response_model_exclude_none=True,
    summary="Lookup Elixir Information",
)
async def getelixir(
    name: str | None = None,
    db: AsyncSession = Depends(get_session),
):
    if name:
        item = await Q.get_elixir(db, name)
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Missing one of the (name) params.",
        )
    if len(item.items) != 0:
        return item
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Nothing Found"
        )
