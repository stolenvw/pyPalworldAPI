class pyPalworldAPIExamples:
    pals = [
        {
            "lang": "Curl",
            "source": """curl -X 'GET' \ 
    'http://127.0.0.0/pals/?name=lamball&page=1&size=50' \ 
    -H 'Accept: application/json'""",
            "label": "Curl",
        },
        {
            "lang": "Python",
            "source": """import asyncio
import json

import aiohttp
from aiohttp.client_exceptions import ClientConnectorError


async def get_pals(name: str):
    url = "http://127.0.0.0/pals/"
    headers = {
        "Accept": "application/json",
    }
    params = {"name": name, "page": 1, "size": 50}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as result:
                data = await result.json()
    except ClientConnectorError as e:
        print(f"ClientConnectorError: {e}")
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    asyncio.run(get_pals(name="lamball"))""",
            "label": "Python",
        },
        {
            "lang": "Curl",
            "source": """curl -X 'GET' \ 
    'http://127.0.0.0/pals/?name=lamball&page=1&size=50' \ 
    -H 'Accept: application/json' \ 
    -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'""",
            "label": "Curl OAuth",
        },
        {
            "lang": "Python",
            "source": """import asyncio
import json

import aiohttp
from aiohttp.client_exceptions import ClientConnectorError


async def get_pals(name: str, access_token: str):
    url = "http://127.0.0.0/pals/"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
    }
    params = {"name": name, "page": 1, "size": 50}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as result:
                data = await result.json()
    except ClientConnectorError as e:
        print(f"ClientConnectorError: {e}")
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    asyncio.run(
        get_pals(name="lamball", access_token="kajfe0983qjaf309ajj3w8j3aij3a3")
    )""",
            "label": "Python OAuth",
        },
    ]

    boss_pals = [
        {
            "lang": "Curl",
            "source": """curl -X 'GET' \ 
    'http://127.0.0.0/bosspals/?name=Mammorest&page=1&size=50' \ 
    -H 'Accept: application/json'""",
            "label": "Curl",
        },
        {
            "lang": "Python",
            "source": """import asyncio
import json

import aiohttp
from aiohttp.client_exceptions import ClientConnectorError


async def get_bosspals(name: str):
    url = "http://127.0.0.0/bosspals/"
    headers = {
        "Accept": "application/json",
    }
    params = {"name": name, "page": 1, "size": 50}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as result:
                data = await result.json()
    except ClientConnectorError as e:
        print(f"ClientConnectorError: {e}")
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    asyncio.run(get_bosspals(name="Mammorest"))""",
            "label": "Python",
        },
        {
            "lang": "Curl",
            "source": """curl -X 'GET' \ 
    'http://127.0.0.0/bosspals/?name=Mammorest&page=1&size=50' \ 
    -H 'Accept: application/json' \ 
    -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'""",
            "label": "Curl OAuth",
        },
        {
            "lang": "Python",
            "source": """import asyncio
import json

import aiohttp
from aiohttp.client_exceptions import ClientConnectorError


async def get_bosspals(name: str, access_token: str):
    url = "http://127.0.0.0/bosspals/"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
    }
    params = {"name": name, "page": 1, "size": 50}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as result:
                data = await result.json()
    except ClientConnectorError as e:
        print(f"ClientConnectorError: {e}")
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    asyncio.run(
        get_bosspals(name="Mammorest", access_token="kajfe0983qjaf309ajj3w8j3aij3a3")
    )""",
            "label": "Python OAuth",
        },
    ]

    breeding = [
        {
            "lang": "Curl",
            "source": """curl -X 'GET' \ 
    'http://127.0.0.0/breeding/?name=Anubis&page=1&size=50' \ 
    -H 'Accept: application/json'""",
            "label": "Curl",
        },
        {
            "lang": "Python",
            "source": """import asyncio
import json

import aiohttp
from aiohttp.client_exceptions import ClientConnectorError


async def get_breeding(name: str):
    url = "http://127.0.0.0/breeding/"
    headers = {
        "Accept": "application/json",
    }
    params = {"name": name, "page": 1, "size": 50}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as result:
                data = await result.json()
    except ClientConnectorError as e:
        print(f"ClientConnectorError: {e}")
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    asyncio.run(get_breeding(name="Anubis"))""",
            "label": "Python",
        },
        {
            "lang": "Curl",
            "source": """curl -X 'GET' \ 
    'http://127.0.0.0/breeding/?name=Anubis&page=1&size=50' \ 
    -H 'Accept: application/json' \ 
    -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'""",
            "label": "Curl OAuth",
        },
        {
            "lang": "Python",
            "source": """import asyncio
import json

import aiohttp
from aiohttp.client_exceptions import ClientConnectorError


async def get_breeding(name: str, access_token: str):
    url = "http://127.0.0.0/breeding/"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
    }
    params = {"name": name, "page": 1, "size": 50}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as result:
                data = await result.json()
    except ClientConnectorError as e:
        print(f"ClientConnectorError: {e}")
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    asyncio.run(
        get_breeding(name="Anubis", access_token="kajfe0983qjaf309ajj3w8j3aij3a3")
    )""",
            "label": "Python OAuth",
        },
    ]

    sickness = [
        {
            "lang": "Curl",
            "source": """curl -X 'GET' \ 
    'http://127.0.0.0/sickness/?name=ulcer&page=1&size=50' \ 
    -H 'Accept: application/json'""",
            "label": "Curl",
        },
        {
            "lang": "Python",
            "source": """import asyncio
import json

import aiohttp
from aiohttp.client_exceptions import ClientConnectorError


async def get_sickness(name: str):
    url = "http://127.0.0.0/sickness/"
    headers = {
        "Accept": "application/json",
    }
    params = {"name": name, "page": 1, "size": 50}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as result:
                data = await result.json()
    except ClientConnectorError as e:
        print(f"ClientConnectorError: {e}")
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    asyncio.run(get_sickness(name="ulcer"))""",
            "label": "Python",
        },
        {
            "lang": "Curl",
            "source": """curl -X 'GET' \ 
    'http://127.0.0.0/sickness/?name=ulcer&page=1&size=50' \ 
    -H 'Accept: application/json' \ 
    -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'""",
            "label": "Curl OAuth",
        },
        {
            "lang": "Python",
            "source": """import asyncio
import json

import aiohttp
from aiohttp.client_exceptions import ClientConnectorError


async def get_sickness(name: str, access_token: str):
    url = "http://127.0.0.0/sickness/"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
    }
    params = {"name": name, "page": 1, "size": 50}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as result:
                data = await result.json()
    except ClientConnectorError as e:
        print(f"ClientConnectorError: {e}")
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    asyncio.run(
        get_sickness(name="ulcer", access_token="kajfe0983qjaf309ajj3w8j3aij3a3")
    )""",
            "label": "Python OAuth",
        },
    ]

    items = [
        {
            "lang": "Curl",
            "source": """curl -X 'GET' \ 
    'http://127.0.0.0/items/?name=arrow&page=1&size=50' \ 
    -H 'Accept: application/json'""",
            "label": "Curl",
        },
        {
            "lang": "Python",
            "source": """import asyncio
import json

import aiohttp
from aiohttp.client_exceptions import ClientConnectorError


async def get_items(name: str):
    url = "http://127.0.0.0/items/"
    headers = {
        "Accept": "application/json",
    }
    params = {"name": name, "page": 1, "size": 50}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as result:
                data = await result.json()
    except ClientConnectorError as e:
        print(f"ClientConnectorError: {e}")
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    asyncio.run(get_items(name="arrow"))""",
            "label": "Python",
        },
        {
            "lang": "Curl",
            "source": """curl -X 'GET' \ 
    'http://127.0.0.0/items/?name=arrow&page=1&size=50' \ 
    -H 'Accept: application/json' \ 
    -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'""",
            "label": "Curl OAuth",
        },
        {
            "lang": "Python",
            "source": """import asyncio
import json

import aiohttp
from aiohttp.client_exceptions import ClientConnectorError


async def get_items(name: str, access_token: str):
    url = "http://127.0.0.0/items/"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
    }
    params = {"name": name, "page": 1, "size": 50}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as result:
                data = await result.json()
    except ClientConnectorError as e:
        print(f"ClientConnectorError: {e}")
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    asyncio.run(get_items(name="arrow", access_token="kajfe0983qjaf309ajj3w8j3aij3a3"))""",
            "label": "Python OAuth",
        },
    ]

    crafting = [
        {
            "lang": "Curl",
            "source": """curl -X 'GET' \ 
    'http://127.0.0.0/crafting/?name=arrow&page=1&size=50' \ 
    -H 'Accept: application/json'""",
            "label": "Curl",
        },
        {
            "lang": "Python",
            "source": """import asyncio
import json

import aiohttp
from aiohttp.client_exceptions import ClientConnectorError


async def get_crafting(name: str):
    url = "http://127.0.0.0/crafting/"
    headers = {
        "Accept": "application/json",
    }
    params = {"name": name, "page": 1, "size": 50}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as result:
                data = await result.json()
    except ClientConnectorError as e:
        print(f"ClientConnectorError: {e}")
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    asyncio.run(get_crafting(name="arrow"))""",
            "label": "Python",
        },
        {
            "lang": "Curl",
            "source": """curl -X 'GET' \ 
    'http://127.0.0.0/crafting/?name=arrow&page=1&size=50' \ 
    -H 'Accept: application/json' \ 
    -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'""",
            "label": "Curl OAuth",
        },
        {
            "lang": "Python",
            "source": """import asyncio
import json

import aiohttp
from aiohttp.client_exceptions import ClientConnectorError


async def get_crafting(name: str, access_token: str):
    url = "http://127.0.0.0/crafting/"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
    }
    params = {"name": name, "page": 1, "size": 50}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as result:
                data = await result.json()
    except ClientConnectorError as e:
        print(f"ClientConnectorError: {e}")
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    asyncio.run(
        get_crafting(name="arrow", access_token="kajfe0983qjaf309ajj3w8j3aij3a3")
    )""",
            "label": "Python OAuth",
        },
    ]

    gear = [
        {
            "lang": "Curl",
            "source": """curl -X 'GET' \ 
    'http://127.0.0.0/gear/?name=cloth%20outfit&page=1&size=50' \ 
    -H 'Accept: application/json'""",
            "label": "Curl",
        },
        {
            "lang": "Python",
            "source": """import asyncio
import json

import aiohttp
from aiohttp.client_exceptions import ClientConnectorError


async def get_gear(name: str):
    url = "http://127.0.0.0/gear/"
    headers = {
        "Accept": "application/json",
    }
    params = {"name": name, "page": 1, "size": 50}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as result:
                data = await result.json()
    except ClientConnectorError as e:
        print(f"ClientConnectorError: {e}")
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    asyncio.run(get_gear(name="cloth outfit"))""",
            "label": "Python",
        },
        {
            "lang": "Curl",
            "source": """curl -X 'GET' \ 
    'http://127.0.0.0/gear/?name=cloth%20outfit&page=1&size=50' \ 
    -H 'Accept: application/json' \ 
    -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'""",
            "label": "Curl OAuth",
        },
        {
            "lang": "Python",
            "source": """import asyncio
import json

import aiohttp
from aiohttp.client_exceptions import ClientConnectorError


async def get_gear(name: str, access_token: str):
    url = "http://127.0.0.0/gear/"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
    }
    params = {"name": name, "page": 1, "size": 50}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as result:
                data = await result.json()
    except ClientConnectorError as e:
        print(f"ClientConnectorError: {e}")
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    asyncio.run(
        get_gear(name="cloth outfit", access_token="kajfe0983qjaf309ajj3w8j3aij3a3")
    )""",
            "label": "Python OAuth",
        },
    ]

    foodeffect = [
        {
            "lang": "Curl",
            "source": """curl -X 'GET' \ 
    'http://127.0.0.0/foodeffect/?name=salad&page=1&size=50' \ 
    -H 'Accept: application/json'""",
            "label": "Curl",
        },
        {
            "lang": "Python",
            "source": """import asyncio
import json

import aiohttp
from aiohttp.client_exceptions import ClientConnectorError


async def get_foodeffect(name: str):
    url = "http://127.0.0.0/foodeffect/"
    headers = {
        "Accept": "application/json",
    }
    params = {"name": name, "page": 1, "size": 50}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as result:
                data = await result.json()
    except ClientConnectorError as e:
        print(f"ClientConnectorError: {e}")
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    asyncio.run(get_foodeffect(name="salad"))""",
            "label": "Python",
        },
        {
            "lang": "Curl",
            "source": """curl -X 'GET' \ 
    'http://127.0.0.0/foodeffect/?name=salad&page=1&size=50' \ 
    -H 'Accept: application/json' \ 
    -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'""",
            "label": "Curl OAuth",
        },
        {
            "lang": "Python",
            "source": """import asyncio
import json

import aiohttp
from aiohttp.client_exceptions import ClientConnectorError


async def get_foodeffect(name: str, access_token: str):
    url = "http://127.0.0.0/foodeffect/"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
    }
    params = {"name": name, "page": 1, "size": 50}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as result:
                data = await result.json()
    except ClientConnectorError as e:
        print(f"ClientConnectorError: {e}")
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    asyncio.run(
        get_foodeffect(name="salad", access_token="kajfe0983qjaf309ajj3w8j3aij3a3")
    )""",
            "label": "Python OAuth",
        },
    ]

    tech = [
        {
            "lang": "Curl",
            "source": """curl -X 'GET' \ 
    'http://127.0.0.0/tech/?name=Nail&page=1&size=50' \ 
    -H 'Accept: application/json'""",
            "label": "Curl",
        },
        {
            "lang": "Python",
            "source": """import asyncio
import json

import aiohttp
from aiohttp.client_exceptions import ClientConnectorError


async def get_tech(name: str):
    url = "http://127.0.0.0/tech/"
    headers = {
        "Accept": "application/json",
    }
    params = {"name": name, "page": 1, "size": 50}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as result:
                data = await result.json()
    except ClientConnectorError as e:
        print(f"ClientConnectorError: {e}")
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    asyncio.run(get_tech(name="Nail"))""",
            "label": "Python",
        },
        {
            "lang": "Curl",
            "source": """curl -X 'GET' \ 
    'http://127.0.0.0/tech/?name=Nail&page=1&size=50' \ 
    -H 'Accept: application/json' \ 
    -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'""",
            "label": "Curl OAuth",
        },
        {
            "lang": "Python",
            "source": """import asyncio
import json

import aiohttp
from aiohttp.client_exceptions import ClientConnectorError


async def get_tech(name: str, access_token: str):
    url = "http://127.0.0.0/tech/"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
    }
    params = {"name": name, "page": 1, "size": 50}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as result:
                data = await result.json()
    except ClientConnectorError as e:
        print(f"ClientConnectorError: {e}")
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    asyncio.run(get_tech(name="Nail", access_token="kajfe0983qjaf309ajj3w8j3aij3a3"))""",
            "label": "Python OAuth",
        },
    ]

    build = [
        {
            "lang": "Curl",
            "source": """curl -X 'GET' \ 
    'http://127.0.0.0/build/?name=Campfire&page=1&size=50' \ 
    -H 'Accept: application/json'""",
            "label": "Curl",
        },
        {
            "lang": "Python",
            "source": """import asyncio
import json

import aiohttp
from aiohttp.client_exceptions import ClientConnectorError


async def get_build(name: str):
    url = "http://127.0.0.0/build/"
    headers = {
        "Accept": "application/json",
    }
    params = {"name": name, "page": 1, "size": 50}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as result:
                data = await result.json()
    except ClientConnectorError as e:
        print(f"ClientConnectorError: {e}")
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    asyncio.run(get_build(name="Campfire"))""",
            "label": "Python",
        },
        {
            "lang": "Curl",
            "source": """curl -X 'GET' \ 
    'http://127.0.0.0/build/?name=Campfire&page=1&size=50' \ 
    -H 'Accept: application/json' \ 
    -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'""",
            "label": "Curl OAuth",
        },
        {
            "lang": "Python",
            "source": """import asyncio
import json

import aiohttp
from aiohttp.client_exceptions import ClientConnectorError


async def get_build(name: str, access_token: str):
    url = "http://127.0.0.0/build/"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
    }
    params = {"name": name, "page": 1, "size": 50}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as result:
                data = await result.json()
    except ClientConnectorError as e:
        print(f"ClientConnectorError: {e}")
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    asyncio.run(
        get_build(name="Campfire", access_token="kajfe0983qjaf309ajj3w8j3aij3a3")
    )""",
            "label": "Python OAuth",
        },
    ]

    passive = [
        {
            "lang": "Curl",
            "source": """curl -X 'GET' \ 
    'http://127.0.0.0/passive/?name=Brave&page=1&size=50' \ 
    -H 'Accept: application/json'""",
            "label": "Curl",
        },
        {
            "lang": "Python",
            "source": """import asyncio
import json

import aiohttp
from aiohttp.client_exceptions import ClientConnectorError


async def get_passive(name: str):
    url = "http://127.0.0.0/passive/"
    headers = {
        "Accept": "application/json",
    }
    params = {"name": name, "page": 1, "size": 50}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as result:
                data = await result.json()
    except ClientConnectorError as e:
        print(f"ClientConnectorError: {e}")
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    asyncio.run(get_passive(name="Brave"))""",
            "label": "Python",
        },
        {
            "lang": "Curl",
            "source": """curl -X 'GET' \ 
    'http://127.0.0.0/passive/?name=Brave&page=1&size=50' \ 
    -H 'Accept: application/json' \ 
    -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'""",
            "label": "Curl OAuth",
        },
        {
            "lang": "Python",
            "source": """import asyncio
import json

import aiohttp
from aiohttp.client_exceptions import ClientConnectorError


async def get_passive(name: str, access_token: str):
    url = "http://127.0.0.0/passive/"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
    }
    params = {"name": name, "page": 1, "size": 50}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as result:
                data = await result.json()
    except ClientConnectorError as e:
        print(f"ClientConnectorError: {e}")
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    asyncio.run(
        get_passive(name="Brave", access_token="kajfe0983qjaf309ajj3w8j3aij3a3")
    )""",
            "label": "Python OAuth",
        },
    ]

    npc = [
        {
            "lang": "Curl",
            "source": """curl -X 'GET' \ 
    'http://127.0.0.0/npc/?name=Wandering%20Merchant&page=1&size=50' \ 
    -H 'Accept: application/json'""",
            "label": "Curl",
        },
        {
            "lang": "Python",
            "source": """import asyncio
import json

import aiohttp
from aiohttp.client_exceptions import ClientConnectorError


async def get_npc(name: str):
    url = "http://127.0.0.0/npc/"
    headers = {
        "Accept": "application/json",
    }
    params = {"name": name, "page": 1, "size": 50}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as result:
                data = await result.json()
    except ClientConnectorError as e:
        print(f"ClientConnectorError: {e}")
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    asyncio.run(get_npc(name="Wandering Merchant"))""",
            "label": "Python",
        },
        {
            "lang": "Curl",
            "source": """curl -X 'GET' \ 
    'http://127.0.0.0/npc/?name=Wandering%20Merchant&page=1&size=50' \ 
    -H 'Accept: application/json' \ 
    -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'""",
            "label": "Curl OAuth",
        },
        {
            "lang": "Python",
            "source": """import asyncio
import json

import aiohttp
from aiohttp.client_exceptions import ClientConnectorError


async def get_npc(name: str, access_token: str):
    url = "http://127.0.0.0/npc/"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
    }
    params = {"name": name, "page": 1, "size": 50}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as result:
                data = await result.json()
    except ClientConnectorError as e:
        print(f"ClientConnectorError: {e}")
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    asyncio.run(
        get_npc(
            name="Wandering Merchant", access_token="kajfe0983qjaf309ajj3w8j3aij3a3"
        )
    )""",
            "label": "Python OAuth",
        },
    ]

    elixir = [
        {
            "lang": "Curl",
            "source": """curl -X 'GET' \ 
    'http://127.0.0.0/elixir/?name=Speed%20Elixir&page=1&size=50' \ 
    -H 'Accept: application/json'""",
            "label": "Curl",
        },
        {
            "lang": "Python",
            "source": """import asyncio
import json

import aiohttp
from aiohttp.client_exceptions import ClientConnectorError


async def get_elixir(name: str):
    url = "http://127.0.0.0/elixir/"
    headers = {
        "Accept": "application/json",
    }
    params = {"name": name, "page": 1, "size": 50}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as result:
                data = await result.json()
    except ClientConnectorError as e:
        print(f"ClientConnectorError: {e}")
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    asyncio.run(get_elixir(name="Speed Elixir"))""",
            "label": "Python",
        },
        {
            "lang": "Curl",
            "source": """curl -X 'GET' \ 
    'http://127.0.0.0/elixir/?name=Speed%20Elixir&page=1&size=50' \ 
    -H 'Accept: application/json' \ 
    -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'""",
            "label": "Curl OAuth",
        },
        {
            "lang": "Python",
            "source": """import asyncio
import json

import aiohttp
from aiohttp.client_exceptions import ClientConnectorError


async def get_elixir(name: str, access_token: str):
    url = "http://127.0.0.0/elixir/"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
    }
    params = {"name": name, "page": 1, "size": 50}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as result:
                data = await result.json()
    except ClientConnectorError as e:
        print(f"ClientConnectorError: {e}")
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    asyncio.run(
        get_elixir(
            name="Speed Elixir", access_token="kajfe0983qjaf309ajj3w8j3aij3a3"
        )
    )""",
            "label": "Python OAuth",
        },
    ]

    alls = [
        {
            "lang": "Curl",
            "source": """curl -X 'GET' \ 
    'http://127.0.0.0/all/pals?page=1&size=50' \ 
    -H 'Accept: application/json'""",
            "label": "Curl",
        },
        {
            "lang": "Python",
            "source": """import asyncio
import json

import aiohttp
from aiohttp.client_exceptions import ClientConnectorError


async def get_all(category: str):
    url = f"http://127.0.0.0/all/{category}"
    headers = {
        "Accept": "application/json",
    }
    params = {"page": 1, "size": 50}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as result:
                data = await result.json()
    except ClientConnectorError as e:
        print(f"ClientConnectorError: {e}")
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    asyncio.run(get_all(category="pals"))""",
            "label": "Python",
        },
        {
            "lang": "Curl",
            "source": """curl -X 'GET' \ 
    'http://127.0.0.0/all/pals?page=1&size=50' \ 
    -H 'Accept: application/json' \ 
    -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'""",
            "label": "Curl OAuth",
        },
        {
            "lang": "Python",
            "source": """import asyncio
import json

import aiohttp
from aiohttp.client_exceptions import ClientConnectorError


async def get_all(category: str, access_token: str):
    url = f"http://127.0.0.0/all/{category}"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
    }
    params = {"page": 1, "size": 50}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as result:
                data = await result.json()
    except ClientConnectorError as e:
        print(f"ClientConnectorError: {e}")
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    asyncio.run(
        get_all(category="pals", access_token="kajfe0983qjaf309ajj3w8j3aij3a3")
    )""",
            "label": "Python OAuth",
        },
    ]

    autocomplete = [
        {
            "lang": "Curl",
            "source": """curl -X 'GET' \ 
    'http://127.0.0.0/autocomplete/palname/?name=la&page=1&size=25' \ 
    -H 'Accept: application/json'""",
            "label": "Curl",
        },
        {
            "lang": "Python",
            "source": """import asyncio
import json

import aiohttp
from aiohttp.client_exceptions import ClientConnectorError


async def get_autocomplete(category: str, name: str):
    url = f"http://127.0.0.0/autocomplete/{category}"
    headers = {
        "Accept": "application/json",
    }
    params = {"name": name, "page": 1, "size": 25}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as result:
                data = await result.json()
    except ClientConnectorError as e:
        print(f"ClientConnectorError: {e}")
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    asyncio.run(get_autocomplete(category="palname", name="la"))""",
            "label": "Python",
        },
        {
            "lang": "Curl",
            "source": """curl -X 'GET' \ 
    'http://127.0.0.0/autocomplete/palname/?name=la&page=1&size=25' \ 
    -H 'Accept: application/json' \ 
    -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'""",
            "label": "Curl OAuth",
        },
        {
            "lang": "Python",
            "source": """import asyncio
import json

import aiohttp
from aiohttp.client_exceptions import ClientConnectorError


async def get_autocomplete(category: str, name: str, access_token: str):
    url = f"http://127.0.0.0/autocomplete/{category}"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
    }
    params = {"name": name, "page": 1, "size": 25}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as result:
                data = await result.json()
    except ClientConnectorError as e:
        print(f"ClientConnectorError: {e}")
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    asyncio.run(
        get_autocomplete(
            category="palname", name="la", access_token="kajfe0983qjaf309ajj3w8j3aij3a3"
        )
    )""",
            "label": "Python OAuth",
        },
    ]

    login = [
        {
            "lang": "Curl",
            "source": """curl -X 'POST' \ 
    'http://127.0.0.0/oauth2/login/' \ 
    -H 'Accept: application/json' \ 
    -H 'Content-Type: application/x-www-form-urlencoded' \ 
    -d 'username=Bob123&password=SomePass'""",
            "label": "Curl",
        },
        {
            "lang": "Python",
            "source": """import asyncio
import json

import aiohttp
from aiohttp.client_exceptions import ClientConnectorError


async def post_login(username: str, password: str):
    url = f"http://127.0.0.0/oauth2/login/"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    body = {"username": username, "password": password}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, data=body) as result:
                data = await result.json()
    except ClientConnectorError as e:
        print(f"ClientConnectorError: {e}")
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    asyncio.run(post_login(username="Bob123", password="SomePass"))""",
            "label": "Python",
        },
    ]

    refresh = [
        {
            "lang": "Curl",
            "source": """curl -X 'POST' \ 
    'http://127.0.0.0/oauth2/refresh/' \ 
    -H 'Accept: application/json' \ 
    -H 'Content-Type: application/x-www-form-urlencoded' \ 
    -d 'token=kafaj083209jq904j8qjiaf39&grant_type=refresh_token'""",
            "label": "Curl",
        },
        {
            "lang": "Python",
            "source": """import asyncio
import json

import aiohttp
from aiohttp.client_exceptions import ClientConnectorError


async def post_refresh(refresh_token: str):
    url = f"http://127.0.0.0/oauth2/refresh/"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    body = {"token": refresh_token, "grant_type": "refresh_token"}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, data=body) as result:
                data = await result.json()
    except ClientConnectorError as e:
        print(f"ClientConnectorError: {e}")
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    asyncio.run(post_refresh(refresh_token="kafaj083209jq904j8qjiaf39"))""",
            "label": "Python",
        },
    ]

    user_change_password = [
        {
            "lang": "Curl",
            "source": """curl -X 'PUT' \ 
    'http://127.0.0.0/user/changepassword/' \ 
    -H 'Accept: application/json' \ 
    -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3' \ 
    -H 'Content-Type: application/x-www-form-urlencoded' \ 
    -d 'current_password=SomePass&new_password=SomeNewPass'""",
            "label": "Curl",
        },
        {
            "lang": "Python",
            "source": """import asyncio
import json

import aiohttp
from aiohttp.client_exceptions import ClientConnectorError


async def put_user_change_password(
    current_password: str, new_password: str, access_token: str
):
    url = f"http://127.0.0.0/user/changepassword/"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    body = {"current_password": current_password, "new_password": new_password}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.put(url, headers=headers, data=body) as result:
                data = await result.json()
    except ClientConnectorError as e:
        print(f"ClientConnectorError: {e}")
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    asyncio.run(
        put_user_change_password(
            current_password="SomePass",
            new_password="SomeNewPass",
            access_token="kajfe0983qjaf309ajj3w8j3aij3a3",
        )
    )""",
            "label": "Python",
        },
    ]

    me = [
        {
            "lang": "Curl",
            "source": """curl -X 'GET' \ 
    'http://127.0.0.0/user/me/' \ 
    -H 'Accept: application/json' \ 
    -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'""",
            "label": "Curl",
        },
        {
            "lang": "Python",
            "source": """import asyncio
import json

import aiohttp
from aiohttp.client_exceptions import ClientConnectorError


async def get_user_me(access_token: str):
    url = f"http://127.0.0.0/user/me/"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
    }
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as result:
                data = await result.json()
    except ClientConnectorError as e:
        print(f"ClientConnectorError: {e}")
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    asyncio.run(get_user_me(access_token="kajfe0983qjaf309ajj3w8j3aij3a3"))""",
            "label": "Python",
        },
    ]

    add_user = [
        {
            "lang": "Curl",
            "source": """curl -X 'Post' \ 
    'http://127.0.0.0/admin/adduser/' \ 
    -H 'Accept: application/json' \ 
    -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3' \ 
    -H 'Content-Type: application/json' \ 
    -d '{
          "username": "Bob123",
          "password": "SomePass",
          "scopes": [
            "APIUser:Read",
            "APIUser:ChangePassword"
          ],
          "disabled": false
        }'""",
            "label": "Curl",
        },
        {
            "lang": "Python",
            "source": """import asyncio
import json

import aiohttp
from aiohttp.client_exceptions import ClientConnectorError


async def post_add_user(
    access_token: str, username: str, password: str, scopes: list, disabled: bool
):
    url = f"http://127.0.0.0/admin/adduser/"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    json_body = {
        "username": username,
        "password": password,
        "scopes": scopes,
        "disabled": disabled,
    }
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=json_body) as result:
                data = await result.json()
    except ClientConnectorError as e:
        print(f"ClientConnectorError: {e}")
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    asyncio.run(
        post_add_user(
            access_token="kajfe0983qjaf309ajj3w8j3aij3a3",
            username="Bob123",
            password="SomePass",
            scopes=["APIUser:Read", "APIUser:ChangePassword"],
            disabled=False,
        )
    )""",
            "label": "Python",
        },
    ]

    admin_change_password = [
        {
            "lang": "Curl",
            "source": """curl -X 'PUT' \ 
    'http://127.0.0.0/admin/chpass/' \ 
    -H 'Accept: application/json' \ 
    -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3' \ 
    -H 'Content-Type: application/x-www-form-urlencoded' \ 
    -d 'username=Bob123&new_password=SomeNewPass'""",
            "label": "Curl",
        },
        {
            "lang": "Python",
            "source": """import asyncio
import json

import aiohttp
from aiohttp.client_exceptions import ClientConnectorError


async def put_admin_change_password(
    username: str, new_password: str, access_token: str
):
    url = f"http://127.0.0.0/admin/chpass/"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    body = {"username": username, "new_password": new_password}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.put(url, headers=headers, data=body) as result:
                data = await result.json()
    except ClientConnectorError as e:
        print(f"ClientConnectorError: {e}")
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    asyncio.run(
        put_admin_change_password(
            username="Bob123",
            new_password="SomeNewPass",
            access_token="kajfe0983qjaf309ajj3w8j3aij3a3",
        )
    )""",
            "label": "Python",
        },
    ]

    delete_user = [
        {
            "lang": "Curl",
            "source": """curl -X 'PUT' \ 
    'http://127.0.0.0/admin/deleteuser/?username=Bob123' \ 
    -H 'Accept: application/json' \ 
    -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'""",
            "label": "Curl",
        },
        {
            "lang": "Python",
            "source": """import asyncio
import json

import aiohttp
from aiohttp.client_exceptions import ClientConnectorError


async def delete_admin_delete_user(access_token: str, username: str):
    url = "http://127.0.0.0/admin/deleteuser/"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
    }
    params = {"username": username}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.delete(url, headers=headers, params=params) as result:
                data = await result.json()
    except ClientConnectorError as e:
        print(f"ClientConnectorError: {e}")
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    asyncio.run(
        delete_admin_delete_user(
            access_token="kajfe0983qjaf309ajj3w8j3aij3a3", username="Bob123"
        )
    )""",
            "label": "Python",
        },
    ]

    list_users = [
        {
            "lang": "Curl",
            "source": """curl -X 'GET' \ 
    'http://127.0.0.0/admin/users/?page=1&size=50' \ 
    -H 'Accept: application/json' \ 
    -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'""",
            "label": "Curl",
        },
        {
            "lang": "Python",
            "source": """import asyncio
import json

import aiohttp
from aiohttp.client_exceptions import ClientConnectorError


async def get_admin_users(access_token: str):
    url = "http://127.0.0.0/admin/users/"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
    }
    params = {"page": 1, "size": 50}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as result:
                data = await result.json()
    except ClientConnectorError as e:
        print(f"ClientConnectorError: {e}")
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    asyncio.run(get_admin_users(access_token="kajfe0983qjaf309ajj3w8j3aij3a3"))""",
            "label": "Python",
        },
    ]

    user_disable = [
        {
            "lang": "Curl",
            "source": """curl -X 'PUT' \ 
    'http://127.0.0.0/admin/userdisable/' \ 
    -H 'Accept: application/json' \ 
    -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3' \ 
    -H 'Content-Type: application/x-www-form-urlencoded' \ 
    -d 'username=Bob123&disabled=True'""",
            "label": "Curl",
        },
        {
            "lang": "Python",
            "source": """import asyncio
import json

import aiohttp
from aiohttp.client_exceptions import ClientConnectorError


async def put_admin_user_disable(access_token: str, username: str, disabled: bool):
    url = f"http://127.0.0.0/admin/userdisable/"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    body = {"username": username, "disabled": disabled}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.put(url, headers=headers, data=body) as result:
                data = await result.json()
    except ClientConnectorError as e:
        print(f"ClientConnectorError: {e}")
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    asyncio.run(
        put_admin_user_disable(
            access_token="kajfe0983qjaf309ajj3w8j3aij3a3",
            username="Bob123",
            disabled=True,
        )
    )""",
            "label": "Python",
        },
    ]

    change_scopes = [
        {
            "lang": "Curl",
            "source": """curl -X 'PUT' \ 
    'http://127.0.0.0/admin/chscope/' \ 
    -H 'Accept: application/json' \ 
    -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3' \ 
    -H 'Content-Type: application/json' \ 
    -d '{
          "username": "Bob123",
          "scopes": [
            "APIUser:Read",
            "APIUser:ChangePassword"
          ],
        }'""",
            "label": "Curl",
        },
        {
            "lang": "Python",
            "source": """import asyncio
import json

import aiohttp
from aiohttp.client_exceptions import ClientConnectorError


async def put_admin_change_scope(access_token: str, username: str, scopes: list):
    url = f"http://127.0.0.0/admin/chscope/"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    json_body = {
        "username": username,
        "scopes": scopes,
    }
    try:
        async with aiohttp.ClientSession() as session:
            async with session.put(url, headers=headers, json=json_body) as result:
                data = await result.json()
    except ClientConnectorError as e:
        print(f"ClientConnectorError: {e}")
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    asyncio.run(
        put_admin_change_scope(
            access_token="kajfe0983qjaf309ajj3w8j3aij3a3",
            username="Bob123",
            scopes=["APIUser:Read", "APIUser:ChangePassword"],
        )
    )""",
            "label": "Python",
        },
    ]

    validate = [
        {
            "lang": "Curl",
            "source": """curl -X 'GET' \ 
    'http://127.0.0.0/oauth2/validate' \ 
    -H 'Accept: application/json' \ 
    -H 'Authorization: OAuth kajfe0983qjaf309ajj3w8j3aij3a3'""",
            "label": "Curl",
        },
        {
            "lang": "Python",
            "source": """import asyncio
import json

import aiohttp
from aiohttp.client_exceptions import ClientConnectorError


async def get_user_me(access_token: str):
    url = "http://127.0.0.0/oauth2/validate"
    headers = {
        "Accept": "application/json",
        "Authorization": f"OAuth {access_token}",
    }
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as result:
                data = await result.json()
    except ClientConnectorError as e:
        print(f"ClientConnectorError: {e}")
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    asyncio.run(get_user_me(access_token="kajfe0983qjaf309ajj3w8j3aij3a3"))""",
            "label": "Python",
        },
    ]
