# Examples

This folder contains longer usage examples in case you want ready-to-run API references even when `/docs` and `/redoc` are disabled.

## Files

- [http.md](http.md): `curl` examples for data routes, localization, OAuth, user, and admin flows.
- [python.md](python.md): `aiohttp` examples for the same route groups.

## Base URL

Examples use:

```text
http://127.0.0.1
```

If your API is running on another host or port, replace that base URL accordingly. For a custom port, use a base URL such as `http://127.0.0.1:8000`.

## Localization

- Default language: `en`
- Included localized language code: `zh-Hans` (Simplified Chinese)

Example:

```text
/pals/?name=棉悠悠&lang=zh-Hans
```

## Notes

> [!IMPORTANT]
> If `COMPOSE_PROFILES=USE_OAUTH2`, data routes require `Authorization: Bearer ACCESS-TOKEN`.

- Data-route examples work whether OAuth is enabled or disabled.
- OAuth, user, and admin examples apply only when `COMPOSE_PROFILES=USE_OAUTH2`.
- When OAuth is enabled, the same data routes shown in these examples require `Authorization: Bearer ACCESS-TOKEN`.
- `map-locations` currently uses `map=world` or `map=tree`.
- Current shipped `map-locations` categories are `dungeon`, `fast_travel`, `lifmunk_effigy`, `note`, `tower`, and `treasure_map`.
- Most protected routes use `Authorization: Bearer ACCESS-TOKEN`.
- `/oauth2/validate` is a special case and expects `Authorization: OAuth ACCESS-TOKEN`.
- `/breeding/` still accepts the legacy `name` query parameter as an alias for `egg`, but it is deprecated in the shipped API and will be removed in a future version.
- `skill` autocomplete supports localized Pal skill names when a supported `lang` value is supplied.
- `npc` autocomplete is available again in the current shipped query behavior.
- `/passive/` accepts `lang`, but passive skill lookups currently return the default English passive skill data.
