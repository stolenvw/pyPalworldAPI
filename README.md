<div align="center"><h1>Palworld API</h1>

A Palworld data API for apps and bots, with pals, items, breeding, and optional OAuth2. 

![GitHub Release](https://img.shields.io/github/v/release/stolenvw/pyPalworldAPI)
![GitHub top language](https://img.shields.io/github/languages/top/stolenvw/pyPalworldAPI)
![GitHub repo size](https://img.shields.io/github/repo-size/stolenvw/pyPalworldAPI)
![GitHub License](https://img.shields.io/github/license/stolenvw/pyPalworldAPI)
![Static Badge](https://img.shields.io/badge/%3E%3D3.12-gray?logo=python&label=Python&labelColor=gray&color=purple)
![Static Badge](https://img.shields.io/badge/v1.0.1.100619-gray?label=Game%20Data&labelColor=gray&color=blue)
</div>

## Overview

`pyPalworldAPI` gives you a self-hosted Palworld data API for apps, bots, websites, and other tools. It brings together pals, boss pals, breeding, items, crafting, gear, food effects, tech tree data, passive skills, NPCs, elixirs, and autocomplete helpers in one API.

Release-by-release changes live in [CHANGELOG.md](CHANGELOG.md).

## Quick Start

### Fastest Start

1. Copy [example.env](example.env) to `.env` and fill in your settings.
2. Choose whether you want OAuth enabled.
   Set `COMPOSE_PROFILES=USE_OAUTH2` to enable `/oauth2/*`, `/user/*`, and `/admin/*`.
   Leave it blank to run the API without those routes.
3. If you are not running behind a reverse proxy, uncomment the `ports` section for `pypalworldapi` in [compose.yaml](compose.yaml).
4. Start with Docker:

```bash
docker compose up
```

5. Open the API at `http://127.0.0.1:<HTTP_PORT>`.

> [!TIP]
> Use `docker compose up --build` after changing the Dockerfile, Python dependencies, or application code that needs a fresh image build.

### Run Locally

If you want to run without Docker, install [uv](https://docs.astral.sh/uv/), import [PalAPI.sql](mysqldb/PalAPI.sql) into MySQL, keep `.env` in the project root, and run:

```bash
uv sync --no-dev
uv run --no-sync uvicorn pyPalworldAPI.mainapi:app --host 0.0.0.0 --port 8000
```

> [!TIP]
> This project now ships with [pyproject.toml](pyproject.toml) and [uv.lock](uv.lock), so `uv sync` is the supported way to install the locked dependencies.

## Features

- Broad Palworld data coverage for pals, boss pals, breeding, items, crafting, gear, food effects, tech tree data, passive skills, NPCs, elixirs, and map locations
- Optional OAuth2 authentication with built-in user and admin management routes
- Localized responses with English and included `zh-Hans` (Simplified Chinese) data
- Autocomplete helpers for bot commands, app search boxes, and other lightweight integrations
- Built-in Swagger UI and ReDoc when those routes are enabled in `.env`
- MySQL-backed data storage with paginated, case-insensitive lookups

## API Availability

> [!IMPORTANT]
> OAuth, user, and admin routes are available only when `COMPOSE_PROFILES=USE_OAUTH2`.

- Core data routes are always available: `/pals/`, `/bosspals/`, `/breeding/`, `/sickness/`, `/items/`, `/crafting/`, `/gear/`, `/foodeffect/`, `/tech/`, `/build/`, `/passive/`, `/npc/`, `/elixir/`, `/map-locations/`, `/all/{category}`, `/autocomplete/{category}/`, and `/health`.
- OAuth and user-management routes are available when `COMPOSE_PROFILES=USE_OAUTH2`: `/oauth2/*`, `/user/*`, and `/admin/*`.
- Built-in docs are optional. `/docs` and `/redoc` are controlled by `.env` and may be disabled, so this README includes a compact route reference and [examples/](examples/README.md) includes longer request examples.

## Localization

> [!TIP]
> Use `lang=en` for default English data or `lang=zh-Hans` for Simplified Chinese data included with this release.

- `lang=en` uses the default English data.
- The included data currently provides localized `LanguageCode` rows for `zh-Hans` (Simplified Chinese).
- Most lookup routes and `/all/{category}` support `lang`.
- When you use a localized `lang` value, name-based lookups should use that language's spelling.
- Autocomplete supports `lang` for categories that have localized data available.
- `skill` autocomplete now reads Pal skill names from the shipped data, including localized Pal skill names when a supported `lang` value is used.
- `/passive/` accepts `lang`, but passive skill lookups currently return the default English passive skill data.

## API Reference

> [!NOTE]
> `/docs` and `/redoc` are optional. You can disable either one by leaving `DOCS_URL` or `REDOC_URL` blank in `.env`.

`/redoc` for API docs.

`/docs` for interactive API testing.

Examples below use `http://127.0.0.1` as the local base URL.

> [!TIP]
> If you expose the API on a non-default port, use `http://127.0.0.1:<HTTP_PORT>` instead.

`/health` returns:

```json
{
  "status": "OK"
}
```

> [!NOTE]
> _When OAuth is enabled, protected API routes use the Authorization header._
> - ```http
>   Authorization: Bearer ACCESS-TOKEN
>   ```

> [!WARNING]
> `/oauth2/validate` is a special case and expects:
> ```http
> Authorization: OAuth ACCESS-TOKEN
> ```

### Core Routes

| Route | Purpose | Key query params |
| :---- | :------ | :--------------- |
| `/pals/` | Look up pals | `name`, `dexkey`, `type`, `suitability`, `drop`, `skill`, `nocturnal`, `lang`, `page`, `size` |
| `/bosspals/` | Look up boss pals | `name`, `type`, `suitability`, `drop`, `skill`, `nocturnal`, `lang`, `page`, `size` |
| `/breeding/` | Find breeding combinations by egg pal or parent pair | `egg` or `p1`+`p2`, `lang`, `page`, `size` |
| `/sickness/` | Look up sickness data | `name`, `lang`, `page`, `size` |
| `/items/` | Look up items | `name`, `type`, `lang`, `page`, `size` |
| `/crafting/` | Look up crafting recipes | `name`, `lang`, `page`, `size` |
| `/gear/` | Look up gear | `name`, `lang`, `page`, `size` |
| `/foodeffect/` | Look up food effects | `name`, `lang`, `page`, `size` |
| `/tech/` | Look up tech tree entries | `name` or `level`, `lang`, `page`, `size` |
| `/build/` | Look up build objects | `name` or `category`, `lang`, `page`, `size` |
| `/passive/` | Look up passive skills | `name`, `lang`, `page`, `size` |
| `/npc/` | Look up NPCs | `name`, `lang`, `page`, `size` |
| `/elixir/` | Look up elixirs | `name`, `lang`, `page`, `size` |
| `/map-locations/` | Look up map locations | `category`, `map`, `page`, `size` |
| `/all/{category}` | Paginate a full category | `lang`, `page`, `size` |
| `/autocomplete/{category}/` | Autocomplete helper | `name`, `lang`, `page`, `size` |
| `/health` | Health check | none |

### `map-locations` Values

- `map`: `world`, `tree`
- Current shipped `category` values: `dungeon`, `fast_travel`, `lifmunk_effigy`, `note`, `tower`, `treasure_map`

> [!WARNING]
> `/breeding/` still accepts the legacy `name` query parameter as an alias for `egg`, but it is marked deprecated in the shipped API and will be removed in a future version. Prefer `egg`, or use `p1` and `p2` for parent-pair lookups.

### `all/{category}` Values

`pals`, `bosspals`, `items`, `breeding`, `buildobjects`, `crafting`, `foodeffect`, `gear`, `sickpal`, `techtree`, `passiveskills`, `npc`, `elixir`, `maplocations`

### `autocomplete/{category}` Values

`palname`, `paldexkey`, `bossname`, `sickness`, `skill`, `passiveskill`, `itemname`, `itemtype`, `crafting`, `gear`, `food`, `tech`, `buildname`, `buildcategory`, `elixir`, `npc`

### OAuth and User Routes

These routes are available when `COMPOSE_PROFILES=USE_OAUTH2`.

| Route | Method | Purpose |
| :---- | :----- | :------ |
| `/oauth2/login/` | `POST` | Get access and refresh tokens |
| `/oauth2/refresh/` | `POST` | Refresh an access token |
| `/oauth2/validate` | `GET` | Validate an access token |
| `/user/changepassword/` | `PUT` | Change the current user's password |
| `/user/me/` | `GET` | Get the current user's username and scopes |
| `/admin/adduser/` | `POST` | Create a user |
| `/admin/chpass/` | `PUT` | Change another user's password |
| `/admin/deleteuser/` | `DELETE` | Delete a user |
| `/admin/users/` | `GET` | List users |
| `/admin/userdisable/` | `PUT` | Enable or disable a user |
| `/admin/chscope/` | `PUT` | Change a user's scopes |

## Examples

- Start with [examples/README.md](examples/README.md) for the examples guide.
- Use [examples/http.md](examples/http.md) for `curl` examples.
- Use [examples/python.md](examples/python.md) for `aiohttp` examples.

> [!NOTE]
> The example files include both open routes and OAuth-protected routes. If `COMPOSE_PROFILES` is blank, only the open-route examples will apply.

## Deployment

### Docker

1. [Download the latest release](https://github.com/stolenvw/pyPalworldAPI/releases/latest).
2. Extract it somewhere.
3. Edit [example.env](example.env) and rename it to `.env`.

To create `SECRET_KEY`:
- Linux: Run `openssl rand -hex 32`.
- Windows: You can use https://www.browserling.com/tools/random-hex and change `How many digits?` to 64.

> [!TIP]
> If you enable OAuth, the first admin account uses `ADMIN_NAME` and starts with the default password `pyPalworldAPI`. Change it after signing in.

Additional notes:
- Leave `COMPOSE_PROFILES` blank if you do not want OAuth, user, or admin routes.
- Keep `DOCS_URL` and `REDOC_URL` set if you want `/docs` or `/redoc`. Leave either blank to disable it.
- The current container image installs dependencies from [pyproject.toml](pyproject.toml) and [uv.lock](uv.lock) with `uv`.

4. Edit [compose.yaml](compose.yaml).

Uncomment:

```yaml
#ports:
#  - ${HTTP_PORT}:${HTTP_PORT}
```

5. If you are not running behind a reverse proxy, edit the Dockerfile.

<details>
  <summary>Dockerfile Edits</summary>

Uncomment this line:

```dockerfile
# CMD ["sh", "-c", "uv run uvicorn pyPalworldAPI.mainapi:app --host 0.0.0.0 --port $HTTP_PORT"]
```

Comment this line:

```dockerfile
CMD ["sh", "-c", "uv run uvicorn pyPalworldAPI.mainapi:app --host 0.0.0.0 --port $HTTP_PORT --proxy-headers --forwarded-allow-ips='*'"]
```
</details>

6. Start the stack:

```bash
docker compose up
```

### Run Without Docker

You will need your own MySQL server.

1. Follow the setup steps above.
2. Install [uv](https://docs.astral.sh/uv/).
3. Keep `.env` in the project root.
4. Install locked production dependencies:

```bash
uv sync --no-dev
```

5. Import [PalAPI.sql](mysqldb/PalAPI.sql) into your MySQL server.
6. Run the following commands from the project root.

If not using a reverse proxy:

```bash
uv run --no-sync uvicorn pyPalworldAPI.mainapi:app --host 0.0.0.0 --port 8000
```

If you are using a reverse proxy:

```bash
uv run --no-sync uvicorn pyPalworldAPI.mainapi:app --host 0.0.0.0 --port 8000 --proxy-headers --forwarded-allow-ips='*'
```

## Environment Variables

To run this project, configure these environment variables in `.env`.

### Common Settings

| Variable | Required | Description |
| :-------- | :------- | :---------- |
| `COMPOSE_PROFILES` | No | Set to `USE_OAUTH2` to enable `/oauth2/*`, `/user/*`, and `/admin/*`. Leave it blank to disable OAuth features. |
| `DOCS_URL` | No | Path for Swagger UI. Set to `/docs` or leave blank to disable. |
| `REDOC_URL` | No | Path for ReDoc. Set to `/redoc` or leave blank to disable. |
| `HTTP_PORT` | Yes | Port exposed by the API container or local `uvicorn` process. |
| `MYSQL_USER` | Yes | MySQL username for the main Palworld data database. |
| `MYSQL_PASSWORD` | Yes | MySQL password for the main Palworld data database. |
| `MYSQL_DATABASE` | Yes | MySQL database name for the main Palworld data tables. |
| `SQL_HOST` | Yes | MySQL host for the main Palworld data database. |
| `MYSQL_PORT` | Yes | MySQL port. |
| `MYSQL_RANDOM_ROOT_PASSWORD` | Docker only | Docker MySQL setting for generating the root password automatically. |

### OAuth Settings

These values are used when OAuth is enabled. In the current release, the OAuth database connection settings still need to be present in `.env` even if OAuth routes are disabled.

| Variable | Required | Description |
| :-------- | :------- | :---------- |
| `SECRET_KEY` | Yes | Secret used to sign access and refresh tokens. |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Yes | Access token lifetime in minutes. |
| `REFRESH_TOKEN_EXPIRE_DAYS` | Yes | Refresh token lifetime in days. |
| `ADMIN_NAME` | OAuth only | Admin username created on first startup when the auth tables do not already exist. |
| `MYSQL_USER_DATABASE` | Yes | MySQL database name used for the OAuth user and token connection. This value still needs to be present in the current release, even if OAuth routes are disabled. |
| `SQL_USER_HOST` | Yes | MySQL host used for the OAuth user and token connection. |

## Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) for the API layer
- [SQLModel](https://sqlmodel.tiangolo.com/) for database models and queries
- [MySQL](https://www.mysql.com/) for Palworld data and OAuth user storage
- [Docker](https://www.docker.com/) and Docker Compose for deployment
- [uv](https://docs.astral.sh/uv/) for Python dependency management
- [FastAPI Pagination](https://uriyyo-fastapi-pagination.netlify.app/) for paginated responses

> [!NOTE]
> The current repo metadata targets Python `>=3.12`, and the Docker image currently builds on Astral's `uv` Python 3.14 base image.

## Acknowledgements

- [dkoz](https://github.com/dkoz)

## License

Distributed under the [MIT](LICENSE) License
