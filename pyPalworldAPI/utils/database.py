import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import create_engine
from sqlmodel.ext.asyncio.session import AsyncSession

load_dotenv(dotenv_path=".env")

engine = create_async_engine(
    f'mysql+aiomysql://{os.getenv("MYSQL_USER")}:{os.getenv("MYSQL_PASSWORD")}@{os.getenv("SQL_HOST")}:{int(os.getenv("MYSQL_PORT"))}/{os.getenv("MYSQL_DATABASE")}',
    echo=False,
)

auth_engine = create_async_engine(
    f'mysql+aiomysql://{os.getenv("MYSQL_USER")}:{os.getenv("MYSQL_PASSWORD")}@{os.getenv("SQL_USER_HOST")}:{int(os.getenv("MYSQL_PORT"))}/{os.getenv("MYSQL_USER_DATABASE")}',
    echo=False,
)

auth_table = create_engine(
    f'mysql://{os.getenv("MYSQL_USER")}:{os.getenv("MYSQL_PASSWORD")}@{os.getenv("SQL_USER_HOST")}:{int(os.getenv("MYSQL_PORT"))}/{os.getenv("MYSQL_USER_DATABASE")}',
    echo=False,
)


async def get_session():
    async with AsyncSession(engine) as session:
        yield session
