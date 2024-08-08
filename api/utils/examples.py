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

async def _get_pals(name: str):
  url = f"http://127.0.0.0/pals/?name={name}&page=1&size=50"
  headers = {
      "Accept": "application/json",
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
  asyncio.run(_get_pals(name="lamball"))""",
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

async def _get_pals(name:str, access_token: str):
  url = f"http://127.0.0.0/pals/?name={name}&page=1&size=50"
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
  asyncio.run(_get_pals(name="lamball", access_token="kajfe0983qjaf309ajj3w8j3aij3a3"))""",
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

async def _get_bosspals(name: str):
  url = f"http://127.0.0.0/bosspals/?name={name}&page=1&size=50"
  headers = {
      "Accept": "application/json",
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
  asyncio.run(_get_bosspals(name="Mammorest"))""",
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

async def _get_bosspals(name: str, access_token: str):
  url = f"http://127.0.0.0/bosspals/?name={name}&page=1&size=50"
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
  asyncio.run(_get_bosspals(name="Mammorest", access_token="kajfe0983qjaf309ajj3w8j3aij3a3"))""",
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

async def _get_breeding(name: str):
  url = f"http://127.0.0.0/breeding/?name={name}&page=1&size=50"
  headers = {
      "Accept": "application/json",
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
  asyncio.run(_get_breeding(name="Anubis"))""",
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

async def _get_breeding(name: str, access_token: str):
  url = f"http://127.0.0.0/breeding/?name={name}&page=1&size=50"
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
  asyncio.run(_get_breeding(name="Anubis", access_token="kajfe0983qjaf309ajj3w8j3aij3a3"))""",
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

async def _get_sickness(name: str):
  url = f"http://127.0.0.0/sickness/?name={name}&page=1&size=50"
  headers = {
      "Accept": "application/json",
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
  asyncio.run(_get_sickness(name="ulcer"))""",
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

async def _get_sickness(name: str, access_token: str):
  url = f"http://127.0.0.0/sickness/?name={name}&page=1&size=50"
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
  asyncio.run(_get_sickness(name="ulcer", access_token="kajfe0983qjaf309ajj3w8j3aij3a3"))""",
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

async def _get_items(name: str):
  url = f"http://127.0.0.0/items/?name={name}&page=1&size=50"
  headers = {
      "Accept": "application/json",
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
  asyncio.run(_get_items(name="arrow"))""",
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

async def _get_items(name: str, access_token: str):
  url = f"http://127.0.0.0/items/?name={name}&page=1&size=50"
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
  asyncio.run(_get_items(name="arrow", access_token="kajfe0983qjaf309ajj3w8j3aij3a3"))""",
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

async def _get_crafting(name: str):
  url = f"http://127.0.0.0/crafting/?name={name}&page=1&size=50"
  headers = {
      "Accept": "application/json",
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
  asyncio.run(_get_crafting(name="arrow"))""",
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

async def _get_crafting(name: str, access_token: str):
  url = f"http://127.0.0.0/crafting/?name={name}&page=1&size=50"
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
  asyncio.run(_get_crafting(name="arrow", access_token="kajfe0983qjaf309ajj3w8j3aij3a3"))""",
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

async def _get_gear(name: str):
  url = f"http://127.0.0.0/gear/?name={name}&page=1&size=50"
  headers = {
      "Accept": "application/json",
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
  asyncio.run(_get_gear(name="cloth%20outfit"))""",
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

async def _get_gear(name: str, access_token: str):
  url = f"http://127.0.0.0/gear/?name={name}&page=1&size=50"
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
  asyncio.run(_get_gear(name="cloth%20outfit", access_token="kajfe0983qjaf309ajj3w8j3aij3a3"))""",
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

async def _get_foodeffect(name: str):
  url = f"http://127.0.0.0/foodeffect/?name={name}&page=1&size=50"
  headers = {
      "Accept": "application/json",
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
  asyncio.run(_get_foodeffect(name="salad"))""",
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

async def _get_foodeffect(name: str, access_token: str):
  url = f"http://127.0.0.0/foodeffect/?name={name}&page=1&size=50"
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
  asyncio.run(_get_foodeffect(name="salad", access_token="kajfe0983qjaf309ajj3w8j3aij3a3"))""",
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

async def _get_tech(name: str):
  url = f"http://127.0.0.0/tech/?name={name}&page=1&size=50"
  headers = {
      "Accept": "application/json",
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
  asyncio.run(_get_tech(name="Nail"))""",
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

async def _get_tech(name: str, access_token: str):
  url = f"http://127.0.0.0/tech/?name={name}&page=1&size=50"
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
  asyncio.run(_get_tech(name="Nail", access_token="kajfe0983qjaf309ajj3w8j3aij3a3"))""",
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

async def _get_build(name: str):
  url = f"http://127.0.0.0/build/?name={name}&page=1&size=50"
  headers = {
      "Accept": "application/json",
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
  asyncio.run(_get_build(name="Campfire"))""",
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

async def _get_build(name: str, access_token: str):
  url = f"http://127.0.0.0/build/?name={name}&page=1&size=50"
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
  asyncio.run(_get_build(name="Campfire", access_token="kajfe0983qjaf309ajj3w8j3aij3a3"))""",
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

async def _get_passive(name: str):
  url = f"http://127.0.0.0/passive/?name={name}&page=1&size=50"
  headers = {
      "Accept": "application/json",
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
  asyncio.run(_get_passive(name="Brave"))""",
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

async def _get_passive(name: str, access_token: str):
  url = f"http://127.0.0.0/passive/?name={name}&page=1&size=50"
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
  asyncio.run(_get_passive(name="Brave", access_token="kajfe0983qjaf309ajj3w8j3aij3a3"))""",
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

async def _get_npc(name: str):
  url = f"http://127.0.0.0/npc/?name={name}&page=1&size=50"
  headers = {
      "Accept": "application/json",
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
  asyncio.run(_get_npc(name="Wandering%20Merchant"))""",
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

async def _get_npc(name: str, access_token: str):
  url = f"http://127.0.0.0/npc/?name={name}&page=1&size=50"
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
  asyncio.run(_get_npc(name="Wandering%20Merchant", access_token="kajfe0983qjaf309ajj3w8j3aij3a3"))""",
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

async def _get_elixir(name: str):
  url = f"http://127.0.0.0/elixir/?name={name}&page=1&size=50"
  headers = {
      "Accept": "application/json",
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
  asyncio.run(_get_elixir(name="Speed%20Elixir"))""",
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

async def _get_elixir(name: str, access_token: str):
  url = f"http://127.0.0.0/elixir/?name={name}&page=1&size=50"
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
  asyncio.run(_get_elixir(name="Speed%20Elixir", access_token="kajfe0983qjaf309ajj3w8j3aij3a3"))""",
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

async def _get_all(category: str):
  url = f"http://127.0.0.0/all/{category}?page=1&size=50"
  headers = {
      "Accept": "application/json",
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
  asyncio.run(_get_all(category="pals"))""",
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

async def _get_all(category: str, access_token: str):
  url = f"http://127.0.0.0/all/{category}?page=1&size=50"
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
  asyncio.run(_get_all(category="pals", access_token="kajfe0983qjaf309ajj3w8j3aij3a3"))""",
        "label": "Python OAuth",
    },
]


autocomplete = [
    {
        "lang": "Curl",
        "source": """curl -X 'GET' \ 
  'http://127.0.0.0/autocomplete/palname/?name=la&page=1&size=50' \ 
  -H 'Accept: application/json'""",
        "label": "Curl",
    },
    {
        "lang": "Python",
        "source": """import asyncio
import json
import aiohttp
from aiohttp.client_exceptions import ClientConnectorError

async def _get_autocomplete(category: str, name: str):
  url = f"http://127.0.0.0/autocomplete/{category}?name={name}&page=1&size=50"
  headers = {
      "Accept": "application/json",
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
  asyncio.run(_get_autocomplete(category="palname", name="la"))""",
        "label": "Python",
    },
    {
        "lang": "Curl",
        "source": """curl -X 'GET' \ 
  'http://127.0.0.0/autocomplete/palname/?name=la&page=1&size=50' \ 
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

async def _get_autocomplete(category: str, name: str, access_token: str):
  url = f"http://127.0.0.0/autocomplete/{category}?name={name}&page=1&size=50"
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
  asyncio.run(_get_autocomplete(category="palname", name="la", access_token="kajfe0983qjaf309ajj3w8j3aij3a3"))""",
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

async def _post_login(username: str, password: str):
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
  asyncio.run(_post_login(username="Bob123", password="SomePass"))""",
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

async def _post_refresh(refresh_token: str):
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
  asyncio.run(_post_refresh(refresh_token="kafaj083209jq904j8qjiaf39"))""",
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

async def _put_user_change_password(current_password: str, new_password: str, access_token: str):
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
  asyncio.run(_put_user_change_password(current_password="SomePass", new_password="SomeNewPass", access_token="kajfe0983qjaf309ajj3w8j3aij3a3"))""",
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

async def _get_user_me(access_token: str):
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
  asyncio.run(_get_user_me(access_token="kajfe0983qjaf309ajj3w8j3aij3a3"))""",
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

async def _post_add_user(access_token: str, username: str, password: str, scopes: list, disabled: bool):
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
  asyncio.run(_post_add_user(access_token="kajfe0983qjaf309ajj3w8j3aij3a3", username="Bob123", password="SomePass", scopes=["APIUser:Read", "APIUser:ChangePassword"], disabled=False))""",
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

async def _put_admin_change_password(username: str, new_password: str, access_token: str):
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
  asyncio.run(_put_admin_change_password(username="Bob123", new_password="SomeNewPass", access_token="kajfe0983qjaf309ajj3w8j3aij3a3"))""",
        "label": "Python",
    },
]


delete_user = [
    {
        "lang": "Curl",
        "source": """curl -X 'PUT' \ 
  'http://127.0.0.0/admin/deleteuser/' \ 
  -H 'Accept: application/json' \ 
  -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3' \ 
  -H 'Content-Type: application/x-www-form-urlencoded' \ 
  -d 'username=Bob123'""",
        "label": "Curl",
    },
    {
        "lang": "Python",
        "source": """import asyncio
import json
import aiohttp
from aiohttp.client_exceptions import ClientConnectorError

async def _delete_admin_delete_user(access_token: str, username: str):
  url = f"http://127.0.0.0/admin/deleteuser/"
  headers = {
      "Accept": "application/json",
      "Authorization": f"Bearer {access_token}",
      "Content-Type": "application/x-www-form-urlencoded",
  }
  body = {"username": username}
  try:
      async with aiohttp.ClientSession() as session:
          async with session.delete(url, headers=headers, data=body) as result:
              data = await result.json()
  except ClientConnectorError as e:
      print(f"ClientConnectorError: {e}")
  else:
      print(json.dumps(data, indent=2))

if __name__ == "__main__":
  asyncio.run(_delete_admin_delete_user(access_token="kajfe0983qjaf309ajj3w8j3aij3a3", username="Bob123"))""",
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

async def _get_admin_users(access_token: str):
  url = f"http://127.0.0.0/admin/users/?page=1&size=50"
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
  asyncio.run(_get_admin_users(access_token="kajfe0983qjaf309ajj3w8j3aij3a3"))""",
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

async def _put_admin_user_disable(access_token: str, username: str, disabled: bool):
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
  asyncio.run(_put_admin_user_disable(access_token="kajfe0983qjaf309ajj3w8j3aij3a3", username="Bob123", disabled=True))""",
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

async def _put_admin_change_scope(access_token: str, username: str, scopes: list):
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
  asyncio.run(_put_admin_change_scope(access_token="kajfe0983qjaf309ajj3w8j3aij3a3", username="Bob123", scopes=["APIUser:Read", "APIUser:ChangePassword"]))""",
        "label": "Python",
    },
]
