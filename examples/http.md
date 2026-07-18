# HTTP Examples

## Data Routes

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

### Health check

```bash
curl -X 'GET' \
  'http://127.0.0.1/health' \
  -H 'Accept: application/json'
```

## OAuth Routes

These routes are available when `COMPOSE_PROFILES=USE_OAUTH2`.

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

## Protected Route Example

```bash
curl -X 'GET' \
  'http://127.0.0.1/pals/?name=Lamball&page=1&size=50' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer ACCESS-TOKEN'
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
