r"""Provide items helpers."""

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
    tags=["Items"],
    responses=PalworldAPIErrorResponses.responses_400_401_404,
    dependencies=(
        [Security(get_current_active_user, scopes=["APIUser:Read"])]
        if os.getenv("COMPOSE_PROFILES") == "USE_OAUTH2"
        else None
    ),
)


@router.get(
    "/items/",
    response_model=Page[models.Items],
    response_model_exclude_none=True,
    summary="Lookup Items Information",
    openapi_extra={"x-codeSamples": PalworldAPIExamples.items},
)
async def getitems(
    request: Request,
    name: str | None = None,
    variety: str | None = Query(None, alias="type"),
    lang: str = Query("en", description="Localized text language code."),
    db: AsyncSession = Depends(get_session),
):
    r"""Look up items.

    \f.

    Parameters
    ----------
    name : str, optional
        Item thats being looked for
    type: str, optional
        Find items by type
    page : int, default: 1
        Page number to return
    size: int, default: 50
        Items to return on the page


    .. note:: Need to supply one of the ``name`` or ``type`` parameters.

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
              "Image": "string",
              "Type": "string",
              "Rank": 0,
              "MaxStackCount": 0,
              "Weight": 0,
              "Gold": 0,
              "Durability": 0,
              "MagazineSize": 0,
              "PhysicalAttackValue": 0,
              "HPValue": 0,
              "PhysicalDefenseValue": 0,
              "ShieldValue": 0,
              "MagicAttackValue": 0,
              "MagicDefenseValue": 0,
              "Description": "string",
              "ItemActorClass": "string",
              "PassiveSkills": {
                "PassiveSkill1": "string",
                "PassiveSkill2": "string",
                "PassiveSkill3": "string",
                "PassiveSkill4": "string"
              }
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
            'http://127.0.0.0/items/?name=arrow&page=1&size=50' \\
            -H 'Accept: application/json' \\
            -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'

    Python::

        import asyncio
        import json

        import aiohttp
        from aiohttp.client_exceptions import ClientConnectorError


        async def get_items(name: str, access_token: str):
            url = "http://127.0.0.0/items/"
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
            asyncio.run(get_items(name="arrow", access_token="kajfe0983qjaf309ajj3w8j3aij3a3"))


    """
    params = request.query_params
    item = await palapi_query.get_item(db, params, lang=lang)
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
    "/crafting/",
    response_model=Page[models.Crafting],
    response_model_exclude_none=True,
    summary="Lookup Crafting Information",
    openapi_extra={"x-codeSamples": PalworldAPIExamples.crafting},
)
async def getcrafting(
    name: str = Query(None, description="Item you want to make."),
    lang: str = Query("en", description="Localized text language code."),
    db: AsyncSession = Depends(get_session),
):
    r"""Look up materials to craft item.

    \f.

    Parameters
    ----------
    name : str
        Item you want to make
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
              "Output": 0,
              "WorkAmount": 0,
              "Material": {
                "additionalProp1": 0,
                "additionalProp2": 0,
                "additionalProp3": 0
              }
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
            'http://127.0.0.0/crafting/?name=arrow&page=1&size=50' \\
            -H 'Accept: application/json' \\
            -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'

    Python::

        import asyncio
        import json

        import aiohttp
        from aiohttp.client_exceptions import ClientConnectorError


        async def get_crafting(name: str, access_token: str):
            url = "http://127.0.0.0/crafting/"
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
                get_crafting(name="arrow", access_token="kajfe0983qjaf309ajj3w8j3aij3a3")
            )


    """
    if name:
        item = await palapi_query.get_crafting(db, name, lang=lang)
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
    "/gear/",
    response_model=Page[models.Gear],
    response_model_exclude_none=True,
    summary="Lookup Gear Information",
    openapi_extra={"x-codeSamples": PalworldAPIExamples.gear},
)
async def getgear(
    name: str,
    lang: str = Query("en", description="Localized text language code."),
    db: AsyncSession = Depends(get_session),
):
    r"""Look gear stats.

    \f.

    Parameters
    ----------
    name : str
        Gear you want to get stats for
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
              "Common": {
                "additionalProp1": 0,
                "additionalProp2": 0,
                "additionalProp3": 0
              },
              "Uncommon": {
                "additionalProp1": 0,
                "additionalProp2": 0,
                "additionalProp3": 0
              },
              "Rare": {
                "additionalProp1": 0,
                "additionalProp2": 0,
                "additionalProp3": 0
              },
              "Epic": {
                "additionalProp1": 0,
                "additionalProp2": 0,
                "additionalProp3": 0
              },
              "Legendary": {
                "additionalProp1": 0,
                "additionalProp2": 0,
                "additionalProp3": 0
              }
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
            'http://127.0.0.0/gear/?name=cloth%20outfit&page=1&size=50' \\
            -H 'Accept: application/json' \\
            -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'

    Python::

        import asyncio
        import json

        import aiohttp
        from aiohttp.client_exceptions import ClientConnectorError


        async def get_gear(name: str, access_token: str):
            url = "http://127.0.0.0/gear/"
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
                get_gear(name="cloth outfit", access_token="kajfe0983qjaf309ajj3w8j3aij3a3")
            )


    """
    if name:
        item = await palapi_query.get_gear(db, name, lang=lang)
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
    "/foodeffect/",
    response_model=Page[models.FoodEffect],
    response_model_exclude_none=True,
    summary="Lookup Food Effects Information",
    openapi_extra={"x-codeSamples": PalworldAPIExamples.foodeffect},
)
async def getfoodeffect(
    name: str,
    lang: str = Query("en", description="Localized text language code."),
    db: AsyncSession = Depends(get_session),
):
    r"""Lookup effect for food.

    \f.

    Parameters
    ----------
    name : str
        Food you want to get effect info for
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
              "EffectTime": 0,
              "Effects": [
                {
                  "Name": "string",
                  "Value": 0,
                  "Interaval": 0
                }
              ]
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
            'http://127.0.0.0/foodeffect/?name=salad&page=1&size=50' \\
            -H 'Accept: application/json' \\
            -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'

    Python::

        import asyncio
        import json

        import aiohttp
        from aiohttp.client_exceptions import ClientConnectorError


        async def get_foodeffect(name: str, access_token: str):
            url = "http://127.0.0.0/foodeffect/"
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
                get_foodeffect(name="salad", access_token="kajfe0983qjaf309ajj3w8j3aij3a3")
            )


    """
    if name:
        item = await palapi_query.get_foodeffects(db, name, lang=lang)
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
    "/tech/",
    response_model=Page[models.TechTree],
    response_model_exclude_none=True,
    summary="Lookup Tech Tree Information",
    openapi_extra={"x-codeSamples": PalworldAPIExamples.tech},
)
async def gettech(
    name: str | None = None,
    level: int | None = Query(None, ge=1, le=80),
    lang: str = Query("en", description="Localized text language code."),
    db: AsyncSession = Depends(get_session),
):
    r"""Lookup level and cost to unlock tech tree item.

    \f.

    Parameters
    ----------
    name : str, optional
        Get tech tree info for item
    level : str, optional
        Get tech tree items for given level
    page : int, default: 1
        Page number to return
    size: int, default: 50
        Items to return on the page


    .. note:: Need to supply one of the ``name`` or ``level`` parameters.

    Returns
    -------
    json
        ::

        {
          "items": [
            {
              "ID": 0,
              "Name": "string",
              "UnlockBuildObjects": [
                "string"
              ],
              "UnlockItemRecipes": [
                "string"
              ],
              "Description": "string",
              "Image": "string",
              "RequireTechnology": "string",
              "IsBossTechnology": true,
              "LevelCap": 0,
              "Cost": 0
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
            'http://127.0.0.0/tech/?name=Nail&page=1&size=50' \\
            -H 'Accept: application/json' \\
            -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'

    Python::

        import asyncio
        import json

        import aiohttp
        from aiohttp.client_exceptions import ClientConnectorError


        async def get_tech(name: str, access_token: str):
            url = "http://127.0.0.0/tech/"
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
            asyncio.run(get_tech(name="Nail", access_token="kajfe0983qjaf309ajj3w8j3aij3a3"))


    """
    if name:
        item = await palapi_query.get_tech(db, name, lang=lang)
    elif level:
        item = await palapi_query.get_tech_by_level(db, level, lang=lang)
    else:
        raise APIError(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Missing one of the (name, level) params.",
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
    "/build/",
    response_model=Page[models.BuildObjects],
    response_model_exclude_none=True,
    summary="Lookup Build Objects Information",
    openapi_extra={"x-codeSamples": PalworldAPIExamples.build},
)
async def getbuild(
    name: str | None = None,
    category: str | None = None,
    lang: str = Query("en", description="Localized text language code."),
    db: AsyncSession = Depends(get_session),
):
    r"""Lookup material needed to build item.

    \f.

    Parameters
    ----------
    name : str, optional
        Build item
    category : str, optional
        Build category
    page : int, default: 1
        Page number to return
    size: int, default: 50
        Items to return on the page


    .. note:: Need to supply one of the ``name`` or ``category`` parameters.

    Returns
    -------
    json
        ::

        {
          "items": [
            {
              "ID": 0,
              "MapObjectId": "string",
              "Name": "string",
              "Description": "string",
              "Image": "string",
              "Material": [
                {
                  "Name": "string",
                  "Amount": 0
                }
              ],
              "Category": "string",
              "RequiredBuildWorkAmount": 0,
              "InstallNeighborThreshold": 0,
              "IsInstallOnlyOnBase": true,
              "IsInstallOnlyHubAround": true
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
            'http://127.0.0.0/build/?name=Campfire&page=1&size=50' \\
            -H 'Accept: application/json' \\
            -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'

    Python::

        import asyncio
        import json

        import aiohttp
        from aiohttp.client_exceptions import ClientConnectorError


        async def get_build(name: str, access_token: str):
            url = "http://127.0.0.0/build/"
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
                get_build(name="Campfire", access_token="kajfe0983qjaf309ajj3w8j3aij3a3")
            )


    """
    if name:
        item = await palapi_query.get_build(db, name, lang=lang)
    elif category:
        item = await palapi_query.get_build_by_category(db, category, lang=lang)
    else:
        raise APIError(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Missing one of the (name, category) params.",
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
    "/elixir/",
    response_model=Page[models.Elixir],
    response_model_exclude_none=True,
    summary="Lookup Elixir Information",
    openapi_extra={"x-codeSamples": PalworldAPIExamples.elixir},
)
async def getelixir(
    name: str | None = None,
    lang: str = Query("en", description="Localized text language code."),
    db: AsyncSession = Depends(get_session),
):
    r"""Lookup elixir status.

    \f.

    Parameters
    ----------
    name : str
        Elixir to get stats for
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
              "Description": "string",
              "DevName": "string",
              "MaxHP": 0,
              "MaxSP": 0,
              "Power": 0,
              "WorkSpeed": 0,
              "maxInventoryWeight": 0
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
            'http://127.0.0.0/elixir/?name=Speed%20Elixir&page=1&size=50' \\
            -H 'Accept: application/json' \\
            -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'

    Python::

        import asyncio
        import json

        import aiohttp
        from aiohttp.client_exceptions import ClientConnectorError


        async def get_elixir(name: str, access_token: str):
            url = "http://127.0.0.0/elixir/"
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
                get_elixir(
                    name="Speed Elixir", access_token="kajfe0983qjaf309ajj3w8j3aij3a3"
                )
            )


    """
    if name:
        item = await palapi_query.get_elixir(db, name, lang=lang)
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
