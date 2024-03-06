from typing import Optional

from pydantic import ConfigDict
from sqlalchemy import Column, String
from sqlmodel import JSON, Field, SQLModel


class HealthCheck(SQLModel):
    status: str = "OK"


class Items(SQLModel, table=True):
    ID: Optional[int] = Field(default=None, primary_key=True)
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
    Descripition: str
    ItemActorClass: Optional[str] = Field(sa_type=String(50))


class Crafting(SQLModel, table=True):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )

    ID: Optional[int] = Field(default=None, primary_key=True)
    Name: str = Field(foreign_key="items")
    Output: int
    WorkAmount: int
    Material: dict[str, int] = Field(sa_column=Column(JSON))


class Gear(SQLModel, table=True):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )

    ID: Optional[int] = Field(default=None, primary_key=True)
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
    Description: str
    Tech: Optional[str]


class PalSkills(SQLModel):
    Name: str
    Type: str
    Description: str
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
    Attack: StatsAttack
    Defense: int
    Stamina: int
    Speed: StatsSpeed
    Support: int
    Food: int
    CraftSpeed: int
    TransportSpeed: int


class PalBreeding(SQLModel):
    Rank: int = Field(description="CombiRank")
    Order: int
    ChildEligble: bool
    MaleProbability: float = Field(description="MaleProbability")


class PalDrops(SQLModel):
    Name: str
    Rate: float
    Min: int
    Max: int


class Pals(SQLModel, table=True):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )

    ID: Optional[int] = Field(default=None, primary_key=True)
    DexKey: str = Field(sa_type=String(4), description="ZukanIndex")
    Image: str = Field(sa_type=String(100))
    Name: str = Field(index=True, sa_type=String(50))
    Wiki: str = Field(sa_type=String(100))
    WikiImage: str = Field(sa_type=String(100))
    Types: list[PalTypes] = Field(sa_column=Column(JSON))
    Suitability: list[PalSuitability] = Field(sa_column=Column(JSON))
    Drops: list[PalDrops] = Field(sa_column=Column(JSON))
    Aura: PalAura = Field(sa_column=Column(JSON))
    Description: str
    Skills: list[PalSkills] = Field(sa_column=Column(JSON))
    Stats: PalStats = Field(sa_column=Column(JSON))
    Asset: str = Field(sa_type=String(50), description="BPClass")
    Genus: str = Field(sa_type=String(50), description="GenusCategory")
    Rarity: int
    Price: int
    Size: str = Field(sa_type=String(2), description="EPalSizeType")
    Maps: dict[str, str] = Field(sa_column=Column(JSON))
    Breeding: PalBreeding = Field(sa_column=Column(JSON))
    AIResponse: str = Field(sa_type=String(20))
    Nocturnal: bool
    Predator: bool
    NooseTrap: bool


class BossPals(SQLModel, table=True):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )

    ID: Optional[int] = Field(default=None, primary_key=True)
    DexKey: str = Field(sa_type=String(4), description="ZukanIndex")
    Image: str = Field(sa_type=String(100))
    Name: str = Field(index=True, sa_type=String(50))
    Wiki: str = Field(sa_type=String(100))
    WikiImage: str = Field(sa_type=String(100))
    Types: list[PalTypes] = Field(sa_column=Column(JSON))
    Suitability: list[PalSuitability] = Field(sa_column=Column(JSON))
    Drops: list[PalDrops] = Field(sa_column=Column(JSON))
    Aura: PalAura = Field(sa_column=Column(JSON))
    Description: str
    Skills: list[PalSkills] = Field(sa_column=Column(JSON))
    Stats: PalStats = Field(sa_column=Column(JSON))
    Asset: str = Field(sa_type=String(50), description="BPClass")
    Genus: str = Field(sa_type=String(50), description="GenusCategory")
    Rarity: int
    Price: int
    Size: str = Field(sa_type=String(2), description="EPalSizeType")
    BattleBGM: str = Field(sa_type=String(50), description="Boss battle location.")
    AIResponse: str = Field(sa_type=String(20))
    Nocturnal: bool
    Predator: bool
    NooseTrap: bool


class Breeding(SQLModel, table=True):
    ID: Optional[int] = Field(default=None, primary_key=True)
    Egg: str = Field(index=True, sa_type=String(50))
    P1: str = Field(sa_type=String(50))
    P2: str = Field(sa_type=String(50))


class PassiveSkills(SQLModel, table=True):
    ID: Optional[int] = Field(default=None, primary_key=True)
    Name: str = Field(index=True, sa_type=String(50))
    DevName: str = Field(sa_type=String(50))
    Ability: str = Field(sa_type=String(50))
    Tier: int
    Description: str
    Image: str = Field(sa_type=String(100))


class FoodEffects(SQLModel):
    Name: str
    Value: int


class FoodEffect(SQLModel, table=True):
    ID: Optional[int] = Field(default=None, primary_key=True)
    Name: str = Field(index=True, sa_type=String(50))
    EffectTime: int
    Effects: list[FoodEffects] = Field(sa_column=Column(JSON))


class TechTree(SQLModel, table=True):
    ID: Optional[int] = Field(default=None, primary_key=True)
    Name: str = Field(index=True, sa_type=String(50))
    UnlockBuildObjects: Optional[list] = Field(sa_column=Column(JSON))
    UnlockItemRecipes: Optional[list] = Field(sa_column=Column(JSON))
    Description: str
    Image: str = Field(sa_type=String(100))
    RequireTechnology: Optional[str] = Field(sa_type=String(50))
    IsBossTechnology: bool
    LevelCap: int
    Cost: int


class SickPal(SQLModel, table=True):
    ID: Optional[int] = Field(default=None, primary_key=True)
    Name: str = Field(index=True, sa_type=String(15))
    EffectiveItemRank: int
    WorkSpeed: int
    MoveSpeed: int
    SatietyDecrease: int
    Description: str


class BuildMaterial(SQLModel):
    Name: str = Field(sa_type=String(50))
    Amount: int


class BuidObjects(SQLModel, table=True):
    ID: Optional[int] = Field(default=None, primary_key=True)
    MapObjectId: str = Field(sa_type=String(50))
    Name: str = Field(index=True, sa_type=String(50))
    Description: str
    Image: Optional[str] = Field(sa_type=String(100))
    Material: list[BuildMaterial] = Field(sa_column=Column(JSON))
    Category: str = Field(index=True, sa_type=String(25), description="TypeA")
    RequiredBuildWorkAmount: float
    InstallNeighborThreshold: float
    IsInstallOnlyOnBase: bool
    IsInstallOnlyHubAround: bool
