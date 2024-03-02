from fastapi_pagination.ext.sqlmodel import paginate
from sqlalchemy.sql.expression import text
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from models.models import Breeding, Crafting, FoodEffect, Gear, Items, Pals, SickPal, TechTree


async def get_item(db: AsyncSession, name: str, variety: str):
    if name:
        return await paginate(db, select(Items).where(Items.Name == name))
    if variety:
        return await paginate(db, select(Items).where(Items.Type == variety))


async def get_crafting(db: AsyncSession, name: str):
    return await paginate(db, select(Crafting).where(Crafting.Name == name))


async def get_gear(db: AsyncSession, name: str):
    return await paginate(db, select(Gear).where(Gear.Name == name))


async def get_pal(db: AsyncSession, name: str):
    return await paginate(db, select(Pals).where(Pals.Name == name))


async def get_pal_by_dexid(db: AsyncSession, idx: str):
    return await paginate(db, select(Pals).where(Pals.DexKey == idx))


async def get_pal_by_type(db: AsyncSession, name: str):
    statement = select(Pals).where(
        text("JSON_SEARCH(Types, 'one', :name)").bindparams(name=name)
    )
    return await paginate(db, statement)


async def get_pal_by_suitability(db: AsyncSession, name: str):
    statement = select(Pals).where(
        text("JSON_SEARCH(Suitability, 'one', :name)").bindparams(name=name)
    )
    return await paginate(db, statement)


async def get_pal_by_drops(db: AsyncSession, drop: str):
    statement = select(Pals).where(
        text(f"JSON_SEARCH(Drops, 'one', :name)").bindparams(name=drop)
    )
    return await paginate(db, statement)


async def get_pal_by_skills(db: AsyncSession, skill: str):
    statement = select(Pals).where(
        text("JSON_SEARCH(Skills, 'one', :name)").bindparams(name=skill)
    )
    return await paginate(db, statement)


async def get_pal_by_nocturnal(db: AsyncSession, nocturnal: str):
    statement = select(Pals).where(Pals.Nocturnal == nocturnal)
    return await paginate(db, statement)


async def get_foodeffects(db: AsyncSession, name: str):
    return await paginate(db, select(FoodEffect).where(FoodEffect.Name == name))


async def get_breeding(db: AsyncSession, name: str):
    return await paginate(db, select(Breeding).where(Breeding.Egg == name))


async def get_sickness(db: AsyncSession, name: str):
    return await paginate(db, select(SickPal).where(SickPal.Name == name))

async def get_tech(db: AsyncSession, name: str):
    return await paginate(db, select(TechTree).where(TechTree.Name == name))

async def get_tech_by_level(db: AsyncSession, level: int):
    return await paginate(db, select(TechTree).where(TechTree.LevelCap == level))
