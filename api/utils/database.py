import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine

load_dotenv(dotenv_path=".env")

engine = create_async_engine(
    f'mysql+aiomysql://{os.getenv("MYSQL_USER")}:{os.getenv("MYSQL_PASSWORD")}@{os.getenv("SQL_HOST")}:{int(os.getenv("SQL_PORT"))}/{os.getenv("MYSQL_DATABASE")}',
    echo=False,
)
