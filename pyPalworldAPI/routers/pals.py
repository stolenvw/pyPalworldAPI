r"""Provide pals helpers."""

import os

from fastapi import APIRouter, Depends, Query, Request, Security, status
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
    tags=["Pals"],
    responses=PalworldAPIErrorResponses.responses_400_401_404,
    dependencies=(
        [Security(get_current_active_user, scopes=["APIUser:Read"])]
        if os.getenv("COMPOSE_PROFILES") == "USE_OAUTH2"
        else None
    ),
)


@router.get(
    "/pals/",
    response_model=Page[models.Pals],
    response_model_exclude_none=True,
    summary="Lookup Pal[s] Information",
    openapi_extra={"x-codeSamples": PalworldAPIExamples.pals},
)
async def getpal(
    request: Request,
    name: str | None = Query(None, description="Pal name."),
    dexkey: str | None = Query(None, description="Paldex number."),
    typename: str | None = Query(None, alias="type"),
    suitability: str | None = None,
    drop: str | None = None,
    skill: str | None = None,
    lang: str = Query("en", description="Localized text language code."),
    nocturnal: bool | None = Query(None, description="False for day Pals, True for night Pals."),
    db: AsyncSession = Depends(get_session),
):
    r"""Lookup pal info.

    \f.

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
    APIError
        HTTP responses with errors.
    RequestValidationError
        When a request contains invalid data.

    Examples
    --------
    Curl::

        curl -X 'GET' \\
            'http://127.0.0.0/pals/?name=lamball&page=1&size=50' \\
            -H 'Accept: application/json' \\
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
    item = await palapi_query.get_pals(db, params, lang=lang)
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
    "/bosspals/",
    response_model=Page[models.BossPals],
    response_model_exclude_none=True,
    summary="Lookup Boss Pal[s] Information",
    openapi_extra={"x-codeSamples": PalworldAPIExamples.boss_pals},
)
async def getbosspal(
    request: Request,
    name: str | None = Query(None, description="Pal name."),
    typename: str | None = Query(None, alias="type"),
    suitability: str | None = None,
    drop: str | None = None,
    skill: str | None = None,
    lang: str = Query("en", description="Localized text language code."),
    nocturnal: bool | None = Query(None, description="False for day Pals, True for night Pals."),
    db: AsyncSession = Depends(get_session),
):
    r"""Lookup boss pal info.

    \f.

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
    APIError
        HTTP responses with errors.
    RequestValidationError
        When a request contains invalid data.

    Examples
    --------
    Curl::

        curl -X 'GET' \\
            'http://127.0.0.0/bosspals/?name=Mammorest&page=1&size=50' \\
            -H 'Accept: application/json' \\
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
    item = await palapi_query.get_bosspal(db, params, lang=lang)
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
    "/breeding/",
    response_model=Page[models.Breeding],
    response_model_exclude_none=True,
    summary="Lookup Breeding Information",
    openapi_extra={"x-codeSamples": PalworldAPIExamples.breeding},
)
async def getbreeding(
    name: str | None = Query(
        None,
        description="Legacy alias for egg. Pal name you want to get from breeding.",
        deprecated=True,
    ),
    egg: str | None = Query(None, description="Egg Pal name to find parent pairs for."),
    p1: str | None = Query(None, description="First parent Pal name."),
    p2: str | None = Query(None, description="Second parent Pal name."),
    lang: str = Query("en", description="Localized text language code."),
    db: AsyncSession = Depends(get_session),
):
    r"""Look up breeding pairs by egg or parent Pal names.

    \f.

    Parameters
    ----------
    name : str, optional
        Deprecated legacy alias for egg. This will be removed in the future; use egg instead
    egg : str, optional
        Pal name you want to get from breeding
    p1 : str, optional
        Parent Pal name
    p2 : str, optional
        Parent Pal name
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
              "EggDexKey": "string",
              "P1": "string",
              "P1DexKey": "string",
              "P2": "string",
              "P2DexKey": "string"
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
            'http://127.0.0.0/breeding/?p1=Lamball&p2=Cattiva&page=1&size=50' \\
            -H 'Accept: application/json' \\
            -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'

    Python::

        import asyncio
        import json

        import aiohttp
        from aiohttp.client_exceptions import ClientConnectorError


        async def get_breeding(p1: str, p2: str, access_token: str):
            url = "http://127.0.0.0/breeding/"
            headers = {
                "Accept": "application/json",
                "Authorization": f"Bearer {access_token}",
            }
            params = {"p1": p1, "p2": p2, "page": 1, "size": 50}
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
                get_breeding(
                    p1="Lamball",
                    p2="Cattiva",
                    access_token="kajfe0983qjaf309ajj3w8j3aij3a3",
                )
            )


    """
    if name or egg or p1 or p2:
        item = await palapi_query.get_breeding(db, name, egg=egg, p1=p1, p2=p2, lang=lang)
    else:
        raise APIError(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Missing one of the (name, egg, p1, p2) params.",
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
    "/sickness/",
    response_model=Page[models.SickPal],
    response_model_exclude_none=True,
    summary="Lookup Sickness Information",
    openapi_extra={"x-codeSamples": PalworldAPIExamples.sickness},
)
async def getsickness(
    name: str,
    lang: str = Query("en", description="Localized text language code."),
    db: AsyncSession = Depends(get_session),
):
    r"""Look up sickness effects.

    \f.

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
    APIError
        HTTP responses with errors.
    RequestValidationError
        When a request contains invalid data.

    Examples
    --------
    Curl::

        curl -X 'GET' \\
            'http://127.0.0.0/sickness/?name=ulcer&page=1&size=50' \\
            -H 'Accept: application/json' \\
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
        item = await palapi_query.get_sickness(db, name, lang=lang)
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
    "/passive/",
    response_model=Page[models.PassiveSkills],
    response_model_exclude_none=True,
    summary="Lookup Passive Skills Information",
    openapi_extra={"x-codeSamples": PalworldAPIExamples.passive},
)
async def getpassive(
    name: str | None = None,
    lang: str = Query("en", description="Localized text language code."),
    db: AsyncSession = Depends(get_session),
):
    r"""Look up passive skill effects.

    \f.

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
    APIError
        HTTP responses with errors.
    RequestValidationError
        When a request contains invalid data.

    Examples
    --------
    Curl::

        curl -X 'GET' \\
            'http://127.0.0.0/passive/?name=Brave&page=1&size=50' \\
            -H 'Accept: application/json' \\
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
        item = await palapi_query.get_passive(db, name, lang=lang)
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
