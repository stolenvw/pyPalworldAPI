import os

import models.models as M
from fastapi import APIRouter, Depends, Query, Request, Security, status
from query import palapi as Q
from sqlmodel.ext.asyncio.session import AsyncSession
from utils.auth import get_current_active_user
from utils.customexception import APIException
from utils.custompage import Page
from utils.customresponses import pyPalworldAPIErrorResponses
from utils.database import get_session
from utils.examples import pyPalworldAPIExamples

router = APIRouter(
    tags=["Pals"],
    responses=pyPalworldAPIErrorResponses.responses_400_401_404,
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
    openapi_extra={"x-codeSamples": pyPalworldAPIExamples.pals},
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
    Lookup pal info.
    \f
    Parameters
    ----------
    name : str, optional
        Pal name to return information on
    dexkey : str, optional
        Paldex ID to return information on
    type : str, optional
        Returns Pals of this type
    suitability : str, optional
        Returns Pals with this suitability
    drop : str, optional
        Returns Pals that drop this item
    skill : str, optional
        Returns Pals with this skill
    nocturnal : bool, optional
        Return Pals that are daytime/nocturnal
    page : int, default: 1
        Page number to return
    size: int, default: 50
        Items to return on the page


    .. note:: Need to supply at lest one of the ``name``, ``dexkey``, ``type``, ``suitability``, ``drop``, ``skill``, ``nocturnal`` parameters.
    
    Returns
    -------
    json
        ::

        {
          "items": [
            {
              "ID": 0,
              "DexKey": "string",
              "Image": "string",
              "Name": "string",
              "Wiki": "string",
              "WikiImage": "string",
              "Types": [
                {
                  "Name": "string",
                  "Image": "string"
                }
              ],
              "Suitability": [
                {
                  "Name": "string",
                  "Image": "string",
                  "Level": 0
                }
              ],
              "Drops": [
                {
                  "Name": "string",
                  "Rate": 0,
                  "Min": 0,
                  "Max": 0
                }
              ],
              "Aura": {
                "Name": "string",
                "Description": "string",
                "Image": "string",
                "Tech": "string"
              },
              "Description": "string",
              "Skills": [
                {
                  "Name": "string",
                  "Type": "string",
                  "Description": "string",
                  "Level": 0,
                  "Cooldown": 0,
                  "Power": 0
                }
              ],
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
              "Asset": "string",
              "Genus": "string",
              "Rarity": 0,
              "Price": 0,
              "Size": "string",
              "Maps": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string"
              },
              "Breeding": {
                "Rank": 0,
                "Order": 0,
                "MaleProbability": 0
              },
              "AIResponse": "string",
              "Nocturnal": true,
              "Predator": true,
              "NooseTrap": true,
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
            'http://127.0.0.0/pals/?name=lamball&page=1&size=50' \ 
            -H 'Accept: application/json' \ 
            -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'

    Python::

        import asyncio
        import json

        import aiohttp
        from aiohttp.client_exceptions import ClientConnectorError


        async def get_pals(name: str, access_token: str):
            url = "http://127.0.0.0/pals/"
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
                get_pals(name="lamball", access_token="kajfe0983qjaf309ajj3w8j3aij3a3")
            )

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
    openapi_extra={"x-codeSamples": pyPalworldAPIExamples.boss_pals},
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
    """
    Lookup boss pal info.
    \f
    Parameters
    ----------
    name : str, optional
        Pal name to return information on
    type : str, optional
        Returns Pals of this type
    suitability : str, optional
        Returns Pals with this suitability
    drop : str, optional
        Returns Pals that drop this item
    skill : str, optional
        Returns Pals with this skill
    nocturnal : bool, optional
        Return Pals that are daytime/nocturnal
    page : int, default: 1
        Page number to return
    size: int, default: 50
        Items to return on the page


    .. note:: Need to supply at lest one of the ``name``, ``type``, ``suitability``, ``drop``, ``skill``, ``nocturnal`` parameters.
    
    Returns
    -------
    json
        ::

        {
          "items": [
            {
              "ID": 0,
              "DexKey": "string",
              "Image": "string",
              "Name": "string",
              "Wiki": "string",
              "WikiImage": "string",
              "Types": [
                {
                  "Name": "string",
                  "Image": "string"
                }
              ],
              "Suitability": [
                {
                  "Name": "string",
                  "Image": "string",
                  "Level": 0
                }
              ],
              "Drops": [
                {
                  "Name": "string",
                  "Rate": 0,
                  "Min": 0,
                  "Max": 0
                }
              ],
              "Aura": {
                "Name": "string",
                "Description": "string",
                "Image": "string",
                "Tech": "string"
              },
              "Description": "string",
              "Skills": [
                {
                  "Name": "string",
                  "Type": "string",
                  "Description": "string",
                  "Level": 0,
                  "Cooldown": 0,
                  "Power": 0
                }
              ],
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
              "Asset": "string",
              "Genus": "string",
              "Rarity": 0,
              "Price": 0,
              "Size": "string",
              "BattleBGM": "string",
              "Maps": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string"
              },
              "AIResponse": "string",
              "Nocturnal": true,
              "Predator": true,
              "NooseTrap": true,
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
            'http://127.0.0.0/bosspals/?name=Mammorest&page=1&size=50' \ 
            -H 'Accept: application/json' \ 
            -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'

    Python::

        import asyncio
        import json

        import aiohttp
        from aiohttp.client_exceptions import ClientConnectorError


        async def get_bosspals(name: str, access_token: str):
            url = "http://127.0.0.0/bosspals/"
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
                get_bosspals(name="Mammorest", access_token="kajfe0983qjaf309ajj3w8j3aij3a3")
            )

    """
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
    openapi_extra={"x-codeSamples": pyPalworldAPIExamples.breeding},
)
async def getbreeding(
    name: str,
    db: AsyncSession = Depends(get_session),
):
    """
    Look up breeding pair to get pal your looking for.
    \f
    Parameters
    ----------
    name : str, optional
        Pal name you want to get from breeding
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
              "Egg": "string",
              "P1": "string",
              "P2": "string"
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
            'http://127.0.0.0/breeding/?name=Anubis&page=1&size=50' \ 
            -H 'Accept: application/json' \ 
            -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'

    Python::

        import asyncio
        import json

        import aiohttp
        from aiohttp.client_exceptions import ClientConnectorError


        async def get_breeding(name: str, access_token: str):
            url = "http://127.0.0.0/breeding/"
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
                get_breeding(name="Anubis", access_token="kajfe0983qjaf309ajj3w8j3aij3a3")
            )

    """
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
    openapi_extra={"x-codeSamples": pyPalworldAPIExamples.sickness},
)
async def getsickness(
    name: str,
    db: AsyncSession = Depends(get_session),
):
    """
    Look up sickness effects.
    \f
    Parameters
    ----------
    name : str, optional
        Sickness you want to get effects for
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
              "EffectiveItemRank": 0,
              "WorkSpeed": 0,
              "MoveSpeed": 0,
              "SatietyDecrease": 0,
              "Description": "string",
              "RecoveryProbabilityPercentageInPalBox": 0
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
            'http://127.0.0.0/sickness/?name=ulcer&page=1&size=50' \ 
            -H 'Accept: application/json' \ 
            -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'

    Python::

        import asyncio
        import json

        import aiohttp
        from aiohttp.client_exceptions import ClientConnectorError


        async def get_sickness(name: str, access_token: str):
            url = "http://127.0.0.0/sickness/"
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
                get_sickness(name="ulcer", access_token="kajfe0983qjaf309ajj3w8j3aij3a3")
            )

    """
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
    openapi_extra={"x-codeSamples": pyPalworldAPIExamples.passive},
)
async def getpassive(
    name: str | None = None,
    db: AsyncSession = Depends(get_session),
):
    """
    Look up passive skill effects.
    \f
    Parameters
    ----------
    name : str, optional
        Passive skill you want to get effects for
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
              "Ability": "string",
              "Tier": 0,
              "Description": "string",
              "Image": "string"
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
            'http://127.0.0.0/passive/?name=Brave&page=1&size=50' \ 
            -H 'Accept: application/json' \ 
            -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'

    Python::

        import asyncio
        import json
        
        import aiohttp
        from aiohttp.client_exceptions import ClientConnectorError
        
        
        async def get_passive(name: str, access_token: str):
            url = "http://127.0.0.0/passive/"
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
                get_passive(name="Brave", access_token="kajfe0983qjaf309ajj3w8j3aij3a3")
            )

    """
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
