<div align="center"><h1>Palworld API</h1>

More than just a paldex, includes a lot of game data.  

![GitHub Release](https://img.shields.io/github/v/release/stolenvw/pyPalworldAPI)
![GitHub top language](https://img.shields.io/github/languages/top/stolenvw/pyPalworldAPI)
![GitHub repo size](https://img.shields.io/github/repo-size/stolenvw/pyPalworldAPI)
![GitHub License](https://img.shields.io/github/license/stolenvw/pyPalworldAPI)
![Static Badge](https://img.shields.io/badge/3.10.12-gray?logo=python&label=Python&labelColor=gray&color=purple)
![Static Badge](https://img.shields.io/badge/v0.3.5.0-gray?label=Game%20Data&labelColor=gray&color=blue)
</div>

## Features

- OAuth
- Case Insensitive Lookups
- Pal Lookups
- Breeding Lookups
- Sickness Lookups
- Items Lookups
- Crafting Lookups
- Gear Lookups
- Food Effects Lookups
- Tech Tree Lookups
- Building Objects
- Built in docs
- Built in interface to test api calls
- Data stored in MySQL database
- Passive Skills
- NPC Lookups
- Elixir Lookups

## API Reference

`/redoc` for API docs.  Can be disabled by leaving environment variable `REDOC_URL` blank

`/docs` For testing API. Can be disabled by leaving environment variable `DOCS_URL` blank

> [!NOTE]
> _When using OAuth all API request need to use Authorization header_
> - ```http
>   Authorization: Bearer ACCESS-TOKEN
>   ```

<details>
  <summary>Reference</summary>

  - #### API
    > [!IMPORTANT]  
    > _When using OAuth users need the `APIUser:Read` scope_

    - <details>
        <summary>Pals</summary>

      #### Get Pals. Ex.

      - <details>
        <summary>Curl</summary>
        
        #### With Out OAuth
        ```bash
        curl -X 'GET' \
          'http://127.0.0.0/pals/?name=lamball&page=1&size=50' \
          -H 'Accept: application/json'
        ```

        #### OAuth
        ```bash
        curl -X 'GET' \
          'http://127.0.0.0/pals/?name=lamball&page=1&size=50' \
          -H 'Accept: application/json' \
          -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'
        ```

        </details>

      - <details>
        <summary>Python</summary>
        
        #### With Out OAuth
        ```python
        import asyncio
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
            asyncio.run(get_pals(name="lamball"))
        ```

        #### OAuth
        ```python
        import asyncio
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
            )
        ```

        </details>

      | Parameter | Type     | Description                |
      | :-------- | :------- | :------------------------- |
      | `name` | `string` | Pal name |
      | `dexkey` | `string` | Paldex string. Ex.`012B` |
      | `type` | `string` | Pal type |
      | `suitability` | `string` | Pal work type |
      | `drop` | `string` | Item |
      | `skill` | `string` | Pal skill |
      | `nocturnal` | `bool` | If true returns night pals, false returns day pal |
      | Optional: | | |
      | `page` | `int` | Page number to return |
      | ` size` | `int` | How many to return per page. Default:`50` Max:`200` |

      </details>

    - <details>
        <summary>Boss Pals</summary>

      #### Get Boss Pals. Ex.

      - <details>
        <summary>Curl</summary>
        
        #### With Out OAuth
        ```bash
        curl -X 'GET' \
          'http://127.0.0.0/bosspals/?name=Mammorest&page=1&size=50' \
          -H 'Accept: application/json'
        ```

        #### OAuth
        ```bash
        curl -X 'GET' \
          'http://127.0.0.0/bosspals/?name=Mammorest&page=1&size=50' \
          -H 'Accept: application/json' \
          -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'
        ```

        </details>

      - <details>
        <summary>Python</summary>
        
        #### With Out OAuth
        ```python
        import asyncio
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
            asyncio.run(get_bosspals(name="Mammorest"))
        ```

        #### OAuth
        ```python
        import asyncio
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
            )
        ```

        </details>

      | Parameter | Type     | Description                |
      | :-------- | :------- | :------------------------- |
      | `name` | `string` | Pal name |
      | `type` | `string` | Pal type |
      | `suitability` | `string` | Pal work type |
      | `drop` | `string` | Item |
      | `skill` | `string` | Pal skill |
      | `nocturnal` | `bool` | If true returns night pals, false returns day pal |
      | Optional: | | |
      | `page` | `int` | Page number to return |
      | ` size` | `int` | How many to return per page. Default:`50` Max:`200` |

      </details>

    - <details>
        <summary>Breeding</summary>

      #### Get Breeding. Ex.

      - <details>
        <summary>Curl</summary>
        
        #### With Out OAuth
        ```bash
        curl -X 'GET' \
          'http://127.0.0.0/breeding/?name=Anubis&page=1&size=50' \
          -H 'Accept: application/json'
        ```

        #### OAuth
        ```bash
        curl -X 'GET' \
          'http://127.0.0.0/breeding/?name=Anubis&page=1&size=50' \
          -H 'Accept: application/json' \
          -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'
        ```

        </details>

      - <details>
        <summary>Python</summary>
        
        #### With Out OAuth
        ```python
        import asyncio
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
            asyncio.run(get_breeding(name="Anubis"))
        ```

        #### OAuth
        ```python
        import asyncio
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
            )
        ```

        </details>

      | Parameter | Type     | Description                |
      | :-------- | :------- | :------------------------- |
      | `name` | `string` | Pal you want get egg of |
      | Optional: | | |
      | `page` | `int` | Page number to return |
      | ` size` | `int` | How many to return per page. Default:`50` Max:`200` |

      </details>

    - <details>
        <summary>Sickness</summary>

      #### Get Sickness. Ex.

      - <details>
        <summary>Curl</summary>
        
        #### With Out OAuth
        ```bash
        curl -X 'GET' \
          'http://127.0.0.0/sickness/?name=ulcer&page=1&size=50' \
          -H 'Accept: application/json'
        ```

        #### OAuth
        ```bash
        curl -X 'GET' \
          'http://127.0.0.0/sickness/?name=ulcer&page=1&size=50' \
          -H 'Accept: application/json' \
          -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'
        ```

        </details>

      - <details>
        <summary>Python</summary>
        
        #### With Out OAuth
        ```python
        import asyncio
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
            asyncio.run(get_sickness(name="ulcer"))
        ```

        #### OAuth
        ```python
        import asyncio
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
            )
        ```

        </details>

      | Parameter | Type     | Description                |
      | :-------- | :------- | :------------------------- |
      | `name` | `string` | Sickness |
      | Optional: | | |
      | `page` | `int` | Page number to return |
      | ` size` | `int` | How many to return per page. Default:`50` Max:`200` |

      </details>

    - <details>
        <summary>Items</summary>

      #### Get Items. Ex.

      - <details>
        <summary>Curl</summary>
        
        #### With Out OAuth
        ```bash
        curl -X 'GET' \
          'http://127.0.0.0/items/?name=arrow&page=1&size=50' \
          -H 'Accept: application/json'
        ```

        #### OAuth
        ```bash
        curl -X 'GET' \
          'http://127.0.0.0/items/?name=arrow&page=1&size=50' \
          -H 'Accept: application/json' \
          -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'
        ```

        </details>

      - <details>
        <summary>Python</summary>
        
        #### With Out OAuth
        ```python
        import asyncio
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
            asyncio.run(get_items(name="arrow"))
        ```

        #### OAuth
        ```python
        import asyncio
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
            asyncio.run(get_items(name="arrow", access_token="kajfe0983qjaf309ajj3w8j3aij3a3"))
        ```

        </details>

      | Parameter | Type     | Description                |
      | :-------- | :------- | :------------------------- |
      | `name` | `string` | Item name |
      | `type` | `string` | Item type |
      | `suitability` | `string` | Pal work type |
      | Optional: | | |
      | `page` | `int` | Page number to return |
      | ` size` | `int` | How many to return per page. Default:`50` Max:`200` |

      </details>

    - <details>
        <summary>Crafting</summary>

      #### Get Crafting. Ex.

      - <details>
        <summary>Curl</summary>
        
        #### With Out OAuth
        ```bash
        curl -X 'GET' \
          'http://127.0.0.0/crafting/?name=arrow&page=1&size=50' \
          -H 'Accept: application/json'
        ```

        #### OAuth
        ```bash
        curl -X 'GET' \
          'http://127.0.0.0/crafting/?name=arrow&page=1&size=50' \
          -H 'Accept: application/json' \
          -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'
        ```

        </details>

      - <details>
        <summary>Python</summary>
        
        #### With Out OAuth
        ```python
        import asyncio
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
            asyncio.run(get_crafting(name="arrow"))
        ```

        #### OAuth
        ```python
        import asyncio
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
            )
        ```

        </details>

      | Parameter | Type     | Description                |
      | :-------- | :------- | :------------------------- |
      | `name` | `string` | Item name to get recipe info for|
      | Optional: | | |
      | `page` | `int` | Page number to return |
      | ` size` | `int` | How many to return per page. Default:`50` Max:`200` |

      </details>

    - <details>
        <summary>Gear</summary>

      #### Get Gear. Ex.

      - <details>
        <summary>Curl</summary>
        
        #### With Out OAuth
        ```bash
        curl -X 'GET' \
          'http://127.0.0.0/gear/?name=cloth%20outfit&page=1&size=50' \
          -H 'Accept: application/json'
        ```

        #### OAuth
        ```bash
        curl -X 'GET' \
          'http://127.0.0.0/gear/?name=cloth%20outfit&page=1&size=50' \
          -H 'Accept: application/json' \
          -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'
        ```

        </details>

      - <details>
        <summary>Python</summary>
        
        #### With Out OAuth
        ```python
        import asyncio
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
            asyncio.run(get_gear(name="cloth outfit"))
        ```

        #### OAuth
        ```python
        import asyncio
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
            )
        ```

        </details>

      | Parameter | Type     | Description                |
      | :-------- | :------- | :------------------------- |
      | `name` | `string` | Gear to lookup |
      | Optional: | | |
      | `page` | `int` | Page number to return |
      | ` size` | `int` | How many to return per page. Default:`50` Max:`200` |

      </details>

    - <details>
        <summary>Foodeffect</summary>

      #### Get Foodeffect. Ex.

      - <details>
        <summary>Curl</summary>
        
        #### With Out OAuth
        ```bash
        curl -X 'GET' \
          'http://127.0.0.0/foodeffect/?name=salad&page=1&size=50' \
          -H 'Accept: application/json'
        ```

        #### OAuth
        ```bash
        curl -X 'GET' \
          'http://127.0.0.0/foodeffect/?name=salad&page=1&size=50' \
          -H 'Accept: application/json' \
          -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'
        ```

        </details>

      - <details>
        <summary>Python</summary>
        
        #### With Out OAuth
        ```python
        import asyncio
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
            asyncio.run(get_foodeffect(name="salad"))
        ```

        #### OAuth
        ```python
        import asyncio
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
            )
        ```

        </details>

      | Parameter | Type     | Description                |
      | :-------- | :------- | :------------------------- |
      | `name` | `string` | Food item |
      | Optional: | | |
      | `page` | `int` | Page number to return |
      | ` size` | `int` | How many to return per page. Default:`50` Max:`200` |

      </details>

    - <details>
        <summary>Tech</summary>

      #### Get Tech. Ex.

      - <details>
        <summary>Curl</summary>
        
        #### With Out OAuth
        ```bash
        curl -X 'GET' \
          'http://127.0.0.0/tech/?name=Nail&page=1&size=50' \
          -H 'Accept: application/json'
        ```

        #### OAuth
        ```bash
        curl -X 'GET' \
          'http://127.0.0.0/tech/?name=Nail&page=1&size=50' \
          -H 'Accept: application/json' \
          -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'
        ```

        </details>

      - <details>
        <summary>Python</summary>
        
        #### With Out OAuth
        ```python
        import asyncio
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
            asyncio.run(get_tech(name="Nail"))
        ```

        #### OAuth
        ```python
        import asyncio
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
            asyncio.run(get_tech(name="Nail", access_token="kajfe0983qjaf309ajj3w8j3aij3a3"))
        ```

        </details>

      | Parameter | Type     | Description                |
      | :-------- | :------- | :------------------------- |
      | | One Of | |
      | `name` | `string` | Tech tree item |
      | `level` | `int` | Tech tree level |
      | Optional: | | |
      | `page` | `int` | Page number to return |
      | ` size` | `int` | How many to return per page. Default:`50` Max:`200` |

      </details>

    - <details>
        <summary>Build</summary>

      #### Get Build. Ex.

      - <details>
        <summary>Curl</summary>
        
        #### With Out OAuth
        ```bash
        curl -X 'GET' \
          'http://127.0.0.0/build/?name=Campfire&page=1&size=50' \
          -H 'Accept: application/json'
        ```

        #### OAuth
        ```bash
        curl -X 'GET' \
          'http://127.0.0.0/build/?name=Campfire&page=1&size=50' \
          -H 'Accept: application/json' \
          -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'
        ```

        </details>

      - <details>
        <summary>Python</summary>
        
        #### With Out OAuth
        ```python
        import asyncio
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
            asyncio.run(get_build(name="Campfire"))
        ```

        #### OAuth
        ```python
        import asyncio
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
            )
        ```

        </details>

      | Parameter | Type     | Description                |
      | :-------- | :------- | :------------------------- |
      | | One Of | |
      | `name` | `string` | Building Object |
      | `category` | `string` | Tech tree level |
      | Optional: | | |
      | `page` | `int` | Page number to return |
      | ` size` | `int` | How many to return per page. Default:`50` Max:`200` |

      </details>

    - <details>
        <summary>Passive</summary>

      #### Get Passive. Ex.

      - <details>
        <summary>Curl</summary>
        
        #### With Out OAuth
        ```bash
        curl -X 'GET' \
          'http://127.0.0.0/passive/?name=Brave&page=1&size=50' \
          -H 'Accept: application/json'
        ```

        #### OAuth
        ```bash
        curl -X 'GET' \
          'http://127.0.0.0/passive/?name=Brave&page=1&size=50' \
          -H 'Accept: application/json' \
          -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'
        ```

        </details>

      - <details>
        <summary>Python</summary>
        
        #### With Out OAuth
        ```python
        import asyncio
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
            asyncio.run(get_passive(name="Brave"))
        ```

        #### OAuth
        ```python
        import asyncio
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
            )
        ```

        </details>

      | Parameter | Type     | Description                |
      | :-------- | :------- | :------------------------- |
      | `name` | `string` | Passive skill |
      | Optional: | | |
      | `page` | `int` | Page number to return |
      | ` size` | `int` | How many to return per page. Default:`50` Max:`200` |

      </details>

    - <details>
        <summary>NPC</summary>

      #### Get NPC. Ex.

      - <details>
        <summary>Curl</summary>
        
        #### With Out OAuth
        ```bash
        curl -X 'GET' \
          'http://127.0.0.0/npc/?name=Wandering%20Merchant&page=1&size=50' \
          -H 'Accept: application/json'
        ```

        #### OAuth
        ```bash
        curl -X 'GET' \
          'http://127.0.0.0/npc/?name=Wandering%20Merchant&page=1&size=50' \
          -H 'Accept: application/json' \
          -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'
        ```

        </details>

      - <details>
        <summary>Python</summary>
        
        #### With Out OAuth
        ```python
        import asyncio
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
            asyncio.run(get_npc(name="Wandering Merchant"))
        ```

        #### OAuth
        ```python
        import asyncio
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
            )
        ```

        </details>

      | Parameter | Type     | Description                |
      | :-------- | :------- | :------------------------- |
      | `name` | `string` | npc |
      | Optional: | | |
      | `page` | `int` | Page number to return |
      | ` size` | `int` | How many to return per page. Default:`50` Max:`200` |

      </details>

    - <details>
        <summary>Elixir</summary>

      #### Get Elixir. Ex.

      - <details>
        <summary>Curl</summary>
        
        #### With Out OAuth
        ```bash
        curl -X 'GET' \
          'http://127.0.0.0/elixir/?name=Speed%20Elixir&page=1&size=50' \
          -H 'Accept: application/json'
        ```

        #### OAuth
        ```bash
        curl -X 'GET' \
          'http://127.0.0.0/elixir/?name=Speed%20Elixir&page=1&size=50' \
          -H 'Accept: application/json' \
          -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'
        ```

        </details>

      - <details>
        <summary>Python</summary>
        
        #### With Out OAuth
        ```python
        import asyncio
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
            asyncio.run(get_elixir(name="Speed Elixir"))
        ```

        #### OAuth
        ```python
        import asyncio
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
            )
        ```

        </details>

      | Parameter | Type     | Description                |
      | :-------- | :------- | :------------------------- |
      | `name` | `string` | Elixir |
      | Optional: | | |
      | `page` | `int` | Page number to return |
      | ` size` | `int` | How many to return per page. Default:`50` Max:`200` |

      </details>

    - <details>
        <summary>All</summary>

      #### Get All. Ex.

      - <details>
        <summary>Curl</summary>
        
        #### With Out OAuth
        ```bash
        curl -X 'GET' \
          'http://127.0.0.0/all/pals?page=1&size=50' \
          -H 'Accept: application/json'
        ```

        #### OAuth
        ```bash
        curl -X 'GET' \
          'http://127.0.0.0/all/pals?page=1&size=50' \
          -H 'Accept: application/json' \
          -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'
        ```

        </details>

      - <details>
        <summary>Python</summary>
        
        #### With Out OAuth
        ```python
        import asyncio
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
            asyncio.run(get_all(category="pals"))
        ```

        #### OAuth
        ```python
        import asyncio
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
            )
        ```

        </details>

      | Category | Type     | Description                |
      | :-------- | :------- | :------------------------- |
      | `pals` | `string` | Pals |
      | `bosspals` | `string` | Boss Pals |
      | `items` | `string` | Items |
      | `breeding` | `string` | Breeding |
      | `buildobjects` | `string` | Build Objects |
      | `crafting` | `string` | Crafting |
      | `foodeffect` | `string` | Food Effect |
      | `gear` | `string` | Gear |
      | `sickpal` | `string` | Sickness |
      | `techtree` | `string` | Tech Tree |
      | `passiveskills` | `string` | Passive Skills |
      | `npc` | `string` | Npc |
      | `elixir` | `string` | Elixir |
      | Optional: | | |
      | `page` | `int` | Page number to return |
      | `size` | `int` | How many to return per page. Default:`50` Max:`200` |

      </details>

    - <details>
        <summary>Autocomplete</summary>

      #### Get Autocomplete. Ex.

      - <details>
        <summary>Curl</summary>
        
        #### With Out OAuth
        ```bash
        curl -X 'GET' \
          'http://127.0.0.0/autocomplete/palname/?name=la&page=1&size=50' \
          -H 'Accept: application/json'
        ```

        #### OAuth
        ```bash
        curl -X 'GET' \
          'http://127.0.0.0/autocomplete/palname/?name=la&page=1&size=50' \
          -H 'Accept: application/json' \
          -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'
        ```

        </details>

      - <details>
        <summary>Python</summary>
        
        #### With Out OAuth
        ```python
        import asyncio
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
            asyncio.run(get_autocomplete(category="palname", name="la"))
        ```

        #### OAuth
        ```python
        import asyncio
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
            )
        ```

        </details>

      | Category | Type     | Description                |
      | :-------- | :------- | :------------------------- |
      | `palname` | `string` | Pal name |
      | `paldexkey` | `string` | Pal dex string |
      | `bossname` | `string` | Boss pal name |
      | `sickness` | `string` | Sickness |
      | `passiveskill` | `string` | Passive skill |
      | `itemname` | `string` | Item name |
      | `itemtype` | `string` | Item type |
      | `crafting` | `string` | Crafting |
      | `gear` | `string` | Gear |
      | `food` | `string` | Food |
      | `tech` | `string` | Tech |
      | `buildname` | `string` | Building object |
      | `buildcategory` | `string` | Building category |
      | `elixir` | `string` | Elixir |
      | `npc` | `string` | Npc |
      | Parameter: | | |
      | `name` | `string` | Start of name of what your looking for. |
      | Optional: | | |
      | `page` | `int` | Page number to return |
      | ` size` | `int` | How many to return per page. Default:`25` Max:`25` |

      </details>

  - #### OAuth2

    - <details>
        <summary>Login</summary>

      #### Login. Ex.

      > [!NOTE]  
      > _Login will make any refresh token you currently have invalid._

      - <details>
        <summary>Curl</summary>
        
        ```bash
        curl -X 'POST' \
          'http://127.0.0.0/oauth2/login/' \
          -H 'Accept: application/json' \
          -H 'Content-Type: application/x-www-form-urlencoded' \
          -d 'username=Bob123&password=SomePass'
        ```

        </details>

      - <details>
        <summary>Python</summary>
        
        ```python
        import asyncio
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
            asyncio.run(post_login(username="Bob123", password="SomePass"))
        ```

        </details>

      | Category | Type     | Description                |
      | :-------- | :------- | :------------------------- |
      | `username` | `string` | Username |
      | `password` | `string` | Password |

      </details>

    - <details>
        <summary>Refresh</summary>

      #### Refresh. Ex.

      - <details>
        <summary>Curl</summary>
        
        ```bash
        curl -X 'POST' \
          'http://127.0.0.0/oauth2/refresh/' \
          -H 'Accept: application/json' \
          -H 'Content-Type: application/x-www-form-urlencoded' \
          -d 'token=kafaj083209jq904j8qjiaf39&grant_type=refresh_token'
        ```

        </details>

      - <details>
        <summary>Python</summary>
        
        ```python
        import asyncio
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
            asyncio.run(post_refresh(refresh_token="kafaj083209jq904j8qjiaf39"))
        ```

        </details>

      | Category | Type     | Description                |
      | :-------- | :------- | :------------------------- |
      | `token` | `string` | Refresh token |
      | `grant_type` | `string` | This needs to be set to `refresh_token` |

      </details>

    - <details>
        <summary>Validate</summary>

      #### Validate. Ex.

      - <details>
        <summary>Curl</summary>
        
        ```bash
        curl -X 'GET' \ 
          'http://127.0.0.0/oauth2/validate' \ 
          -H 'Accept: application/json' \ 
          -H 'Authorization: OAuth kajfe0983qjaf309ajj3w8j3aij3a3'
        ```

        </details>

      - <details>
        <summary>Python</summary>
        
        ```python
        import asyncio
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
            asyncio.run(get_user_me(access_token="kajfe0983qjaf309ajj3w8j3aij3a3"))
        ```

        </details>

      </details>

  - #### User

    - <details>
        <summary>Change Password</summary>

      #### Change Password. Ex.

      > [!IMPORTANT]  
      > _Users need the `APIUser:Read, APIUser:ChangePassword` scopes_

      > [!NOTE]  
      > Changing password will make any access/refresh token you currently have invalid.

      - <details>
        <summary>Curl</summary>
        
        ```bash
        curl -X 'PUT' \
          'http://127.0.0.0/user/changepassword/' \
          -H 'Accept: application/json' \
          -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3' \
          -H 'Content-Type: application/x-www-form-urlencoded' \
          -d 'current_password=SomePass&new_password=SomeNewPass'
        ```

        </details>

      - <details>
        <summary>Python</summary>
        
        ```python
        import asyncio
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
            )
        ```

        </details>

      | Category | Type     | Description                |
      | :-------- | :------- | :------------------------- |
      | `current_password` | `string` | Current Password |
      | `new_password` | `string` | New Password |

      </details>

    - <details>
        <summary>Me</summary>

      #### Me. Ex.

      > [!IMPORTANT]  
      > _Users need the `APIUser:Read` scopes_

      - <details>
        <summary>Curl</summary>
        
        ```bash
        curl -X 'GET' \
          'http://127.0.0.0/user/me/' \
          -H 'Accept: application/json' \
          -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'
        ```

        </details>

      - <details>
        <summary>Python</summary>
        
        ```python
        import asyncio
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
            asyncio.run(get_user_me(access_token="kajfe0983qjaf309ajj3w8j3aij3a3"))
        ```

        </details>

      </details>

  - #### Admin

    > [!IMPORTANT]  
    > _Users need the `APIAdmin:Write` scope_

    - <details>
        <summary>Add User</summary>

      #### Add User. Ex.

      - <details>
        <summary>Curl</summary>
        
        ```bash
        curl -X 'Post' \
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
              }'
        ```

        </details>

      - <details>
        <summary>Python</summary>
        
        ```python
        import asyncio
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
            )
        ```

        </details>

      | Category | Type     | Description                |
      | :-------- | :------- | :------------------------- |
      | `username` | `string` | Username |
      | `password` | `string` | Password |
      | `scopes` | `list` | List of scopes. Valid Scopes [APIAdmin:Write, APIUser:Read, APIUser:ChangePassword] |
      | `disabled` | `bool` | Account disabled |

      </details>

    - <details>
        <summary>Change Password</summary>

      #### Change Password. Ex.

      > [!NOTE]
      > Changing password will make any access/refresh token the user currently has invalid.

      - <details>
        <summary>Curl</summary>
      
        ```bash
        curl -X 'PUT' \
          'http://127.0.0.0/admin/chpass/' \
          -H 'Accept: application/json' \
          -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3' \
          -H 'Content-Type: application/x-www-form-urlencoded' \
          -d 'username=Bob123&new_password=SomeNewPass'
        ```

        </details>

      - <details>
        <summary>Python</summary>
        
        ```python
        import asyncio
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
            )
          ```

          </details>

      | Category | Type     | Description                |
      | :-------- | :------- | :------------------------- |
      | `username` | `string` | Username |
      | `new_password` | `string` | Password |

      </details>

    - <details>
        <summary>Delete User</summary>

      #### Delete User. Ex.

      - <details>
        <summary>Curl</summary>
        
        ```bash
        curl -X 'DELETE' \
          'http://127.0.0.0/admin/deleteuser/?username=Bob123' \
          -H 'Accept: application/json' \
          -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'
        ```

        </details>

      - <details>
        <summary>Python</summary>
        
        ```python
        import asyncio
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
            )
        ```

        </details>

      | Category | Type     | Description                |
      | :-------- | :------- | :------------------------- |
      | `username` | `string` | Username |

      </details>

    - <details>
          <summary>Users</summary>

      #### Users. Ex.

      - <details>
        <summary>Curl</summary>
        
        ```bash
        curl -X 'GET' \
          'http://127.0.0.0/admin/users/?page=1&size=50' \
          -H 'Accept: application/json' \
          -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3'
        ```

        </details>

      - <details>
        <summary>Python</summary>
        
        ```python
        import asyncio
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
            asyncio.run(get_admin_users(access_token="kajfe0983qjaf309ajj3w8j3aij3a3"))
        ```

        </details>

      | Category | Type     | Description                |
      | :-------- | :------- | :------------------------- |
      | Optional: | | |
      | `page` | `int` | Page number to return |
      | ` size` | `int` | How many to return per page. Default:`50` Max:`200` |

      </details>

    - <details>
          <summary>User Disable</summary>

      #### User Disable. Ex.

      - <details>
        <summary>Curl</summary>
        
        ```bash
        curl -X 'PUT' \
          'http://127.0.0.0/admin/userdisable/' \
          -H 'Accept: application/json' \
          -H 'Authorization: Bearer kajfe0983qjaf309ajj3w8j3aij3a3' \
          -H 'Content-Type: application/x-www-form-urlencoded' \
          -d 'username=Bob123&disabled=True'
        ```

        </details>

      - <details>
        <summary>Python</summary>
        
        ```python
        import asyncio
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
            )
        ```

        </details>

      | Category | Type     | Description                |
      | :-------- | :------- | :------------------------- |
      | `username` | `string` | Username |
      | `disabled` | `bool` | Account disabled |

      </details>

    - <details>
        <summary>Change Scopes</summary>

      #### Change Scopes. Ex.

      - <details>
        <summary>Curl</summary>
        
        ```bash
        curl -X 'PUT' \
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
              }'
        ```

        </details>

      - <details>
        <summary>Python</summary>
        
        ```python
        import asyncio
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
            )
        ```

        </details>

      | Category | Type     | Description                |
      | :-------- | :------- | :------------------------- |
      | `username` | `string` | Username |
      | `scopes` | `list` | List of scopes. Valid Scopes [APIAdmin:Write, APIUser:Read, APIUser:ChangePassword] |

      </details>

</details>

## Deployment

- [Download latest release](https://github.com/stolenvw/pyPalworldAPI/releases/latest)

- Extract it somewhere.

- Edit the [example.env](example.env) file and rename to `.env`

  - To make `SECRET_KEY`
    - Linux: Run `openssl rand -hex 32`.
    - Windows: You can use this site https://www.browserling.com/tools/random-hex and change `How many digits?` to 64 then hit `Generate Hex`.

- Edit the [compose.yaml](compose.yaml) file.

  - Uncomment

    ```
    #ports:
    #  - ${HTTP_PORT}:${HTTP_PORT}
    ```

- _If not running it behind a reversed proxy edit the Dockerfile_

  - <details>
      <summary>Dockerfile Edits</summary>

      Uncomment this line `# CMD ["sh", "-c", "uvicorn mainapi:app --host 0.0.0.0 --port $HTTP_PORT"]`  
      and comment this line `CMD ["sh", "-c", "uvicorn mainapi:app --host 0.0.0.0 --port $HTTP_PORT --proxy-headers     --forwarded-allow-ips='*'"]`
    </details>

- To deploy run

```bash
docker-compose up
```

#### How to run without Docker

<details>

  _You will need your own MySQL server_

  - Do steps 1 through 3 above.

  - Recommended: Setup a Python virtual environment

  - Move the `.env` into the `pyPalworldAPI` folder

  - Install Python requirements.

    ```bash
      pip install -r requirements.txt
    ```

  - Import the [PalAPI.sql](mysqldb/PalAPI.sql) data from the mysqldb folder into your MySQL server.

  - If not using a reverse proxy run from in the pyPalworldAPI folder.

    ```bash
      uvicorn mainapi:app --host 0.0.0.0 --port 8000
    ```

  - With a reverse proxy run from in the pyPalworldAPI folder

    ```bash
      uvicorn mainapi:app --host 0.0.0.0 --port 8000 --proxy-headers --forwarded-allow-ips='*'
    ```

</details>


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`DOCS_URL`

`REDOC_URL`

`HTTP_PORT`

`MYSQL_USER`

`MYSQL_PASSWORD`

`MYSQL_DATABASE`

`SQL_HOST`

`MYSQL_USER_DATABASE`

`SQL_USER_HOST`

`MYSQL_RANDOM_ROOT_PASSWORD`

`MYSQL_PORT`

`COMPOSE_PROFILES`

`SECRET_KEY`

`ACCESS_TOKEN_EXPIRE_MINUTES`

`REFRESH_TOKEN_EXPIRE_DAYS`

`ADMIN_NAME`

## Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [FastAPI Pagination](https://uriyyo-fastapi-pagination.netlify.app/)
- [SQLModel](https://sqlmodel.tiangolo.com/)
- [MySQL](https://www.mysql.com/)

## Used By

This project is used by the following projects:

## Acknowledgements

 - [dkoz](https://github.com/dkoz)

## License

Distributed under the [MIT](LICENSE) License