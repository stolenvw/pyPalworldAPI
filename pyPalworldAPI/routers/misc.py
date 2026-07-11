import os
from typing import Union

import models.models as M
from fastapi import APIRouter, Depends, Security, status
from query import palapi as Q
from sqlmodel.ext.asyncio.session import AsyncSession
from utils.auth import get_current_active_user
from utils.customexception import APIException
from utils.custompage import Page
from utils.customresponses import pyPalworldAPIErrorResponses
from utils.database import get_session
from utils.examples import pyPalworldAPIExamples

router = APIRouter(
    tags=["Misc"],
    responses=pyPalworldAPIErrorResponses.responses_400_401_404,
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
    openapi_extra={"x-codeSamples": pyPalworldAPIExamples.alls},
)
async def getall(
    category: M.APIModels,
    db: AsyncSession = Depends(get_session),
):
    """
    Paginate full category.
    \f
    Parameters
    ----------
    category : {"pals", "bosspals", "items", "breeding", "buildobjects", "crafting", "foodeffect", "gear", "sickpal", "techtree", "passiveskills", "npc", "elixir"}
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
    APIException
        HTTP responses with errors.
    RequestValidationError
        When a request contains invalid data.
        
    Examples
    -------
    Curl::

        curl -X 'GET' \ 
            'http://127.0.0.0/all/pals?page=1&size=50' \ 
            -H 'Accept: application/json' \ 
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
    item = await Q.get_all(db, category.value)
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
    "/npc/",
    response_model=Page[M.NPC],
    response_model_exclude_none=True,
    summary="Lookup NPC Information",
    openapi_extra={"x-codeSamples": pyPalworldAPIExamples.npc},
)
async def getnpc(
    name: str | None = None,
    db: AsyncSession = Depends(get_session),
):
    """
    Lookup npc info.
    \f
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
    APIException
        HTTP responses with errors.
    RequestValidationError
        When a request contains invalid data.
        
    Examples
    -------
    Curl::

        curl -X 'GET' \ 
            'http://127.0.0.0/npc/?name=Wandering%20Merchant&page=1&size=50' \ 
            -H 'Accept: application/json' \ 
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
        item = await Q.get_npc(db, name)
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
