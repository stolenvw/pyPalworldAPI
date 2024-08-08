import os
from contextlib import asynccontextmanager

import models.auth_models as AuthModel
import models.models as M
import sqlalchemy as sa
import utils.auth as AuthUtils
import utils.descriptions as D
from dotenv import load_dotenv
from fastapi import FastAPI, status, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi_pagination import add_pagination
from routers import admin, autocomplete, items, misc, oauth2, pals, user
from sqlmodel.ext.asyncio.session import AsyncSession
from utils.database import auth_engine, auth_table, engine
from utils.customexception import APIException

load_dotenv(dotenv_path=".env")


@asynccontextmanager
async def lifespan(app: FastAPI):
    if os.getenv("COMPOSE_PROFILES") == "USE_OAUTH2":
        if not sa.inspect(auth_table).has_table("user"):
            AuthModel.User.__table__.create(auth_table)
            async with AsyncSession(auth_engine) as auth_session:
                hashed_password = await AuthUtils.get_password_hash("pyPalworldAPI")
                new_user = AuthModel.User(
                    username=os.getenv("ADMIN_NAME"),
                    password=hashed_password,
                    scopes=["APIAdmin:Write", "APIUser:Read", "APIUser:ChangePassword"],
                    disabled=False,
                )
                auth_session.add(new_user)
                await auth_session.commit()
        if not sa.inspect(auth_table).has_table("refreshtoken"):
            AuthModel.RefreshToken.__table__.create(auth_table)
        if not sa.inspect(auth_table).has_table("token"):
            AuthModel.Token.__table__.create(auth_table)
        auth_table.dispose()
    yield
    if os.getenv("COMPOSE_PROFILES") == "USE_OAUTH2":
        await auth_engine.dispose()
    await engine.dispose()


app = FastAPI(
    title="Palworld API",
    description=D.description,
    version="0.0.6-alpha",
    contact={
        "name": "pyPalworldAPI GitHub",
        "url": "https://github.com/stolenvw/pyPalworldAPI",
    },
    license_info={
        "name": "MIT license",
        "identifier": "MIT",
    },
    openapi_tags=(
        D.tags_metadata
        if os.getenv("COMPOSE_PROFILES") != "USE_OAUTH2"
        else D.oauth_tags_metadata
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

@app.exception_handler(APIException)
async def api_exception_handler(request: Request, exc: APIException):
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.content,
        headers=exc.headers
    )

if os.getenv("COMPOSE_PROFILES") == "USE_OAUTH2":
    app.include_router(user.router)
    app.include_router(admin.router)
    app.include_router(oauth2.router)

app.include_router(autocomplete.router)
app.include_router(items.router)
app.include_router(misc.router)
app.include_router(pals.router)

app.mount("/public", StaticFiles(directory="public"), name="public")


@app.get(
    "/health",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=M.HealthCheck,
    include_in_schema=False,
)
async def get_health() -> M.HealthCheck:
    return M.HealthCheck(status="OK")
