"""
SQL table and data verification models for api data.

"""

from enum import Enum
from typing import Optional

from pydantic import SerializeAsAny
from sqlalchemy import Column, Index, String, UniqueConstraint
from sqlmodel import JSON, Field, SQLModel, Text


class HealthCheck(SQLModel):
    status: str = "OK"


class ItemPassive(SQLModel):
    PassiveSkill1: str
    PassiveSkill2: str
    PassiveSkill3: str
    PassiveSkill4: str


class Items(SQLModel, table=True):
    ID: Optional[int] = Field(default=None, primary_key=True)
    """Auto incremented database primary key."""
    Name: str = Field(index=True, sa_type=String(50))
    DevName: str = Field(sa_type=String(50))
    Image: Optional[str] = Field(sa_type=String(100))
    Type: str = Field(index=True, sa_type=String(45))
    Rank: int
    MaxStackCount: int
    Weight: float
    Gold: int
    Durability: Optional[int]
    MagazineSize: Optional[int]
    PhysicalAttackValue: Optional[int]
    HPValue: Optional[int]
    PhysicalDefenseValue: Optional[int]
    ShieldValue: Optional[int]
    MagicAttackValue: Optional[int]
    MagicDefenseValue: Optional[int]
    Description: str = Field(sa_column=Column(Text))
    ItemActorClass: Optional[str] = Field(sa_type=String(50))
    PassiveSkills: SerializeAsAny[ItemPassive] = Field(sa_column=Column(JSON))
    bLegalInGame: bool


class Crafting(SQLModel, table=True):
    ID: Optional[int] = Field(default=None, primary_key=True)
    """Auto incremented database primary key."""
    SourceKey: str = Field(sa_type=String(80), exclude=True)
    Name: str
    Output: int
    WorkAmount: int
    Material: dict[str, int] = Field(sa_column=Column(JSON))
    CraftExpRate: float


class Gear(SQLModel, table=True):
    ID: Optional[int] = Field(default=None, primary_key=True)
    """Auto incremented database primary key."""
    SourceKey: str = Field(sa_type=String(50), exclude=True)
    Name: str = Field(index=True, sa_type=String(50))
    Common: dict[str, int] = Field(sa_column=Column(JSON))
    Uncommon: dict[str, int] = Field(sa_column=Column(JSON))
    Rare: dict[str, int] = Field(sa_column=Column(JSON))
    Epic: dict[str, int] = Field(sa_column=Column(JSON))
    Legendary: dict[str, int] = Field(sa_column=Column(JSON))


class PalTypes(SQLModel):
    Name: str
    Image: str


class PalSuitability(SQLModel):
    Name: str
    Image: str
    Level: int


class PalAura(SQLModel):
    Name: str
    Description: str = Field(sa_column=Column(Text))
    Image: Optional[str]
    Tech: Optional[str]


class PalSkills(SQLModel):
    Name: str
    Type: str
    Description: str = Field(sa_column=Column(Text))
    Level: int
    Cooldown: int
    Power: int


class StatsAttack(SQLModel):
    Melee: int
    Ranged: int


class StatsSpeed(SQLModel):
    Walk: int
    Run: int
    Ride: int


class PalStats(SQLModel):
    HP: int
    Attack: SerializeAsAny[StatsAttack]
    Defense: int
    Stamina: int
    Speed: SerializeAsAny[StatsSpeed]
    Support: int
    Food: int
    CraftSpeed: int
    TransportSpeed: int
    EnemyMaxHPRate: float
    EnemyReceiveDamageRate: float
    EnemyInflictDamageRate: float


class PalBreeding(SQLModel):
    Rank: int = Field(description="CombiRank")
    Order: int
    MaleProbability: float = Field(description="MaleProbability")


class PalDrops(SQLModel):
    Name: str
    Rate: float
    Min: int
    Max: int

class DefeatRewardItem(SQLModel):
    Name: Optional[str]
    Image: Optional[str]
    Description: Optional[str] = Field(sa_column=Column(Text))


class Pals(SQLModel, table=True):
    ID: Optional[int] = Field(default=None, primary_key=True)
    """Auto incremented database primary key."""
    DevName: str = Field(sa_type=String(50), exclude=True)
    DexKey: str = Field(sa_type=String(4), description="ZukanIndex")
    Image: str = Field(sa_type=String(100))
    Name: str = Field(index=True, sa_type=String(50))
    Wiki: str = Field(sa_type=String(100))
    WikiImage: str = Field(sa_type=String(200))
    Types: SerializeAsAny[list[PalTypes]] = Field(sa_column=Column(JSON))
    Suitability: SerializeAsAny[list[PalSuitability]] = Field(sa_column=Column(JSON))
    Drops: SerializeAsAny[list[PalDrops]] = Field(sa_column=Column(JSON))
    Aura: SerializeAsAny[PalAura] = Field(sa_column=Column(JSON))
    Description: str = Field(sa_column=Column(Text))
    Skills: SerializeAsAny[list[PalSkills]] = Field(sa_column=Column(JSON))
    Stats: SerializeAsAny[PalStats] = Field(sa_column=Column(JSON))
    Asset: str = Field(sa_type=String(50), description="BPClass")
    Genus: str = Field(sa_type=String(50), description="GenusCategory")
    Rarity: int
    Price: int
    Size: str = Field(sa_type=String(2), description="EPalSizeType")
    Maps: dict[str, str] = Field(sa_column=Column(JSON))
    Breeding: SerializeAsAny[PalBreeding] = Field(sa_column=Column(JSON))
    AIResponse: str = Field(sa_type=String(20))
    Nocturnal: bool
    Predator: bool
    NooseTrap: bool
    IsRaidBoss: bool
    IgnoreStun: bool
    IgnoreCombi: bool
    FirstDefeatRewardItemID: SerializeAsAny[DefeatRewardItem] = Field(sa_column=Column(JSON))


class BossPals(SQLModel, table=True):
    ID: Optional[int] = Field(default=None, primary_key=True)
    """Auto incremented database primary key."""
    DevName: str = Field(sa_type=String(50), exclude=True)
    DexKey: str = Field(sa_type=String(4), description="ZukanIndex")
    Image: str = Field(sa_type=String(100))
    Name: str = Field(index=True, sa_type=String(50))
    Wiki: str = Field(sa_type=String(100))
    WikiImage: str = Field(sa_type=String(200))
    Types: SerializeAsAny[list[PalTypes]] = Field(sa_column=Column(JSON))
    Suitability: SerializeAsAny[list[PalSuitability]] = Field(sa_column=Column(JSON))
    Drops: SerializeAsAny[list[PalDrops]] = Field(sa_column=Column(JSON))
    Aura: SerializeAsAny[PalAura] = Field(sa_column=Column(JSON))
    Description: str = Field(sa_column=Column(Text))
    Skills: SerializeAsAny[list[PalSkills]] = Field(sa_column=Column(JSON))
    Stats: SerializeAsAny[PalStats] = Field(sa_column=Column(JSON))
    Asset: str = Field(sa_type=String(50), description="BPClass")
    Genus: str = Field(sa_type=String(50), description="GenusCategory")
    Rarity: int
    Price: int
    Size: str = Field(sa_type=String(2), description="EPalSizeType")
    BattleBGM: str = Field(sa_type=String(50), description="Boss battle location.")
    Maps: dict[str, str] = Field(sa_column=Column(JSON))
    AIResponse: str = Field(sa_type=String(20))
    Nocturnal: bool
    Predator: bool
    NooseTrap: bool
    IsRaidBoss: bool
    IgnoreStun: bool
    IgnoreCombi: bool
    FirstDefeatRewardItemID: SerializeAsAny[DefeatRewardItem] = Field(sa_column=Column(JSON))


class BreedingRecord(SQLModel, table=True):
    __tablename__ = "breeding"
    __table_args__ = (
        UniqueConstraint("EggPalID", "P1PalID", "P2PalID", name="uq_breeding_pair"),
    )

    ID: Optional[int] = Field(default=None, primary_key=True)
    """Auto incremented database primary key."""
    EggPalID: int = Field(foreign_key="pals.ID")
    P1PalID: int = Field(foreign_key="pals.ID")
    P2PalID: int = Field(foreign_key="pals.ID")


class Breeding(SQLModel):
    ID: int
    Egg: str
    P1: str = Field(sa_type=String(50))
    P2: str = Field(sa_type=String(50))


class PassiveSkills(SQLModel, table=True):
    ID: Optional[int] = Field(default=None, primary_key=True)
    """Auto incremented database primary key."""
    Name: str = Field(index=True, sa_type=String(50))
    DevName: str = Field(sa_type=String(50))
    Ability: str = Field(sa_type=String(50))
    Tier: int
    Description: str = Field(sa_column=Column(Text))
    Image: str = Field(sa_type=String(100))


class FoodEffects(SQLModel):
    Name: str
    Value: int
    Interaval: int


class FoodEffect(SQLModel, table=True):
    ID: Optional[int] = Field(default=None, primary_key=True)
    """Auto incremented database primary key."""
    SourceKey: str = Field(sa_type=String(80), exclude=True)
    Name: str = Field(index=True, sa_type=String(50))
    EffectTime: int
    Effects: SerializeAsAny[list[FoodEffects]] = Field(sa_column=Column(JSON))


class TechTree(SQLModel, table=True):
    ID: Optional[int] = Field(default=None, primary_key=True)
    """Auto incremented database primary key."""
    DevName: str = Field(sa_type=String(80), exclude=True)
    Name: str = Field(index=True, sa_type=String(50))
    UnlockBuildObjects: Optional[list] = Field(sa_column=Column(JSON))
    UnlockItemRecipes: Optional[list] = Field(sa_column=Column(JSON))
    Description: str = Field(sa_column=Column(Text))
    Image: str = Field(sa_type=String(100))
    RequireTechnology: Optional[str] = Field(sa_type=String(50))
    IsBossTechnology: bool
    LevelCap: int
    Cost: int


class SickPal(SQLModel, table=True):
    ID: Optional[int] = Field(default=None, primary_key=True)
    """Auto incremented database primary key."""
    DevName: str = Field(sa_type=String(50), exclude=True)
    Name: str = Field(index=True, sa_type=String(15))
    EffectiveItemRank: int
    WorkSpeed: int
    MoveSpeed: int
    SatietyDecrease: int
    Description: str = Field(sa_column=Column(Text))
    RecoveryProbabilityPercentageInPalBox: int


class BuildMaterial(SQLModel):
    Name: str = Field(sa_type=String(50))
    Amount: int


class BuildObjects(SQLModel, table=True):
    ID: Optional[int] = Field(default=None, primary_key=True)
    """Auto incremented database primary key."""
    DevName: str = Field(sa_type=String(80), exclude=True)
    MapObjectId: str = Field(sa_type=String(50))
    Name: str = Field(index=True, sa_type=String(50))
    Description: str = Field(sa_column=Column(Text))
    Image: Optional[str] = Field(sa_type=String(100))
    Material: SerializeAsAny[list[BuildMaterial]] = Field(sa_column=Column(JSON))
    Category: str = Field(index=True, sa_type=String(25), description="TypeA")
    RequiredBuildWorkAmount: float
    InstallNeighborThreshold: float
    IsInstallOnlyOnBase: bool
    IsInstallOnlyHubAround: bool
    BuildExpRate: float


class APIModels(str, Enum):
    pals = "pals"
    bosspals = "bosspals"
    items = "items"
    breeding = "breeding"
    buildobjects = "buildobjects"
    crafting = "crafting"
    foodeffect = "foodeffect"
    gear = "gear"
    sickpal = "sickpal"
    techtree = "techtree"
    passiveskills = "passiveskills"
    npc = "npc"
    elixir = "elixir"


class NPC(SQLModel, table=True):
    ID: Optional[int] = Field(default=None, primary_key=True)
    """Auto incremented database primary key."""
    Name: str = Field(index=True, sa_type=String(50))
    DevName: str = Field(sa_type=String(50))
    Asset: str = Field(sa_type=String(50), description="BPClass")
    Genus: str = Field(sa_type=String(50), description="GenusCategory")
    Weapon: Optional[str] = Field(sa_type=String(50))
    Stats: SerializeAsAny[PalStats] = Field(sa_column=Column(JSON))
    Rarity: int
    Price: int
    Size: str = Field(sa_type=String(2), description="EPalSizeType")
    AIResponse: str = Field(sa_type=String(200))
    NooseTrap: bool
    Suitability: SerializeAsAny[list[PalSuitability]] = Field(sa_column=Column(JSON))
    IsRaidBoss: bool
    IgnoreStun: bool
    IgnoreCombi: bool


class Elixir(SQLModel, table=True):
    ID: Optional[int] = Field(default=None, primary_key=True)
    """Auto incremented database primary key."""
    Name: str = Field(index=True, sa_type=String(50))
    Description: str = Field(sa_column=Column(Text))
    DevName: str = Field(sa_type=String(50))
    MaxHP: int
    MaxSP: int
    Power: int
    WorkSpeed: int
    maxInventoryWeight: int


class AutoCompleteModels(str, Enum):
    palname = "palname"
    paldexkey = "paldexkey"
    bossname = "bossname"
    sickness = "sickness"
    skill = "skill"
    passiveskill = "passiveskill"
    itemname = "itemname"
    itemtype = "itemtype"
    crafting = "crafting"
    gear = "gear"
    food = "food"
    tech = "tech"
    buildname = "buildname"
    buildcategory = "buildcategory"
    elixir = "elixir"
    npc = "npc"


class ItemsI18n(SQLModel, table=True):
    __table_args__ = (
        UniqueConstraint("ItemID", "LanguageCode", name="uq_itemsi18n_parent_language"),
        Index("ix_itemsi18n_language_name", "LanguageCode", "Name"),
    )

    ID: Optional[int] = Field(default=None, primary_key=True)
    ItemID: int
    LanguageCode: str = Field(sa_type=String(16))
    Name: str = Field(sa_type=String(100))
    Description: str = Field(sa_column=Column(Text))
    PassiveSkills: SerializeAsAny[ItemPassive] = Field(sa_column=Column(JSON))


class CraftingI18n(SQLModel, table=True):
    __table_args__ = (
        UniqueConstraint("CraftingID", "LanguageCode", name="uq_craftingi18n_parent_language"),
        Index("ix_craftingi18n_language_name", "LanguageCode", "Name"),
    )

    ID: Optional[int] = Field(default=None, primary_key=True)
    CraftingID: int
    LanguageCode: str = Field(sa_type=String(16))
    Name: str = Field(sa_type=String(100))
    Material: dict[str, int] = Field(sa_column=Column(JSON))


class GearI18n(SQLModel, table=True):
    __table_args__ = (
        UniqueConstraint("GearID", "LanguageCode", name="uq_geari18n_parent_language"),
        Index("ix_geari18n_language_name", "LanguageCode", "Name"),
    )

    ID: Optional[int] = Field(default=None, primary_key=True)
    GearID: int
    LanguageCode: str = Field(sa_type=String(16))
    Name: str = Field(sa_type=String(100))


class PalsI18n(SQLModel, table=True):
    __table_args__ = (
        UniqueConstraint("PalsID", "LanguageCode", name="uq_palsi18n_parent_language"),
        Index("ix_palsi18n_language_name", "LanguageCode", "Name"),
    )

    ID: Optional[int] = Field(default=None, primary_key=True)
    PalsID: int
    LanguageCode: str = Field(sa_type=String(16))
    Name: str = Field(sa_type=String(100))
    Types: SerializeAsAny[list[PalTypes]] = Field(sa_column=Column(JSON))
    Suitability: SerializeAsAny[list[PalSuitability]] = Field(sa_column=Column(JSON))
    Drops: SerializeAsAny[list[PalDrops]] = Field(sa_column=Column(JSON))
    Aura: SerializeAsAny[PalAura] = Field(sa_column=Column(JSON))
    Description: str = Field(sa_column=Column(Text))
    Skills: SerializeAsAny[list[PalSkills]] = Field(sa_column=Column(JSON))
    FirstDefeatRewardItemID: SerializeAsAny[DefeatRewardItem] = Field(sa_column=Column(JSON))


class BossPalsI18n(SQLModel, table=True):
    __table_args__ = (
        UniqueConstraint("BossPalsID", "LanguageCode", name="uq_bosspalsi18n_parent_language"),
        Index("ix_bosspalsi18n_language_name", "LanguageCode", "Name"),
    )

    ID: Optional[int] = Field(default=None, primary_key=True)
    BossPalsID: int
    LanguageCode: str = Field(sa_type=String(16))
    Name: str = Field(sa_type=String(100))
    Types: SerializeAsAny[list[PalTypes]] = Field(sa_column=Column(JSON))
    Suitability: SerializeAsAny[list[PalSuitability]] = Field(sa_column=Column(JSON))
    Drops: SerializeAsAny[list[PalDrops]] = Field(sa_column=Column(JSON))
    Aura: SerializeAsAny[PalAura] = Field(sa_column=Column(JSON))
    Description: str = Field(sa_column=Column(Text))
    Skills: SerializeAsAny[list[PalSkills]] = Field(sa_column=Column(JSON))
    FirstDefeatRewardItemID: SerializeAsAny[DefeatRewardItem] = Field(sa_column=Column(JSON))


class PassiveSkillsI18n(SQLModel, table=True):
    __table_args__ = (
        UniqueConstraint(
            "PassiveSkillsID",
            "LanguageCode",
            name="uq_passiveskillsi18n_parent_language",
        ),
        Index("ix_passiveskillsi18n_language_name", "LanguageCode", "Name"),
    )

    ID: Optional[int] = Field(default=None, primary_key=True)
    PassiveSkillsID: int
    LanguageCode: str = Field(sa_type=String(16))
    Name: str = Field(sa_type=String(100))
    Description: str = Field(sa_column=Column(Text))


class FoodEffectI18n(SQLModel, table=True):
    __table_args__ = (
        UniqueConstraint(
            "FoodEffectID",
            "LanguageCode",
            name="uq_foodeffecti18n_parent_language",
        ),
        Index("ix_foodeffecti18n_language_name", "LanguageCode", "Name"),
    )

    ID: Optional[int] = Field(default=None, primary_key=True)
    FoodEffectID: int
    LanguageCode: str = Field(sa_type=String(16))
    Name: str = Field(sa_type=String(100))


class TechTreeI18n(SQLModel, table=True):
    __table_args__ = (
        UniqueConstraint("TechTreeID", "LanguageCode", name="uq_techtreei18n_parent_language"),
        Index("ix_techtreei18n_language_name", "LanguageCode", "Name"),
    )

    ID: Optional[int] = Field(default=None, primary_key=True)
    TechTreeID: int
    LanguageCode: str = Field(sa_type=String(16))
    Name: str = Field(sa_type=String(100))
    UnlockBuildObjects: Optional[list] = Field(sa_column=Column(JSON))
    UnlockItemRecipes: Optional[list] = Field(sa_column=Column(JSON))
    Description: str = Field(sa_column=Column(Text))
    RequireTechnology: Optional[str] = Field(sa_type=String(100))


class SickPalI18n(SQLModel, table=True):
    __table_args__ = (
        UniqueConstraint("SickPalID", "LanguageCode", name="uq_sickpali18n_parent_language"),
        Index("ix_sickpali18n_language_name", "LanguageCode", "Name"),
    )

    ID: Optional[int] = Field(default=None, primary_key=True)
    SickPalID: int
    LanguageCode: str = Field(sa_type=String(16))
    Name: str = Field(sa_type=String(100))
    Description: str = Field(sa_column=Column(Text))


class BuildObjectsI18n(SQLModel, table=True):
    __table_args__ = (
        UniqueConstraint(
            "BuildObjectsID",
            "LanguageCode",
            name="uq_buildobjectsi18n_parent_language",
        ),
        Index("ix_buildobjectsi18n_language_name", "LanguageCode", "Name"),
        Index("ix_buildobjectsi18n_language_category", "LanguageCode", "Category"),
    )

    ID: Optional[int] = Field(default=None, primary_key=True)
    BuildObjectsID: int
    LanguageCode: str = Field(sa_type=String(16))
    Name: str = Field(sa_type=String(100))
    Description: str = Field(sa_column=Column(Text))
    Material: SerializeAsAny[list[BuildMaterial]] = Field(sa_column=Column(JSON))
    Category: str = Field(sa_type=String(100))


class NPCI18n(SQLModel, table=True):
    __table_args__ = (
        UniqueConstraint("NPCID", "LanguageCode", name="uq_npci18n_parent_language"),
        Index("ix_npci18n_language_name", "LanguageCode", "Name"),
    )

    ID: Optional[int] = Field(default=None, primary_key=True)
    NPCID: int
    LanguageCode: str = Field(sa_type=String(16))
    Name: str = Field(sa_type=String(100))
    Weapon: Optional[str] = Field(sa_type=String(100))
    Suitability: SerializeAsAny[list[PalSuitability]] = Field(sa_column=Column(JSON))


class ElixirI18n(SQLModel, table=True):
    __table_args__ = (
        UniqueConstraint("ElixirID", "LanguageCode", name="uq_elixiri18n_parent_language"),
        Index("ix_elixiri18n_language_name", "LanguageCode", "Name"),
    )

    ID: Optional[int] = Field(default=None, primary_key=True)
    ElixirID: int
    LanguageCode: str = Field(sa_type=String(16))
    Name: str = Field(sa_type=String(100))
    Description: str = Field(sa_column=Column(Text))
