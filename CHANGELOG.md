# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added

- Game data from v0.3.1.55394

## [0.0.5] - 2024-6-27

### Changed

- "Boss" Pals HP, EnemyReceiveDamageRate, EnemyInflictDamageRate to new values from v0.2.4.0

## [0.0.4] - 2024-5-14

### Added

- Game data from v0.2.2.0

### Changed

- ITEM_NAME_PalSummon name from "Bellanoir's Slab" to "Summoning Altar"

## [0.0.3] - 2024-4-14

### Added

- Game data from v0.2.0.6
- Items passive skills
- Pal stats:
    - EnemyMaxHPRate
    - EnemyReceiveDamageRate
    - EnemyInflictDamageRate
- Pals IsRaidBoss
- BossPals IsRaidBoss
- FoodEffects Interaval
- SickPal RecoveryProbabilityPercentageInPalBox
- NPC IsRaidBoss
- Elixir
- New Breeding data (have checked some of them, if you find ones that are wrong let me know)

### Changed

- Some images to new version from v0.2.0.6

## [0.0.2] - 2024-3-13

### Added

- Get paginate return of full category
    ```http
    GET /all/{category}
    ```
- NPC information.

### Changed

- fastapi to version 0.110.0
- fastapi-pagination to version 0.12.19
- pydantic to version 2.6.3
- SQLAlchemy to version 2.0.28
- uvicorn to version 0.28.0
- get pals to take multiple params to filter results more
- get bosspals to take multiple params to filter results more

### Fixed

- Docs successful response example value, to show example instead of just "string"
