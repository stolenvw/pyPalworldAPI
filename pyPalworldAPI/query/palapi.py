from fastapi_pagination.ext.sqlmodel import paginate
from models.models import (
    NPC,
    NPCI18n,
    BossPals,
    BossPalsI18n,
    Breeding,
    BreedingRecord,
    BuildObjects,
    BuildObjectsI18n,
    Crafting,
    CraftingI18n,
    Elixir,
    ElixirI18n,
    FoodEffect,
    FoodEffectI18n,
    Gear,
    GearI18n,
    Items,
    ItemsI18n,
    Pals,
    PalsI18n,
    PassiveSkills,
    SickPal,
    SickPalI18n,
    TechTree,
    TechTreeI18n,
)
from sqlalchemy import and_, bindparam, column as sql_column, func, literal_column, true
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession


LOCALIZATION_CONFIG = {
    "pals": (PalsI18n, "PalsID", ("Name", "Types", "Suitability", "Drops", "Aura", "Description", "Skills", "FirstDefeatRewardItemID")),
    "bosspals": (BossPalsI18n, "BossPalsID", ("Name", "Types", "Suitability", "Drops", "Aura", "Description", "Skills", "FirstDefeatRewardItemID")),
    "items": (ItemsI18n, "ItemID", ("Name", "Description", "PassiveSkills")),
    "buildobjects": (BuildObjectsI18n, "BuildObjectsID", ("Name", "Description", "Material", "Category")),
    "crafting": (CraftingI18n, "CraftingID", ("Name", "Material")),
    "foodeffect": (FoodEffectI18n, "FoodEffectID", ("Name",)),
    "gear": (GearI18n, "GearID", ("Name",)),
    "sickpal": (SickPalI18n, "SickPalID", ("Name", "Description")),
    "techtree": (TechTreeI18n, "TechTreeID", ("Name", "UnlockBuildObjects", "UnlockItemRecipes", "Description", "RequireTechnology")),
    "npc": (NPCI18n, "NPCID", ("Name", "Weapon", "Suitability")),
    "elixir": (ElixirI18n, "ElixirID", ("Name", "Description")),
}


def _json_search(column, bind_name: str, value: str):
    return func.JSON_SEARCH(
        column,
        "one",
        bindparam(bind_name, value).collate("utf8mb4_general_ci"),
    ).is_not(None)


async def _apply_localization(db: AsyncSession, page, category: str, lang: str):
    if lang == "en" or category not in LOCALIZATION_CONFIG or len(page.items) == 0:
        return page

    i18n_model, parent_field, fields = LOCALIZATION_CONFIG[category]
    item_ids = [item.ID for item in page.items if getattr(item, "ID", None) is not None]
    if not item_ids:
        return page

    statement = select(i18n_model).where(
        getattr(i18n_model, parent_field).in_(item_ids),
        i18n_model.LanguageCode == lang,
    )
    localizations = {
        getattr(row, parent_field): row for row in (await db.exec(statement)).all()
    }
    for item in page.items:
        row = localizations.get(item.ID)
        if row is None:
            continue
        for field in fields:
            value = getattr(row, field)
            if value is not None:
                setattr(item, field, value)
    return page


def _localized_join(statement, base_model, i18n_model, parent_field: str, lang: str):
    return statement.join(
        i18n_model,
        and_(
            getattr(i18n_model, parent_field) == base_model.ID,
            i18n_model.LanguageCode == lang,
        ),
    )


async def _paginate_with_localization(
    db: AsyncSession,
    statement,
    category: str,
    lang: str,
):
    page = await paginate(db, statement)
    return await _apply_localization(db, page, category, lang)


async def get_pals(db: AsyncSession, params, lang: str = "en"):
    localized = lang != "en"
    wheres = select(Pals)
    if localized:
        wheres = _localized_join(wheres, Pals, PalsI18n, "PalsID", lang)
    for parm in params:
        if parm in {"size", "page", "lang"}:
            continue
        if parm == "nocturnal":
            value = params[parm] == "True"
            wheres = wheres.where(Pals.Nocturnal == value)
        elif parm == "name":
            wheres = wheres.where((PalsI18n.Name if localized else Pals.Name) == params[parm])
        elif parm == "dexkey":
            wheres = wheres.where(Pals.DexKey == params[parm])
        elif parm == "type":
            wheres = wheres.where(
                _json_search(PalsI18n.Types if localized else Pals.Types, "type_name", params[parm])
            )
        elif parm == "suitability":
            wheres = wheres.where(
                _json_search(
                    PalsI18n.Suitability if localized else Pals.Suitability,
                    "suitability_name",
                    params[parm],
                )
            )
        elif parm == "drop":
            wheres = wheres.where(
                _json_search(PalsI18n.Drops if localized else Pals.Drops, "drop_name", params[parm])
            )
        elif parm == "skill":
            wheres = wheres.where(
                _json_search(PalsI18n.Skills if localized else Pals.Skills, "skill_name", params[parm])
            )
    return await _paginate_with_localization(db, wheres, "pals", lang)


async def get_bosspal(db: AsyncSession, params, lang: str = "en"):
    localized = lang != "en"
    wheres = select(BossPals)
    if localized:
        wheres = _localized_join(wheres, BossPals, BossPalsI18n, "BossPalsID", lang)
    for parm in params:
        if parm in {"size", "page", "lang"}:
            continue
        if parm == "nocturnal":
            value = params[parm] == "True"
            wheres = wheres.where(BossPals.Nocturnal == value)
        elif parm == "name":
            wheres = wheres.where(
                (BossPalsI18n.Name if localized else BossPals.Name) == params[parm]
            )
        elif parm == "type":
            wheres = wheres.where(
                _json_search(
                    BossPalsI18n.Types if localized else BossPals.Types,
                    "boss_type_name",
                    params[parm],
                )
            )
        elif parm == "suitability":
            wheres = wheres.where(
                _json_search(
                    BossPalsI18n.Suitability if localized else BossPals.Suitability,
                    "boss_suitability_name",
                    params[parm],
                )
            )
        elif parm == "drop":
            wheres = wheres.where(
                _json_search(
                    BossPalsI18n.Drops if localized else BossPals.Drops,
                    "boss_drop_name",
                    params[parm],
                )
            )
        elif parm == "skill":
            wheres = wheres.where(
                _json_search(
                    BossPalsI18n.Skills if localized else BossPals.Skills,
                    "boss_skill_name",
                    params[parm],
                )
            )
    return await _paginate_with_localization(db, wheres, "bosspals", lang)


async def get_item(db: AsyncSession, params, lang: str = "en"):
    localized = lang != "en"
    wheres = select(Items)
    if localized:
        wheres = _localized_join(wheres, Items, ItemsI18n, "ItemID", lang)
    for parm in params:
        if parm in {"size", "page", "lang"}:
            continue
        if parm == "name":
            wheres = wheres.where((ItemsI18n.Name if localized else Items.Name) == params[parm])
        elif parm == "type":
            wheres = wheres.where(Items.Type == params[parm])
    return await _paginate_with_localization(db, wheres, "items", lang)


async def _get_by_name(db: AsyncSession, *, base_model, i18n_model, parent_field: str, category: str, field_name: str, name: str, lang: str):
    wheres = select(base_model)
    if lang != "en":
        wheres = _localized_join(wheres, base_model, i18n_model, parent_field, lang)
        wheres = wheres.where(getattr(i18n_model, field_name) == name)
    else:
        wheres = wheres.where(getattr(base_model, field_name) == name)
    return await _paginate_with_localization(db, wheres, category, lang)


async def get_crafting(db: AsyncSession, name: str, lang: str = "en"):
    return await _get_by_name(
        db,
        base_model=Crafting,
        i18n_model=CraftingI18n,
        parent_field="CraftingID",
        category="crafting",
        field_name="Name",
        name=name,
        lang=lang,
    )


async def get_gear(db: AsyncSession, name: str, lang: str = "en"):
    return await _get_by_name(
        db,
        base_model=Gear,
        i18n_model=GearI18n,
        parent_field="GearID",
        category="gear",
        field_name="Name",
        name=name,
        lang=lang,
    )


async def get_foodeffects(db: AsyncSession, name: str, lang: str = "en"):
    return await _get_by_name(
        db,
        base_model=FoodEffect,
        i18n_model=FoodEffectI18n,
        parent_field="FoodEffectID",
        category="foodeffect",
        field_name="Name",
        name=name,
        lang=lang,
    )


async def get_breeding(db: AsyncSession, name: str, lang: str = "en"):
    pal_id = await _get_pal_id(db, name, lang)
    statement = select(BreedingRecord).where(BreedingRecord.EggPalID == pal_id)
    return await _paginate_breeding(db, statement, lang)


async def _paginate_breeding(db: AsyncSession, statement, lang: str):
    """Resolve relationship rows before Page[Breeding] validates them."""

    async def transform(rows):
        return await _resolve_breeding_names(db, rows, lang)

    return await paginate(db, statement, transformer=transform)


async def _paginate_scalar_autocomplete(db: AsyncSession, statement):
    """Flatten single-column row results before AutoCompletePage[str] validation."""

    async def transform(rows):
        return [row[0] for row in rows]

    return await paginate(db, statement, transformer=transform)


async def _get_pal_id(db: AsyncSession, name: str, lang: str) -> int | None:
    if lang == "en":
        statement = select(Pals.ID).where(Pals.Name == name)
    else:
        statement = (
            select(Pals.ID)
            .join(PalsI18n, PalsI18n.PalsID == Pals.ID)
            .where(PalsI18n.LanguageCode == lang, PalsI18n.Name == name)
        )
    return (await db.exec(statement)).first()


async def _resolve_breeding_names(db: AsyncSession, rows, lang: str):
    pal_ids = {
        pal_id
        for row in rows
        for pal_id in (row.EggPalID, row.P1PalID, row.P2PalID)
    }
    if not pal_ids:
        return []

    base_statement = select(Pals.ID, Pals.Name).where(Pals.ID.in_(pal_ids))
    names = dict((await db.exec(base_statement)).all())
    if lang != "en":
        localized_statement = (
            select(Pals.ID, PalsI18n.Name)
            .join(PalsI18n, PalsI18n.PalsID == Pals.ID)
            .where(Pals.ID.in_(pal_ids), PalsI18n.LanguageCode == lang)
        )
        names.update((await db.exec(localized_statement)).all())

    return [
        Breeding(
            ID=row.ID,
            Egg=names.get(row.EggPalID, str(row.EggPalID)),
            P1=names.get(row.P1PalID, str(row.P1PalID)),
            P2=names.get(row.P2PalID, str(row.P2PalID)),
        )
        for row in rows
    ]


async def get_sickness(db: AsyncSession, name: str, lang: str = "en"):
    return await _get_by_name(
        db,
        base_model=SickPal,
        i18n_model=SickPalI18n,
        parent_field="SickPalID",
        category="sickpal",
        field_name="Name",
        name=name,
        lang=lang,
    )


async def get_tech(db: AsyncSession, name: str, lang: str = "en"):
    return await _get_by_name(
        db,
        base_model=TechTree,
        i18n_model=TechTreeI18n,
        parent_field="TechTreeID",
        category="techtree",
        field_name="Name",
        name=name,
        lang=lang,
    )


async def get_tech_by_level(db: AsyncSession, level: int, lang: str = "en"):
    return await _paginate_with_localization(
        db,
        select(TechTree).where(TechTree.LevelCap == level),
        "techtree",
        lang,
    )


async def get_build(db: AsyncSession, name: str, lang: str = "en"):
    return await _get_by_name(
        db,
        base_model=BuildObjects,
        i18n_model=BuildObjectsI18n,
        parent_field="BuildObjectsID",
        category="buildobjects",
        field_name="Name",
        name=name,
        lang=lang,
    )


async def get_build_by_category(db: AsyncSession, category: str, lang: str = "en"):
    wheres = select(BuildObjects)
    if lang != "en":
        wheres = _localized_join(wheres, BuildObjects, BuildObjectsI18n, "BuildObjectsID", lang)
        wheres = wheres.where(BuildObjectsI18n.Category == category)
    else:
        wheres = wheres.where(BuildObjects.Category == category)
    return await _paginate_with_localization(db, wheres, "buildobjects", lang)


async def get_passive(db: AsyncSession, name: str, lang: str = "en"):
    return await paginate(db, select(PassiveSkills).where(PassiveSkills.Name == name))


async def get_npc(db: AsyncSession, name: str, lang: str = "en"):
    return await _get_by_name(
        db,
        base_model=NPC,
        i18n_model=NPCI18n,
        parent_field="NPCID",
        category="npc",
        field_name="Name",
        name=name,
        lang=lang,
    )


async def get_elixir(db: AsyncSession, name: str, lang: str = "en"):
    return await _get_by_name(
        db,
        base_model=Elixir,
        i18n_model=ElixirI18n,
        parent_field="ElixirID",
        category="elixir",
        field_name="Name",
        name=name,
        lang=lang,
    )


async def get_all(db: AsyncSession, name, lang: str = "en"):
    model_map = {
        "pals": Pals,
        "bosspals": BossPals,
        "items": Items,
        "breeding": BreedingRecord,
        "buildobjects": BuildObjects,
        "crafting": Crafting,
        "foodeffect": FoodEffect,
        "gear": Gear,
        "sickpal": SickPal,
        "techtree": TechTree,
        "passiveskills": PassiveSkills,
        "npc": NPC,
        "elixir": Elixir,
    }
    model = model_map.get(name)
    if model is None:
        return
    if name == "breeding":
        return await _paginate_breeding(db, select(model), lang)
    page = await paginate(db, select(model))
    return await _apply_localization(db, page, name, lang)


async def get_autocomplete(db: AsyncSession, category: str, name: str, lang: str = "en"):
    localized_map = {
        "palname": (PalsI18n, PalsI18n.Name),
        "bossname": (BossPalsI18n, BossPalsI18n.Name),
        "sickness": (SickPalI18n, SickPalI18n.Name),
        "itemname": (ItemsI18n, ItemsI18n.Name),
        "crafting": (CraftingI18n, CraftingI18n.Name),
        "gear": (GearI18n, GearI18n.Name),
        "food": (FoodEffectI18n, FoodEffectI18n.Name),
        "tech": (TechTreeI18n, TechTreeI18n.Name),
        "buildname": (BuildObjectsI18n, BuildObjectsI18n.Name),
        "buildcategory": (BuildObjectsI18n, BuildObjectsI18n.Category),
        "elixir": (ElixirI18n, ElixirI18n.Name),
        "npc": (NPCI18n, NPCI18n.Name),
    }
    if category == "skill":
        source_model = PalsI18n if lang != "en" else Pals
        skill_table = func.JSON_TABLE(
            source_model.Skills,
            literal_column("'$[*]'"),
            literal_column("COLUMNS(skill_name VARCHAR(255) PATH '$.Name')"),
        ).table_valued(sql_column("skill_name"))
        statement = (
            select(skill_table.c.skill_name)
            .select_from(source_model)
            .join(skill_table, true())
            .where(skill_table.c.skill_name.like(f"{name}%"))
            .order_by(skill_table.c.skill_name.asc())
            .distinct()
        )
        if lang != "en":
            statement = statement.where(source_model.LanguageCode == lang)
        return await _paginate_scalar_autocomplete(db, statement)

    if lang != "en" and category in localized_map:
        model, column = localized_map[category]
        return await _paginate_scalar_autocomplete(
            db,
            select(column)
            .where(model.LanguageCode == lang, column.like(f"{name}%"))
            .order_by(column.asc())
            .distinct(),
        )

    if category == "palname":
        return await _paginate_scalar_autocomplete(
            db,
            select(Pals.Name)
            .where(Pals.Name.like(f"{name}%"))
            .order_by(Pals.Name.asc())
            .distinct(),
        )
    elif category == "paldexkey":
        return await _paginate_scalar_autocomplete(
            db,
            select(Pals.DexKey)
            .where(Pals.DexKey.like(f"{name}%"))
            .order_by(Pals.DexKey.asc())
            .distinct(),
        )
    elif category == "bossname":
        return await _paginate_scalar_autocomplete(
            db,
            select(BossPals.Name)
            .where(BossPals.Name.like(f"{name}%"))
            .order_by(BossPals.Name.asc())
            .distinct(),
        )
    elif category == "sickness":
        return await _paginate_scalar_autocomplete(
            db,
            select(SickPal.Name)
            .where(SickPal.Name.like(f"{name}%"))
            .order_by(SickPal.Name.asc())
            .distinct(),
        )
    elif category == "passiveskill":
        return await _paginate_scalar_autocomplete(
            db,
            select(PassiveSkills.Name)
            .where(PassiveSkills.Name.like(f"{name}%"))
            .order_by(PassiveSkills.Name.asc())
            .distinct(),
        )
    elif category == "itemname":
        return await _paginate_scalar_autocomplete(
            db,
            select(Items.Name)
            .where(Items.Name.like(f"{name}%"))
            .order_by(Items.Name.asc())
            .distinct(),
        )
    elif category == "itemtype":
        return await _paginate_scalar_autocomplete(
            db,
            select(Items.Type)
            .where(Items.Type.like(f"{name}%"))
            .order_by(Items.Type.asc())
            .distinct(),
        )
    elif category == "crafting":
        return await _paginate_scalar_autocomplete(
            db,
            select(Crafting.Name)
            .where(Crafting.Name.like(f"{name}%"))
            .order_by(Crafting.Name.asc())
            .distinct(),
        )
    elif category == "gear":
        return await _paginate_scalar_autocomplete(
            db,
            select(Gear.Name)
            .where(Gear.Name.like(f"{name}%"))
            .order_by(Gear.Name.asc())
            .distinct(),
        )
    elif category == "food":
        return await _paginate_scalar_autocomplete(
            db,
            select(FoodEffect.Name)
            .where(FoodEffect.Name.like(f"{name}%"))
            .order_by(FoodEffect.Name.asc())
            .distinct(),
        )
    elif category == "tech":
        return await _paginate_scalar_autocomplete(
            db,
            select(TechTree.Name)
            .where(TechTree.Name.like(f"{name}%"))
            .order_by(TechTree.Name.asc())
            .distinct(),
        )
    elif category == "buildname":
        return await _paginate_scalar_autocomplete(
            db,
            select(BuildObjects.Name)
            .where(BuildObjects.Name.like(f"{name}%"))
            .order_by(BuildObjects.Name.asc())
            .distinct(),
        )
    elif category == "buildcategory":
        return await _paginate_scalar_autocomplete(
            db,
            select(BuildObjects.Category)
            .where(BuildObjects.Category.like(f"{name}%"))
            .order_by(BuildObjects.Category.asc())
            .distinct(),
        )
    elif category == "elixir":
        return await _paginate_scalar_autocomplete(
            db,
            select(Elixir.Name)
            .where(Elixir.Name.like(f"{name}%"))
            .order_by(Elixir.Name.asc())
            .distinct(),
        )
    elif category == "npc":
        return await _paginate_scalar_autocomplete(
            db,
            select(NPC.Name)
            .where(NPC.Name.like(f"{name}%"))
            .order_by(NPC.Name.asc())
            .distinct(),
        )
    return
