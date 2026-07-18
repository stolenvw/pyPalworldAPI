# Python Examples

These examples use `aiohttp`.

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


## OAuth Routes

These routes are available when `COMPOSE_PROFILES=USE_OAUTH2`.

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

## Protected Route Example

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
