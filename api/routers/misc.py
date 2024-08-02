import os
from typing import Union

import models.models as M
from fastapi import APIRouter, Depends, HTTPException, Security, status
from query import palapi as Q
from sqlmodel.ext.asyncio.session import AsyncSession
from utils import customresponses as R
from utils.auth import get_current_active_user
from utils.custompage import Page
from utils.database import get_session

router = APIRouter(
    tags=["Misc"],
    responses=R.responses,
    dependencies=(
        [Security(get_current_active_user, scopes=["APIUser:Read"])]
        if os.getenv("COMPOSE_PROFILES") == "USE_OAUTH2"
        else None
    ),
)


@router.get(
    "/all/{category}",
    response_model=Page[
        Union[
            M.Pals,
            M.BossPals,
            M.Items,
            M.Crafting,
            M.Breeding,
            M.BuildObjects,
            M.FoodEffect,
            M.Gear,
            M.SickPal,
            M.TechTree,
            M.PassiveSkills,
            M.NPC,
            M.Elixir,
        ]
    ],
    response_model_exclude_none=True,
    summary="Paginate full category",
)
async def getall(
    category: M.APIModels,
    db: AsyncSession = Depends(get_session),
):
    item = await Q.get_all(db, category.value)
    if len(item.items) != 0:
        return item
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Nothing Found"
        )


@router.get(
    "/npc/",
    response_model=Page[M.NPC],
    response_model_exclude_none=True,
    summary="Lookup NPC Information",
)
async def getnpc(
    name: str | None = None,
    db: AsyncSession = Depends(get_session),
):
    if name:
        item = await Q.get_npc(db, name)
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
