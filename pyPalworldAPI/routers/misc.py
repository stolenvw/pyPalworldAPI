r"""Provide misc helpers."""

import os
from typing import Literal, Union

from fastapi import APIRouter, Depends, Query, Security, status
from sqlmodel.ext.asyncio.session import AsyncSession

from pyPalworldAPI.models import models
from pyPalworldAPI.query import palapi as palapi_query
from pyPalworldAPI.utils.auth import get_current_active_user
from pyPalworldAPI.utils.customexception import APIError
from pyPalworldAPI.utils.custompage import Page
from pyPalworldAPI.utils.customresponses import PalworldAPIErrorResponses
from pyPalworldAPI.utils.database import get_session
from pyPalworldAPI.utils.examples import PalworldAPIExamples

router = APIRouter(
    tags=["Misc"],
    responses=PalworldAPIErrorResponses.responses_400_401_404,
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
            models.Pals,
            models.BossPals,
            models.Items,
            models.Crafting,
            models.Breeding,
            models.BuildObjects,
            models.FoodEffect,
            models.Gear,
            models.SickPal,
            models.TechTree,
            models.PassiveSkills,
            models.NPC,
            models.Elixir,
            models.MapLocations,
        ]
    ],
    response_model_exclude_none=True,
    summary="Paginate full category",
    openapi_extra={"x-codeSamples": PalworldAPIExamples.alls},
)
async def getall(
    category: models.APIModels,
    lang: str = Query("en", description="Localized text language code."),
    db: AsyncSession = Depends(get_session),
):
    r"""Paginate full category.

    \f.

    Parameters
    ----------
    category : {"pals", "bosspals", "items", "breeding", "buildobjects", "crafting", "foodeffect", "gear", "sickpal", "techtree", "passiveskills", "npc", "elixir", "maplocations"}
        Category to get
    page : int, default: 1
        Page number to return
    size: int, default: 50
        Items to return on the page

    Returns
    -------
    json

    Raises
    ------
    APIError
        HTTP responses with errors.
    RequestValidationError
        When a request contains invalid data.

    Examples
    --------
    Curl::

        curl -X 'GET' \\
            'http://127.0.0.0/all/pals?page=1&size=50' \\
            -H 'Accept: application/json' \\
            -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'

    Python::

        import asyncio
        import json

        import aiohttp
        from aiohttp.client_exceptions import ClientConnectorError


        async def get_all(category: str, access_token: str):
            url = f"http://127.0.0.0/all/{category}"
            headers = {
                "Accept": "application/json",
                "Authorization": f"Bearer {access_token}",
            }
            params = {"page": 1, "size": 50}
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(url, headers=headers, params=params) as result:
                        data = await result.json()
            except ClientConnectorError as e:
                print(f"ClientConnectorError: {e}")
            else:
                print(json.dumps(data, indent=2))


        if __name__ == "__main__":
            asyncio.run(
                get_all(category="pals", access_token="kajfe0983qjaf309ajj3w8j3aij3a3")
            )


    """
    item = await palapi_query.get_all(db, category.value, lang=lang)
    if len(item.items) != 0:
        return item
    else:
        raise APIError(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "status": status.HTTP_404_NOT_FOUND,
                "message": "Nothing Found.",
            },
            headers=None,
        )


@router.get(
    "/npc/",
    response_model=Page[models.NPC],
    response_model_exclude_none=True,
    summary="Lookup NPC Information",
    openapi_extra={"x-codeSamples": PalworldAPIExamples.npc},
)
async def getnpc(
    name: str | None = None,
    lang: str = Query("en", description="Localized text language code."),
    db: AsyncSession = Depends(get_session),
):
    r"""Lookup npc info.

    \f.

    Parameters
    ----------
    name : str
        NPC to get stats for
    page : int, default: 1
        Page number to return
    size: int, default: 50
        Items to return on the page

    Returns
    -------
    json
        ::

        {
          "items": [
            {
              "ID": 0,
              "Name": "string",
              "DevName": "string",
              "Asset": "string",
              "Genus": "string",
              "Weapon": "string",
              "Stats": {
                "HP": 0,
                "Attack": {
                  "Melee": 0,
                  "Ranged": 0
                },
                "Defense": 0,
                "Stamina": 0,
                "Speed": {
                  "Walk": 0,
                  "Run": 0,
                  "Ride": 0
                },
                "Support": 0,
                "Food": 0,
                "CraftSpeed": 0,
                "TransportSpeed": 0,
                "EnemyMaxHPRate": 0,
                "EnemyReceiveDamageRate": 0,
                "EnemyInflictDamageRate": 0
              },
              "Rarity": 0,
              "Price": 0,
              "Size": "string",
              "AIResponse": "string",
              "NooseTrap": true,
              "Suitability": [
                {
                  "Name": "string",
                  "Image": "string",
                  "Level": 0
                }
              ],
              "IsRaidBoss": true
            }
          ],
          "total": 0,
          "page": 0,
          "size": 0,
          "pages": 0
        }

    Raises
    ------
    APIError
        HTTP responses with errors.
    RequestValidationError
        When a request contains invalid data.

    Examples
    --------
    Curl::

        curl -X 'GET' \\
            'http://127.0.0.0/npc/?name=Wandering%20Merchant&page=1&size=50' \\
            -H 'Accept: application/json' \\
            -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'

    Python::

        import asyncio
        import json

        import aiohttp
        from aiohttp.client_exceptions import ClientConnectorError


        async def get_npc(name: str, access_token: str):
            url = "http://127.0.0.0/npc/"
            headers = {
                "Accept": "application/json",
                "Authorization": f"Bearer {access_token}",
            }
            params = {"name": name, "page": 1, "size": 50}
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(url, headers=headers, params=params) as result:
                        data = await result.json()
            except ClientConnectorError as e:
                print(f"ClientConnectorError: {e}")
            else:
                print(json.dumps(data, indent=2))


        if __name__ == "__main__":
            asyncio.run(
                get_npc(
                    name="Wandering Merchant", access_token="kajfe0983qjaf309ajj3w8j3aij3a3"
                )
            )


    """
    if name:
        item = await palapi_query.get_npc(db, name, lang=lang)
    else:
        raise APIError(
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
        raise APIError(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "status": status.HTTP_404_NOT_FOUND,
                "message": "Nothing Found.",
            },
            headers=None,
        )


@router.get(
    "/map-locations/",
    response_model=Page[models.MapLocations],
    response_model_exclude_none=True,
    summary="Lookup Map Locations",
)
async def get_map_locations(
    category: str | None = Query(
        None,
        description="Filter locations by category.",
    ),
    map: Literal["world", "tree"] | None = Query(
        None,
        description="Filter locations to the world or tree map.",
    ),
    db: AsyncSession = Depends(get_session),
):
    r"""Lookup map location info.

    \f.

    Parameters
    ----------
    category : str | None
        Optional category filter.
    map : {"world", "tree"} | None
        Optional map filter.
    page : int, default: 1
        Page number to return
    size: int, default: 50
        Items to return on the page

    Returns
    -------
    json

    Raises
    ------
    APIError
        HTTP responses with errors.
    RequestValidationError
        When a request contains invalid data.


    """
    item = await palapi_query.get_map_locations(db, category=category, map_name=map)
    if len(item.items) != 0:
        return item
    else:
        raise APIError(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "status": status.HTTP_404_NOT_FOUND,
                "message": "Nothing Found.",
            },
            headers=None,
        )
