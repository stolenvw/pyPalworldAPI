"""Create and configure the Palworld API application."""

import os
import tomllib
from contextlib import asynccontextmanager
from pathlib import Path

import sqlalchemy as sa
from dotenv import load_dotenv
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi_pagination import add_pagination
from sqlmodel.ext.asyncio.session import AsyncSession

from pyPalworldAPI.models import auth_models, models
from pyPalworldAPI.routers import admin, autocomplete, items, misc, oauth2, pals, user
from pyPalworldAPI.utils import auth as auth_utils
from pyPalworldAPI.utils import descriptions
from pyPalworldAPI.utils.customexception import APIError
from pyPalworldAPI.utils.database import auth_engine, auth_table, engine

load_dotenv(dotenv_path=".env")


def _get_project_version() -> str:
    pyproject_path = Path(__file__).resolve().parents[1] / "pyproject.toml"
    with pyproject_path.open("rb") as pyproject_file:
        pyproject = tomllib.load(pyproject_file)
    return pyproject["project"]["version"]


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application startup and shutdown resources."""
    if os.getenv("COMPOSE_PROFILES") == "USE_OAUTH2":
        if not sa.inspect(auth_table).has_table("user"):
            auth_models.User.__table__.create(auth_table)
            async with AsyncSession(auth_engine) as auth_session:
                hashed_password = await auth_utils.get_password_hash("pyPalworldAPI")
                new_user = auth_models.User(
                    username=os.getenv("ADMIN_NAME"),
                    password=hashed_password,
                    scopes=["APIAdmin:Write", "APIUser:Read", "APIUser:ChangePassword"],
                    disabled=False,
                )
                auth_session.add(new_user)
                await auth_session.commit()
        if not sa.inspect(auth_table).has_table("refreshtoken"):
            auth_models.RefreshToken.__table__.create(auth_table)
        if not sa.inspect(auth_table).has_table("token"):
            auth_models.Token.__table__.create(auth_table)
        auth_table.dispose()
    yield
    if os.getenv("COMPOSE_PROFILES") == "USE_OAUTH2":
        await auth_engine.dispose()
    await engine.dispose()


app = FastAPI(
    title="Palworld API",
    description=descriptions.description,
    version=_get_project_version(),
    contact={
        "name": "pyPalworldAPI GitHub",
        "url": "https://github.com/stolenvw/pyPalworldAPI",
    },
    license_info={
        "name": "MIT license",
        "identifier": "MIT",
    },
    openapi_tags=(
        descriptions.tags_metadata
        if os.getenv("COMPOSE_PROFILES") != "USE_OAUTH2"
        else descriptions.oauth_tags_metadata
    ),
    swagger_ui_parameters={
        "defaultModelsExpandDepth": -1,
        "persistAuthorization": True,
        "showExtensions": False,
    },
    docs_url=os.getenv("DOCS_URL"),
    redoc_url=os.getenv("REDOC_URL"),
    lifespan=lifespan,
)

add_pagination(app)


@app.exception_handler(APIError)
async def api_exception_handler(request: Request, exc: APIError):
    """Convert API exceptions into JSON responses."""
    return JSONResponse(status_code=exc.status_code, content=exc.content, headers=exc.headers)


if os.getenv("COMPOSE_PROFILES") == "USE_OAUTH2":
    app.include_router(user.router)
    app.include_router(admin.router)
    app.include_router(oauth2.router)

app.include_router(autocomplete.router)
app.include_router(items.router)
app.include_router(misc.router)
app.include_router(pals.router)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
app.mount("/public", StaticFiles(directory=os.path.join(SCRIPT_DIR, "public")), name="public")


@app.get(
    "/health",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=models.HealthCheck,
    include_in_schema=False,
)
async def get_health() -> models.HealthCheck:
    """Return the API health-check status."""
    return models.HealthCheck(status="OK")
