# HTTP Examples

Examples below use `http://127.0.0.1` as the base URL. If your API is exposed on another host or port, replace that part of each request first.

> [!TIP]
> If your API is running on another port, update the examples to use a base URL such as `http://127.0.0.1:8000`.

## Data Routes

If OAuth is disabled, these requests can be sent as shown below. If OAuth is enabled, send the same requests with `Authorization: Bearer ACCESS-TOKEN`.

### Pals

```bash
curl -X 'GET' \
  'http://127.0.0.1/pals/?name=Lamball&page=1&size=50' \
  -H 'Accept: application/json'
```

### Pals with localization

```bash
curl -X 'GET' \
  'http://127.0.0.1/pals/?name=棉悠悠&lang=zh-Hans&page=1&size=50' \
  -H 'Accept: application/json'
```

### Boss pals

```bash
curl -X 'GET' \
  'http://127.0.0.1/bosspals/?name=Mammorest&page=1&size=50' \
  -H 'Accept: application/json'
```

### Items

```bash
curl -X 'GET' \
  'http://127.0.0.1/items/?name=Arrow&page=1&size=50' \
  -H 'Accept: application/json'
```

### Breeding by egg name

```bash
curl -X 'GET' \
  'http://127.0.0.1/breeding/?egg=Anubis&lang=en&page=1&size=50' \
  -H 'Accept: application/json'
```

> [!WARNING]
> The legacy `/breeding/?name=...` alias is deprecated in the shipped API and will be removed in a future version. Use `egg`, or use `p1` and `p2` for parent-pair lookups.

### Crafting

```bash
curl -X 'GET' \
  'http://127.0.0.1/crafting/?name=Arrow&page=1&size=50' \
  -H 'Accept: application/json'
```

### Tech tree by name

```bash
curl -X 'GET' \
  'http://127.0.0.1/tech/?name=Nail&page=1&size=50' \
  -H 'Accept: application/json'
```

### Tech tree by level

```bash
curl -X 'GET' \
  'http://127.0.0.1/tech/?level=10&page=1&size=50' \
  -H 'Accept: application/json'
```

### Build objects by category

```bash
curl -X 'GET' \
  'http://127.0.0.1/build/?category=Food&lang=en&page=1&size=50' \
  -H 'Accept: application/json'
```

### Full category pagination

```bash
curl -X 'GET' \
  'http://127.0.0.1/all/pals?page=1&size=50&lang=en' \
  -H 'Accept: application/json'
```

### Map locations

```bash
curl -X 'GET' \
  'http://127.0.0.1/map-locations/?category=fast_travel&map=world&page=1&size=50' \
  -H 'Accept: application/json'
```

### Autocomplete

```bash
curl -X 'GET' \
  'http://127.0.0.1/autocomplete/palname/?name=La&page=1&size=25' \
  -H 'Accept: application/json'
```

### Skill autocomplete with localization

```bash
curl -X 'GET' \
  'http://127.0.0.1/autocomplete/skill/?name=龙&lang=zh-Hans&page=1&size=25' \
  -H 'Accept: application/json'
```

### NPC autocomplete

```bash
curl -X 'GET' \
  'http://127.0.0.1/autocomplete/npc/?name=Wan&page=1&size=25' \
  -H 'Accept: application/json'
```

### Health check

```bash
curl -X 'GET' \
  'http://127.0.0.1/health' \
  -H 'Accept: application/json'
```

## Data Routes With OAuth

These are a small sample of the same data endpoints shown above, this time with the auth header required when `COMPOSE_PROFILES=USE_OAUTH2`. The other data-route examples above also support `Authorization: Bearer ACCESS-TOKEN` when OAuth is enabled.

> [!IMPORTANT]
> The examples in this section are only samples. The other data-route examples above also become protected when OAuth is enabled.

### Pals with Bearer token

```bash
curl -X 'GET' \
  'http://127.0.0.1/pals/?name=Lamball&page=1&size=50' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer ACCESS-TOKEN'
```

### Map locations with Bearer token

```bash
curl -X 'GET' \
  'http://127.0.0.1/map-locations/?category=fast_travel&map=world&page=1&size=50' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer ACCESS-TOKEN'
```

## OAuth Routes

These routes are available when `COMPOSE_PROFILES=USE_OAUTH2`.

> [!WARNING]
> `/oauth2/validate` does not use the normal Bearer format. It expects `Authorization: OAuth ACCESS-TOKEN`.

### Login

```bash
curl -X 'POST' \
  'http://127.0.0.1/oauth2/login/' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'username=Bob123&password=SomePass'
```

### Refresh an access token

```bash
curl -X 'POST' \
  'http://127.0.0.1/oauth2/refresh/' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'token=REFRESH-TOKEN&grant_type=refresh_token'
```

### Validate access token

```bash
curl -X 'GET' \
  'http://127.0.0.1/oauth2/validate' \
  -H 'Accept: application/json' \
  -H 'Authorization: OAuth ACCESS-TOKEN'
```

## User Routes

### Current user

```bash
curl -X 'GET' \
  'http://127.0.0.1/user/me/' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer ACCESS-TOKEN'
```

### Change your password

```bash
curl -X 'PUT' \
  'http://127.0.0.1/user/changepassword/' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer ACCESS-TOKEN' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'current_password=OldPass&new_password=NewPass'
```

## Admin Routes

### Add user

```bash
curl -X 'POST' \
  'http://127.0.0.1/admin/adduser/' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer ACCESS-TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
        "username": "Bob123",
        "password": "SomePass",
        "scopes": ["APIUser:Read", "APIUser:ChangePassword"],
        "disabled": false
      }'
```

### List users

```bash
curl -X 'GET' \
  'http://127.0.0.1/admin/users/?page=1&size=50' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer ACCESS-TOKEN'
```

### Change a user's scopes

```bash
curl -X 'PUT' \
  'http://127.0.0.1/admin/chscope/' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer ACCESS-TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
        "username": "Bob123",
        "scopes": ["APIUser:Read", "APIUser:ChangePassword"]
      }'
```
