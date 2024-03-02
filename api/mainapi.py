from fastapi import Depends, FastAPI, HTTPException, Query, Request, status
from fastapi.staticfiles import StaticFiles
from fastapi_pagination import Page, add_pagination
from sqlmodel.ext.asyncio.session import AsyncSession

import models.models as M
import utils.descriptions as D
import utils.querydb as Q
from utils.customresponses import responses
from utils.database import engine

app = FastAPI(
    title="Palworld API",
    description=D.description,
    version="0.0.1",
    license_info={
        "name": "MIT license",
        "identifier": "MIT",
    },
    openapi_tags=D.tags_metadata,
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
)
add_pagination(app)
app.mount("/public", StaticFiles(directory="public"), name="public")


async def get_session():
    async with AsyncSession(engine) as session:
        yield session


@app.get(
    "/items/",
    response_model=Page[M.Items],
    response_model_exclude_none=True,
    summary="Lookup Items Information",
    tags=["Items"],
    responses=responses,
)
async def getitems(
    name: str | None = None,
    variety: str | None = Query(None, alias="type"),
    db: AsyncSession = Depends(get_session),
):
    """
    Lookup items by one of the options below:

    - **name**: item name to return information on.
    - **type**: item type.
    """
    if name and variety:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Please only use one of the (name, variety) params at a time.",
        )
    if name or variety:
        item = await Q.get_item(db, name, variety)
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Missing one of the (name, variety) params.",
        )
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
    Lookup Pal by one of the options below:

    - **name**: Pal name to return information on.
    - **dexkey**: Paldex ID to return information on.
    - **type**: Returns Pals of this type.
    - **suitability**: Returns Pals with this suitability.
    - **drop**: Returns Pals that drop this item
    - **skill**: Returns Pals with this skill.
    - **nocturnal**: Return Pals that are daytime/nocturnal.
    """
    params = request.query_params
    if name:
        item = await Q.get_pal(db, name)
    elif dexkey:
        item = await Q.get_pal_by_dexid(db, dexkey)
    elif typename:
        item = await Q.get_pal_by_type(db, typename)
    elif suitability:
        item = await Q.get_pal_by_suitability(db, suitability)
    elif drop:
        item = await Q.get_pal_by_drops(db, drop)
    elif skill:
        item = await Q.get_pal_by_skills(db, skill)
    elif "nocturnal" in params:
        item = await Q.get_pal_by_nocturnal(db, nocturnal)
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Missing one of the (name, dexkey, typename, suitability, drop, skill) params.",
        )
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
    name: str,
    db: AsyncSession = Depends(get_session),
):
    if name:
        item = await Q.get_tech(db, name)
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
