import os

import models.models as M
from fastapi import APIRouter, Depends, Security, status
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
    db: AsyncSession = Depends(get_session),
):
    item = await Q.get_autocomplete(db, category.value, name)
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
