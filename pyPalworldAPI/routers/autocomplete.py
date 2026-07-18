import os

import models.models as M
from fastapi import APIRouter, Depends, Query, Security, status
from query import palapi as Q
from sqlmodel.ext.asyncio.session import AsyncSession
from utils.auth import get_current_active_user
from utils.autocustompage import AutoCompletePage
from utils.customexception import APIException
from utils.customresponses import pyPalworldAPIErrorResponses
from utils.database import get_session
from utils.examples import pyPalworldAPIExamples

router = APIRouter(
    prefix="/autocomplete",
    tags=["AutoComplete"],
    dependencies=(
        [Security(get_current_active_user, scopes=["APIUser:Read"])]
        if os.getenv("COMPOSE_PROFILES") == "USE_OAUTH2"
        else None
    ),
    responses=pyPalworldAPIErrorResponses.response_401_404,
)


@router.get(
    "/{category}/",
    response_model=AutoCompletePage[str],
    response_model_exclude_none=True,
    summary="AutoComplete Helper",
    openapi_extra={"x-codeSamples": pyPalworldAPIExamples.autocomplete},
)
async def getautocomplete(
    category: M.AutoCompleteModels,
    name: str | None = "%",
    lang: str = Query("en", description="Localized text language code."),
    db: AsyncSession = Depends(get_session),
):
    """
    Helper for discord bots autocomplete.
    \f
    Parameters
    ----------
    category: str
        Category to search in
    name : str
        Start of item thats being looked for
    page : int, default: 1
        Page number to return
    size: int, default: 25
        Items to return on the page
    
    Returns
    -------
    json
        ::

        {
          "items": [
            "Lamball"
          ],
          "total": 1,
          "page": 1,
          "size": 25,
          "pages": 1
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
            'http://127.0.0.0/autocomplete/palname/?name=la&page=1&size=50' \ 
            -H 'Accept: application/json' \ 
            -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'

    Python::

        import asyncio
        import json
        
        import aiohttp
        from aiohttp.client_exceptions import ClientConnectorError
        
        
        async def get_autocomplete(category: str, name: str, access_token: str):
            url = f"http://127.0.0.0/autocomplete/{category}"
            headers = {
                "Accept": "application/json",
                "Authorization": f"Bearer {access_token}",
            }
            params = {"name": name, "page": 1, "size": 25}
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
                get_autocomplete(
                    category="palname", name="la", access_token="kajfe0983qjaf309ajj3w8j3aij3a3"
                )
            )

    """
    item = await Q.get_autocomplete(db, category.value, name, lang=lang)
    if item is not None and len(item.items) != 0:
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
