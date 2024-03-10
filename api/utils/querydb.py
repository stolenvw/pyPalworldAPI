from fastapi_pagination.ext.sqlmodel import paginate
from sqlalchemy.sql.expression import text
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from models.models import (
    BossPals,
    Breeding,
    BuidObjects,
    Crafting,
    FoodEffect,
    Gear,
    Items,
    Pals,
    SickPal,
    TechTree,
    PassiveSkills,
    NPC,
)


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


async def get_bosspal(db: AsyncSession, name: str):
    return await paginate(db, select(BossPals).where(BossPals.Name == name))


async def get_pal_by_dexid(db: AsyncSession, idx: str):
    return await paginate(db, select(Pals).where(Pals.DexKey == idx))


async def get_pal_by_type(db: AsyncSession, name: str):
    statement = select(Pals).where(
        text("JSON_SEARCH(Types, 'one', :name COLLATE utf8mb4_general_ci)").bindparams(
            name=name
        )
    )
    return await paginate(db, statement)


async def get_bosspal_by_type(db: AsyncSession, name: str):
    statement = select(BossPals).where(
        text("JSON_SEARCH(Types, 'one', :name COLLATE utf8mb4_general_ci)").bindparams(
            name=name
        )
    )
    return await paginate(db, statement)


async def get_pal_by_suitability(db: AsyncSession, name: str):
    statement = select(Pals).where(
        text(
            "JSON_SEARCH(Suitability, 'one', :name COLLATE utf8mb4_general_ci)"
        ).bindparams(name=name)
    )
    return await paginate(db, statement)


async def get_bosspal_by_suitability(db: AsyncSession, name: str):
    statement = select(BossPals).where(
        text(
            "JSON_SEARCH(Suitability, 'one', :name COLLATE utf8mb4_general_ci)"
        ).bindparams(name=name)
    )
    return await paginate(db, statement)


async def get_pal_by_drops(db: AsyncSession, drop: str):
    statement = select(Pals).where(
        text(f"JSON_SEARCH(Drops, 'one', :name COLLATE utf8mb4_general_ci)").bindparams(
            name=drop
        )
    )
    return await paginate(db, statement)


async def get_pal_by_skills(db: AsyncSession, skill: str):
    statement = select(Pals).where(
        text("JSON_SEARCH(Skills, 'one', :name COLLATE utf8mb4_general_ci)").bindparams(
            name=skill
        )
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


async def get_build(db: AsyncSession, name: str):
    return await paginate(db, select(BuidObjects).where(BuidObjects.Name == name))


async def get_build_by_category(db: AsyncSession, category: str):
    return await paginate(
        db, select(BuidObjects).where(BuidObjects.Category == category)
    )

async def get_passive(db: AsyncSession, name: str):
    return await paginate(db, select(PassiveSkills).where(PassiveSkills.Name == name))

async def get_npc(db: AsyncSession, name: str):
    return await paginate(db, select(NPC).where(NPC.Name == name))

async def get_all(db: AsyncSession, name):
    if name == "pals":
        return await paginate(db, select(Pals))
    elif name == "bosspals":
        return await paginate(db, select(BossPals))
    elif name == "items":
        return await paginate(db, select(Items))
    elif name == "breeding":
        return await paginate(db, select(Breeding))
    elif name == "buidobjects":
        return await paginate(db, select(BuidObjects))
    elif name == "crafting":
        return await paginate(db, select(Crafting))
    elif name == "foodeffect":
        return await paginate(db, select(FoodEffect))
    elif name == "gear":
        return await paginate(db, select(Gear))
    elif name == "sickpal":
        return await paginate(db, select(SickPal))
    elif name == "techtree":
        return await paginate(db, select(TechTree))
    elif name == "passiveskills":
        return await paginate(db, select(PassiveSkills))
    elif name == "npc":
        return await paginate(db, select(NPC))
    return