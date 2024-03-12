import os
from typing import Union

from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException, Query, Request, status
from fastapi.staticfiles import StaticFiles
from fastapi_pagination import add_pagination
from sqlmodel.ext.asyncio.session import AsyncSession

import models.models as M
import utils.descriptions as D
import utils.querydb as Q
from utils.custompage import Page
from utils.customresponses import responses
from utils.database import engine

load_dotenv(dotenv_path=".env")

app = FastAPI(
    title="Palworld API",
    description=D.description,
    version="0.0.1",
    contact={
        "name": "pyPalworldAPI GitHub",
        "url": "https://github.com/stolenvw/pyPalworldAPI",
    },
    license_info={
        "name": "MIT license",
        "identifier": "MIT",
    },
    openapi_tags=D.tags_metadata,
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
    docs_url=os.getenv("DOCS_URL"),
    redoc_url=os.getenv("REDOC_URL"),
)

add_pagination(app)
app.mount("/public", StaticFiles(directory="public"), name="public")


async def get_session():
    async with AsyncSession(engine) as session:
        yield session


@app.get(
    "/health",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=M.HealthCheck,
)
def get_health() -> M.HealthCheck:
    return M.HealthCheck(status="OK")


@app.get(
    "/items/",
    response_model=Page[M.Items],
    response_model_exclude_none=True,
    summary="Lookup Items Information",
    tags=["Items"],
    responses=responses,
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


@app.get(
    "/crafting/",
    response_model=Page[M.Crafting],
    response_model_exclude_none=True,
    summary="Lookup Crafting Information",
    tags=["Items"],
    responses=responses,
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


@app.get(
    "/gear/",
    response_model=Page[M.Gear],
    response_model_exclude_none=True,
    summary="Lookup Gear Information",
    tags=["Items"],
    responses=responses,
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


@app.get(
    "/pals/",
    response_model=Page[M.Pals],
    response_model_exclude_none=True,
    summary="Lookup Pal[s] Information",
    tags=["Pals"],
    responses=responses,
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
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Nothing Found"
        )


@app.get(
    "/bosspals/",
    response_model=Page[M.BossPals],
    response_model_exclude_none=True,
    summary="Lookup Boss Pal[s] Information",
    tags=["Pals"],
    responses=responses,
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
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Nothing Found"
        )


@app.get(
    "/foodeffect/",
    response_model=Page[M.FoodEffect],
    response_model_exclude_none=True,
    summary="Lookup Food Effects Information",
    tags=["Items"],
    responses=responses,
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


@app.get(
    "/breeding/",
    response_model=Page[M.Breeding],
    response_model_exclude_none=True,
    summary="Lookup Breeding Information",
    tags=["Pals"],
    responses=responses,
)
async def getbreeding(
    name: str,
    db: AsyncSession = Depends(get_session),
):
    if name:
        item = await Q.get_breeding(db, name)
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


@app.get(
    "/sickness/",
    response_model=Page[M.SickPal],
    response_model_exclude_none=True,
    summary="Lookup Sickness Information",
    tags=["Pals"],
    responses=responses,
)
async def getsickness(
    name: str,
    db: AsyncSession = Depends(get_session),
):
    if name:
        item = await Q.get_sickness(db, name)
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


@app.get(
    "/tech/",
    response_model=Page[M.TechTree],
    response_model_exclude_none=True,
    summary="Lookup Tech Tree Information",
    tags=["Items"],
    responses=responses,
)
async def gettech(
    name: str | None = None,
    level: int | None = Query(None, ge=1, le=50),
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


@app.get(
    "/build/",
    response_model=Page[M.BuidObjects],
    response_model_exclude_none=True,
    summary="Lookup Build Objects Information",
    tags=["Items"],
    responses=responses,
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


@app.get(
    "/passive/",
    response_model=Page[M.PassiveSkills],
    response_model_exclude_none=True,
    summary="Lookup Passive Skills Information",
    tags=["Pals"],
    responses=responses,
)
async def getpassive(
    name: str | None = None,
    db: AsyncSession = Depends(get_session),
):
    if name:
        item = await Q.get_passive(db, name)
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


@app.get(
    "/all/{category}",
    response_model=Page[
        Union[
            M.Pals,
            M.BossPals,
            M.Items,
            M.Crafting,
            M.Breeding,
            M.BuidObjects,
            M.FoodEffect,
            M.Gear,
            M.SickPal,
            M.TechTree,
            M.PassiveSkills,
            M.NPC,
        ]
    ],
    response_model_exclude_none=True,
    summary="Paginate full category",
    tags=["Misc"],
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


@app.get(
    "/npc/",
    response_model=Page[M.NPC],
    response_model_exclude_none=True,
    summary="Lookup NPC Information",
    tags=["Misc"],
    responses=responses,
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
