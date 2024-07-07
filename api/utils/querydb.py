from fastapi_pagination.ext.sqlmodel import paginate
from sqlalchemy.sql.expression import text
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from models.models import (
    NPC,
    BossPals,
    Breeding,
    BuidObjects,
    Crafting,
    Elixir,
    FoodEffect,
    Gear,
    Items,
    Pals,
    PassiveSkills,
    SickPal,
    TechTree,
)


async def get_pals(db: AsyncSession, params):
    palstocolume = {
        "name": Pals.Name,
        "dexkey": Pals.DexKey,
        "nocturnal": Pals.Nocturnal,
    }
    wheres = select(Pals)
    for parm in params:
        if parm == "size" or parm == "page":
            continue
        if parm == "nocturnal":
            if params[parm] == "True":
                p = 1
            else:
                p = 0
        else:
            p = params[parm]
        if parm == "type":
            wheres = wheres.where(
                text(
                    "JSON_SEARCH(Types, 'one', :name COLLATE utf8mb4_general_ci)"
                ).bindparams(name=p)
            )
        elif parm == "suitability":
            wheres = wheres.where(
                text(
                    "JSON_SEARCH(Suitability, 'one', :suit COLLATE utf8mb4_general_ci)"
                ).bindparams(suit=p)
            )
        elif parm == "drop":
            wheres = wheres.where(
                text(
                    f"JSON_SEARCH(Drops, 'one', :drop COLLATE utf8mb4_general_ci)"
                ).bindparams(drop=p)
            )
        elif parm == "skill":
            wheres = wheres.where(
                text(
                    "JSON_SEARCH(Skills, 'one', :skill COLLATE utf8mb4_general_ci)"
                ).bindparams(skill=p)
            )
        else:
            wheres = wheres.where(palstocolume[parm] == p)
    return await paginate(db, wheres)


async def get_bosspal(db: AsyncSession, params):
    palstocolume = {
        "name": BossPals.Name,
        "nocturnal": BossPals.Nocturnal,
    }
    wheres = select(BossPals)
    for parm in params:
        if parm == "size" or parm == "page":
            continue
        if parm == "nocturnal":
            if params[parm] == "True":
                p = 1
            else:
                p = 0
        else:
            p = params[parm]
        if parm == "type":
            wheres = wheres.where(
                text(
                    "JSON_SEARCH(Types, 'one', :name COLLATE utf8mb4_general_ci)"
                ).bindparams(name=p)
            )
        elif parm == "suitability":
            wheres = wheres.where(
                text(
                    "JSON_SEARCH(Suitability, 'one', :suit COLLATE utf8mb4_general_ci)"
                ).bindparams(suit=p)
            )
        elif parm == "drop":
            wheres = wheres.where(
                text(
                    f"JSON_SEARCH(Drops, 'one', :drop COLLATE utf8mb4_general_ci)"
                ).bindparams(drop=p)
            )
        elif parm == "skill":
            wheres = wheres.where(
                text(
                    "JSON_SEARCH(Skills, 'one', :skill COLLATE utf8mb4_general_ci)"
                ).bindparams(skill=p)
            )
        else:
            wheres = wheres.where(palstocolume[parm] == p)
    return await paginate(db, wheres)


async def get_item(db: AsyncSession, params):
    itemtocolume = {
        "name": Items.Name,
        "type": Items.Type,
    }
    wheres = select(Items)
    for parm in params:
        if parm == "size" or parm == "page":
            continue
        wheres = wheres.where(itemtocolume[parm] == params[parm])
    return await paginate(db, wheres)


async def get_crafting(db: AsyncSession, name: str):
    return await paginate(db, select(Crafting).where(Crafting.Name == name))


async def get_gear(db: AsyncSession, name: str):
    return await paginate(db, select(Gear).where(Gear.Name == name))


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


async def get_elixir(db: AsyncSession, name: str):
    return await paginate(db, select(Elixir).where(Elixir.Name == name))


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
    elif name == "elixir":
        return await paginate(db, select(Elixir))
    return


async def get_autocomplete(db: AsyncSession, category: str, name: str):
    if category == "palname":
        return await paginate(
            db,
            select(Pals.Name)
            .where(Pals.Name.like(f"{name}%"))
            .order_by(Pals.Name.asc())
            .distinct(),
        )
    elif category == "paldexkey":
        return await paginate(
            db,
            select(Pals.DexKey)
            .where(Pals.DexKey.like(f"{name}%"))
            .order_by(Pals.DexKey.asc())
            .distinct(),
        )
    elif category == "bossname":
        return await paginate(
            db,
            select(BossPals.Name)
            .where(BossPals.Name.like(f"{name}%"))
            .order_by(BossPals.Name.asc())
            .distinct(),
        )
    elif category == "sickness":
        return await paginate(
            db,
            select(SickPal.Name)
            .where(SickPal.Name.like(f"{name}%"))
            .order_by(SickPal.Name.asc())
            .distinct(),
        )
    elif category == "passiveskill":
        return await paginate(
            db,
            select(PassiveSkills.Name)
            .where(PassiveSkills.Name.like(f"{name}%"))
            .order_by(PassiveSkills.Name.asc())
            .distinct(),
        )
    elif category == "itemname":
        return await paginate(
            db,
            select(Items.Name)
            .where(Items.Name.like(f"{name}%"))
            .order_by(Items.Name.asc())
            .distinct(),
        )
    elif category == "itemtype":
        return await paginate(
            db,
            select(Items.Type)
            .where(Items.Type.like(f"{name}%"))
            .order_by(Items.Type.asc())
            .distinct(),
        )
    elif category == "crafting":
        return await paginate(
            db,
            select(Crafting.Name)
            .where(Crafting.Name.like(f"{name}%"))
            .order_by(Crafting.Name.asc())
            .distinct(),
        )
    elif category == "gear":
        return await paginate(
            db,
            select(Gear.Name)
            .where(Gear.Name.like(f"{name}%"))
            .order_by(Gear.Name.asc())
            .distinct(),
        )
    elif category == "food":
        return await paginate(
            db,
            select(FoodEffect.Name)
            .where(FoodEffect.Name.like(f"{name}%"))
            .order_by(FoodEffect.Name.asc())
            .distinct(),
        )
    elif category == "tech":
        return await paginate(
            db,
            select(TechTree.Name)
            .where(TechTree.Name.like(f"{name}%"))
            .order_by(TechTree.Name.asc())
            .distinct(),
        )
    elif category == "buidname":
        return await paginate(
            db,
            select(BuidObjects.Name)
            .where(BuidObjects.Name.like(f"{name}%"))
            .order_by(BuidObjects.Name.asc())
            .distinct(),
        )
    elif category == "buildcategory":
        return await paginate(
            db,
            select(BuidObjects.Category)
            .where(BuidObjects.Category.like(f"{name}%"))
            .order_by(BuidObjects.Category.asc())
            .distinct(),
        )
    elif category == "elixir":
        return await paginate(
            db,
            select(Elixir.Name)
            .where(Elixir.Name.like(f"{name}%"))
            .order_by(Elixir.Name.asc())
            .distinct(),
        )
    elif category == "npc":
        return await paginate(
            db,
            select(NPC.Name)
            .where(NPC.Name.like(f"{name}%"))
            .order_by(NPC.Name.asc())
            .distinct(),
        )
    return
