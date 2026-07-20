"""Store OpenAPI description metadata."""

description = """
A Palworld data API for apps and bots, with pals, items, breeding, and optional OAuth2.

### Note: _Some Null items will not be in json response_

_Parsed game data v1.0.1.100619_

"""

tags_metadata = [
    {"name": "Pals", "description": "All your Pals info."},
    {
        "name": "Items",
        "description": "All your Game items info.",
    },
    {
        "name": "Misc",
        "description": "Miscellaneous.",
    },
    {
        "name": "AutoComplete",
        "description": "Discord bots AutoComplete helper.",
    },
]

oauth_tags_metadata = [
    {"name": "Pals", "description": "All your Pals info."},
    {
        "name": "Items",
        "description": "All your Game items info.",
    },
    {
        "name": "Misc",
        "description": "Miscellaneous.",
    },
    {
        "name": "AutoComplete",
        "description": "Discord bots AutoComplete helper.",
    },
    {
        "name": "User",
        "description": "Users section.",
    },
    {
        "name": "Auth",
        "description": "oAuth2 section.",
    },
    {
        "name": "Admin",
        "description": "Admin for user database.",
    },
]
