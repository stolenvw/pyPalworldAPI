# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added

- Game data from v0.3.5
- Get autocomplete to help with discord bots slash command autocomplete
    ```http
    GET /autocomplete/{category}/?name=
    ```
- Container for user database, that uses a different storage volume (`db-user-data`).  This allows you to delete the `db-data` volume when doing updates to get the new api data without losing all the user accounts. *_Only made if `COMPOSE_PROFILES` is set to `USE_OAUTH2`._
- Environment variables for OAuth
    - `MYSQL_USER_DATABASE` Database to store user accounts.
    - `SQL_USER_HOST` MySQL host for user accounts.
    - `COMPOSE_PROFILES` To use OAuth set to `USE_OAUTH2` else leave blank.
    - `SECRET_KEY` Used for making tokens.
    - `ACCESS_TOKEN_EXPIRE_MINUTES` How many minutes should a access token be valid for.
    - `REFRESH_TOKEN_EXPIRE_DAYS` How many days should a refresh token be valid for. When refreshing an access token a new refresh token will be issued if its getting close to expiring.
    - `ADMIN_NAME` Name of admin account that will be auto made if users table does not already exist, will be made with a default password of `pyPalworldAPI`
- API endpoints for OAuth
    - `/oauth2/login/` Used to login and get an access and refresh token. *_Logging in again will make all current access/refresh tokens invalid._
    - `/oauth2/refresh/` Used to get new access token after current one expired, will also give new refresh token if its close to expiring.
    - `/oauth2/validate` Used to check if access token is still valid.
    - `/user/changepassword/` Allows users with `APIUser:ChangePassword` scope to change there password. *_Will make all current access/refresh tokens invalid._
    - `/user/me/` Allows users with `APIUser:Read` scope to get username and scopes associated with the access token there using.
    - `/admin/adduser/` Allows user with `APIAdmin:Write` scope to add new users.
    - `/admin/chpass/` Allows user with `APIAdmin:Write` scope to change other users passwords. *_Will make all there current access/refresh tokens invalid._
    - `/admin/deleteuser/` Allows user with `APIAdmin:Write` scope to delete a user.
    - `/admin/users/` Allows user with `APIAdmin:Write` scope to list all users in the database.
    - `/admin/userdisable/` Allows user with `APIAdmin:Write` scope to disable a users account.
    - `/admin/chscope/` Allows user with `APIAdmin:Write` scope to change a users scopes.
- OAuth scopes
    - `APIAdmin:Write` Needed to use `/admin/*` endpoints.
    - `APIUser:Read` Needed to get info from API.
    - `APIUser:ChangePassword` Needed to use `/user/changepassword/` endpoint.
- `Curl` and `Python` request samples to the `/redoc` URL.

### Changed

- api folder name to pyPalworldAPI (Posable breaking change for people not using docker.)
- bcrypt to version 4.2.0
- fastapi to version 0.111.1
- fastapi-pagination to version 0.12.26
- pydantic to version 2.8.2
- SQLAlchemy to version 2.0.31
- sqlmodel to version 0.0.21
- uvicorn to version 0.30.4
- Most of the error returns to be format shown below, (Validation Error is still the same.)
    ```json
    {
        "status": 0,
        "message": "string"
    }
    ```

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
