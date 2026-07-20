# Python Examples

These examples use `aiohttp`.

Set `BASE_URL` to match where your API is running, such as `http://127.0.0.1:8000`.

> [!TIP]
> Update `BASE_URL` first before trying the examples, especially if you are using a custom port or reverse proxy.

## Shared helpers

```python
import asyncio
import json

import aiohttp
from aiohttp.client_exceptions import ClientConnectorError


BASE_URL = "http://127.0.0.1"


async def get_json(method: str, path: str, *, headers=None, params=None, data=None, json_body=None):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.request(
                method,
                f"{BASE_URL}{path}",
                headers=headers,
                params=params,
                data=data,
                json=json_body,
            ) as result:
                payload = await result.json()
    except ClientConnectorError as exc:
        print(f"ClientConnectorError: {exc}")
    else:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
```

## Data Routes

If OAuth is disabled, these requests can be sent as shown below. If OAuth is enabled, send the same requests with `Authorization: Bearer ACCESS-TOKEN`.

### Pals

```python
async def get_pals():
    await get_json(
        "GET",
        "/pals/",
        headers={"Accept": "application/json"},
        params={"name": "Lamball", "page": 1, "size": 50},
    )


asyncio.run(get_pals())
```

### Pals in Simplified Chinese

```python
async def get_pals_zh_hans():
    await get_json(
        "GET",
        "/pals/",
        headers={"Accept": "application/json"},
        params={"name": "棉悠悠", "lang": "zh-Hans", "page": 1, "size": 50},
    )


asyncio.run(get_pals_zh_hans())
```

### Items

```python
async def get_items():
    await get_json(
        "GET",
        "/items/",
        headers={"Accept": "application/json"},
        params={"name": "Arrow", "page": 1, "size": 50},
    )


asyncio.run(get_items())
```

### Breeding by egg name

```python
async def get_breeding_by_egg():
    await get_json(
        "GET",
        "/breeding/",
        headers={"Accept": "application/json"},
        params={"egg": "Anubis", "lang": "en", "page": 1, "size": 50},
    )


asyncio.run(get_breeding_by_egg())
```

The legacy `/breeding/?name=...` alias is deprecated in the shipped API and will be removed in a future version. Use `egg`, or use `p1` and `p2` for parent-pair lookups.

### Full category pagination

```python
async def get_all_pals():
    await get_json(
        "GET",
        "/all/pals",
        headers={"Accept": "application/json"},
        params={"lang": "en", "page": 1, "size": 50},
    )


asyncio.run(get_all_pals())
```

### Map locations

```python
async def get_map_locations():
    await get_json(
        "GET",
        "/map-locations/",
        headers={"Accept": "application/json"},
        params={"category": "fast_travel", "map": "world", "page": 1, "size": 50},
    )


asyncio.run(get_map_locations())
```

### Autocomplete

```python
async def get_autocomplete():
    await get_json(
        "GET",
        "/autocomplete/palname/",
        headers={"Accept": "application/json"},
        params={"name": "La", "page": 1, "size": 25},
    )


asyncio.run(get_autocomplete())
```

### Skill autocomplete in Simplified Chinese

```python
async def get_skill_autocomplete_zh_hans():
    await get_json(
        "GET",
        "/autocomplete/skill/",
        headers={"Accept": "application/json"},
        params={"name": "龙", "lang": "zh-Hans", "page": 1, "size": 25},
    )


asyncio.run(get_skill_autocomplete_zh_hans())
```

### NPC autocomplete

```python
async def get_npc_autocomplete():
    await get_json(
        "GET",
        "/autocomplete/npc/",
        headers={"Accept": "application/json"},
        params={"name": "Wan", "page": 1, "size": 25},
    )


asyncio.run(get_npc_autocomplete())
```

## Data Routes With OAuth

These are a small sample of the same data endpoints shown above, this time with the auth header required when `COMPOSE_PROFILES=USE_OAUTH2`. The other data-route examples above also support `Authorization: Bearer ACCESS-TOKEN` when OAuth is enabled.

> [!IMPORTANT]
> The examples in this section are only samples. The other data-route examples above also become protected when OAuth is enabled.

### Pals with Bearer token

```python
async def get_pals_with_token():
    await get_json(
        "GET",
        "/pals/",
        headers={
            "Accept": "application/json",
            "Authorization": "Bearer ACCESS-TOKEN",
        },
        params={"name": "Lamball", "page": 1, "size": 50},
    )


asyncio.run(get_pals_with_token())
```

### Map locations with Bearer token

```python
async def get_map_locations_with_token():
    await get_json(
        "GET",
        "/map-locations/",
        headers={
            "Accept": "application/json",
            "Authorization": "Bearer ACCESS-TOKEN",
        },
        params={"category": "fast_travel", "map": "world", "page": 1, "size": 50},
    )


asyncio.run(get_map_locations_with_token())
```

## OAuth Routes

These routes are available when `COMPOSE_PROFILES=USE_OAUTH2`.

> [!WARNING]
> `/oauth2/validate` does not use the normal Bearer format. It expects `Authorization: OAuth ACCESS-TOKEN`.

### Login

```python
async def login():
    await get_json(
        "POST",
        "/oauth2/login/",
        headers={
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data={"username": "Bob123", "password": "SomePass"},
    )


asyncio.run(login())
```

### Refresh an access token

```python
async def refresh():
    await get_json(
        "POST",
        "/oauth2/refresh/",
        headers={
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data={"token": "REFRESH-TOKEN", "grant_type": "refresh_token"},
    )


asyncio.run(refresh())
```

### Validate token

```python
async def validate_token():
    await get_json(
        "GET",
        "/oauth2/validate",
        headers={
            "Accept": "application/json",
            "Authorization": "OAuth ACCESS-TOKEN",
        },
    )


asyncio.run(validate_token())
```

## User Routes

### Current user

```python
async def get_current_user():
    await get_json(
        "GET",
        "/user/me/",
        headers={
            "Accept": "application/json",
            "Authorization": "Bearer ACCESS-TOKEN",
        },
    )


asyncio.run(get_current_user())
```

### Change password

```python
async def change_password():
    await get_json(
        "PUT",
        "/user/changepassword/",
        headers={
            "Accept": "application/json",
            "Authorization": "Bearer ACCESS-TOKEN",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data={"current_password": "OldPass", "new_password": "NewPass"},
    )


asyncio.run(change_password())
```

## Admin Routes

### Add user

```python
async def add_user():
    await get_json(
        "POST",
        "/admin/adduser/",
        headers={
            "Accept": "application/json",
            "Authorization": "Bearer ACCESS-TOKEN",
            "Content-Type": "application/json",
        },
        json_body={
            "username": "Bob123",
            "password": "SomePass",
            "scopes": ["APIUser:Read", "APIUser:ChangePassword"],
            "disabled": False,
        },
    )


asyncio.run(add_user())
```

### List users

```python
async def list_users():
    await get_json(
        "GET",
        "/admin/users/",
        headers={
            "Accept": "application/json",
            "Authorization": "Bearer ACCESS-TOKEN",
        },
        params={"page": 1, "size": 50},
    )


asyncio.run(list_users())
```

### Change a user's scopes

```python
async def change_scopes():
    await get_json(
        "PUT",
        "/admin/chscope/",
        headers={
            "Accept": "application/json",
            "Authorization": "Bearer ACCESS-TOKEN",
            "Content-Type": "application/json",
        },
        json_body={
            "username": "Bob123",
            "scopes": ["APIUser:Read", "APIUser:ChangePassword"],
        },
    )


asyncio.run(change_scopes())
```
