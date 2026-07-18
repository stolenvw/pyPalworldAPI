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

If your API is running on another host or port, replace that base URL accordingly.

## Localization

- Default language: `en`
- Included localized language code: `zh-Hans` (Simplified Chinese)

Example:

```text
/pals/?name=棉悠悠&lang=zh-Hans
```

## Notes

- Most protected routes use `Authorization: Bearer ACCESS-TOKEN`.
- `/oauth2/validate` is a special case and expects `Authorization: OAuth ACCESS-TOKEN`.
- `skill` autocomplete supports localized Pal skill names when a supported `lang` value is supplied.
- `npc` autocomplete is available again in the current shipped query behavior.
- `/passive/` accepts `lang`, but passive skill lookups currently return the default English passive skill data.
