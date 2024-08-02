<div align="center"><h1>Palworld API</h1>

More than just a paldex, includes a lot of game data.  

![GitHub Release](https://img.shields.io/github/v/release/stolenvw/pyPalworldAPI)
![GitHub top language](https://img.shields.io/github/languages/top/stolenvw/pyPalworldAPI)
![GitHub repo size](https://img.shields.io/github/repo-size/stolenvw/pyPalworldAPI)
![GitHub License](https://img.shields.io/github/license/stolenvw/pyPalworldAPI)
![Static Badge](https://img.shields.io/badge/3.10.12-gray?logo=python&label=Python&labelColor=gray&color=purple)
![Static Badge](https://img.shields.io/badge/v0.2.4.0-gray?label=Game%20Data&labelColor=gray&color=blue)
</div>

## Features

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

## API Reference

`/redoc` for API docs.  Can be disabled by leaving environment variable `REDOC_URL` blank

`/docs` For testing API. Can be disabled by leaving environment variable `DOCS_URL` blank

*_When using OAuth all API request need to use Authorization header_

- ```http
    Authorization: Bearer ACCESS-TOKEN
  ```

<details>
  <summary>Reference</summary>

  - #### API
    *_When using OAuth users need the `APIUser:Read` scope_

    - <details>
        <summary>Pals</summary>

      #### Get Pals. Ex. `/pals/?name=lamball`,  `/pals/?name=lamball&page=1&size=20`

      ```http
        GET /pals/?
      ```

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

      #### Get Boss Pals. Ex. `/bosspals/?name=Mammorest`,  `/bosspals/?name=Mammorest&page=1&size=20`

      ```http
        GET /bosspals/?
      ```

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

      #### Get Breeding. Ex. `/breeding/?name=Anubis`,  `/breeding/?name=Anubis&page=1&size=20`

      ```http
        GET /breeding/?
      ```

      | Parameter | Type     | Description                |
      | :-------- | :------- | :------------------------- |
      | `name` | `string` | Pal you want get egg of |
      | Optional: | | |
      | `page` | `int` | Page number to return |
      | ` size` | `int` | How many to return per page. Default:`50` Max:`200` |

      </details>

    - <details>
        <summary>Sickness</summary>

      #### Get Sickness. Ex. `/sickness/?name=ulcer`,  `/sickness/?name=ulcer&page=1&size=20`

      ```http
        GET /sickness/?
      ```

      | Parameter | Type     | Description                |
      | :-------- | :------- | :------------------------- |
      | `name` | `string` | Sickness |
      | Optional: | | |
      | `page` | `int` | Page number to return |
      | ` size` | `int` | How many to return per page. Default:`50` Max:`200` |

      </details>

    - <details>
        <summary>Items</summary>

      #### Get Items. Ex. `/items/?name=arrow`,  `/items/?name=Arrow&page=1&size=20`

      ```http
        GET /items/?
      ```

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

      #### Get Crafting. Ex. `/crafting/?name=arrow`,  `/crafting/?name=Arrow&page=1&size=20`

      ```http
        GET /crafting/?
      ```

      | Parameter | Type     | Description                |
      | :-------- | :------- | :------------------------- |
      | `name` | `string` | Item name to get recipe info for|
      | Optional: | | |
      | `page` | `int` | Page number to return |
      | ` size` | `int` | How many to return per page. Default:`50` Max:`200` |

      </details>

    - <details>
        <summary>Gear</summary>

      #### Get Gear. Ex. `/gear/?name=cloth%20outfit`,  `?name=cloth%20outfit&page=1&size=20`

      ```http
        GET /gear/?
      ```

      | Parameter | Type     | Description                |
      | :-------- | :------- | :------------------------- |
      | `name` | `string` | Gear to lookup |
      | Optional: | | |
      | `page` | `int` | Page number to return |
      | ` size` | `int` | How many to return per page. Default:`50` Max:`200` |

      </details>

    - <details>
        <summary>Foodeffect</summary>

      #### Get Foodeffect. Ex. `/foodeffect/?name=salad`,  `?foodeffect=salad&page=1&size=20`

      ```http
        GET /foodeffect/?
      ```

      | Parameter | Type     | Description                |
      | :-------- | :------- | :------------------------- |
      | `name` | `string` | Food item |
      | Optional: | | |
      | `page` | `int` | Page number to return |
      | ` size` | `int` | How many to return per page. Default:`50` Max:`200` |

      </details>

    - <details>
        <summary>Tech</summary>

      #### Get Tech. Ex. `/tech/?name=Nail`,  `/tech/?name=Nail&page=1&size=20`

      ```http
        GET /tech/?
      ```

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

      #### Get Build. Ex. `/build/?name=Campfire`,  `/build/?name=Campfire&page=1&size=20`

      ```http
        GET /build/?
      ```

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

      #### Get Passive. Ex. `/passive/?name=Brave`,  `?passive=Brave&page=1&size=20`

      ```http
        GET /passive/?
      ```

      | Parameter | Type     | Description                |
      | :-------- | :------- | :------------------------- |
      | `name` | `string` | Passive skill |
      | Optional: | | |
      | `page` | `int` | Page number to return |
      | ` size` | `int` | How many to return per page. Default:`50` Max:`200` |

      </details>

    - <details>
        <summary>NPC</summary>

      #### Get NPC. Ex. `/npc/?name=Wandering%20Merchant`,  `/npc/?name=Wandering%20Merchant&page=1&size=20`

      ```http
        GET /npc/?
      ```

      | Parameter | Type     | Description                |
      | :-------- | :------- | :------------------------- |
      | `name` | `string` | npc |
      | Optional: | | |
      | `page` | `int` | Page number to return |
      | ` size` | `int` | How many to return per page. Default:`50` Max:`200` |

      </details>

    - <details>
        <summary>Elixir</summary>

      #### Get Elixir. Ex. `/elixir/?name=Power%20Elixir`,  `/elixir/?name=Power%20Elixir&page=1&size=20`

      ```http
        GET /elixir/?
      ```

      | Parameter | Type     | Description                |
      | :-------- | :------- | :------------------------- |
      | `name` | `string` | Elixir |
      | Optional: | | |
      | `page` | `int` | Page number to return |
      | ` size` | `int` | How many to return per page. Default:`50` Max:`200` |

      </details>

    - <details>
        <summary>All</summary>

      #### Get All. Ex. `/all/pals`

      ```http
        GET /all/{category}
      ```

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
      | ` size` | `int` | How many to return per page. Default:`50` Max:`200` |

      </details>

    - <details>
        <summary>Autocomplete</summary>

      #### Get Autocomplete. Ex. `/autocomplete/palname/?name=la`

      ```http
        GET /autocomplete/{category}/?name=
      ```

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

      #### Login. Ex. `/oauth2/login/`

      *_Login will make any refresh token you currently have invalid._

      ```http
        POST /oauth2/login/
        accept: application/json
        Content-Type: application/x-www-form-urlencoded

        username=USERNAME&password=PASSWORD
      ```

      | Category | Type     | Description                |
      | :-------- | :------- | :------------------------- |
      | `username` | `string` | Username |
      | `password` | `string` | Password |

      </details>

    - <details>
        <summary>Refresh</summary>

      #### Refresh. Ex. `/oauth2/refresh/`

      ```http
        POST /oauth2/refresh/
        accept: application/json
        Content-Type: application/x-www-form-urlencoded

        token=REFRESH-TOKEN&grant_type=refresh_token
      ```

      | Category | Type     | Description                |
      | :-------- | :------- | :------------------------- |
      | `token` | `string` | Refresh token |
      | `grant_type` | `string` | refresh_token |

      </details>

  - #### User

    - <details>
        <summary>Change Password</summary>

      #### Change Password. Ex. `/user/changepassword/`

      *_Users need the `APIUser:Read, APIUser:ChangePassword` scopes_  
      *Change password will make any access/refresh token you currently have invalid.

      ```http
        PUT /user/changepassword/
        accept: application/json
        Authorization: Bearer ACCESS-TOKEN
        Content-Type: application/x-www-form-urlencoded
        
        current_password=CURRENT-PASSWORD&new_password=NEW-PASSWORD
      ```

      | Category | Type     | Description                |
      | :-------- | :------- | :------------------------- |
      | `current_password` | `string` | Current Password |
      | `new_password` | `string` | New Password |

      </details>

    - <details>
        <summary>Me</summary>

      #### Me. Ex. `/user/me/`

      *_Users need the `APIUser:Read` scopes_

      ```http
        PUT /user/me/
        accept: application/json
        Authorization: Bearer ACCESS-TOKEN
      ```

      </details>

  - #### Admin

    *_Users need the `APIAdmin:Write` scope_

    - <details>
        <summary>Add User</summary>

      #### Add User. Ex. `/admin/adduser/`

      <blockquote>

      ```http
        POST /admin/adduser/
        accept: application/json
        Authorization: Bearer ACCESS-TOKEN
        Content-Type: application/json
      ```
      ```json
        {
          "username": "USERNAME",
          "password": "PASSWORD",
          "scopes": [
            "APIUser:Read",
            "APIUser:ChangePassword"
          ],
          "disabled": false
        }
      ```

      </blockquote>

      | Category | Type     | Description                |
      | :-------- | :------- | :------------------------- |
      | `username` | `string` | Username |
      | `password` | `string` | Password |
      | `scopes` | `list` | List of scopes. Valid Scopes [APIAdmin:Write, APIUser:Read, APIUser:ChangePassword] |
      | `disabled` | `bool` | Account disabled |

      </details>

    - <details>
          <summary>Change Password</summary>

        #### Change Password. Ex. `/admin/chpass/`

        *Change password will make any access/refresh token the user currently has invalid.

        ```http
          PUT /admin/chpass/
          accept: application/json
          Authorization: Bearer ACCESS-TOKEN
          Content-Type: application/x-www-form-urlencoded

          username=USERNAME&new_password=PASSWORD
        ```

        | Category | Type     | Description                |
        | :-------- | :------- | :------------------------- |
        | `username` | `string` | Username |
        | `new_password` | `string` | Password |

        </details>

    - <details>
          <summary>Delete User</summary>

        #### Delete User. Ex. `/admin/deleteuser/`

        ```http
          DELETE /admin/deleteuser/
          accept: application/json
          Authorization: Bearer ACCESS-TOKEN
          Content-Type: application/x-www-form-urlencoded

          username=USERNAME
        ```

        | Category | Type     | Description                |
        | :-------- | :------- | :------------------------- |
        | `username` | `string` | Username |

        </details>

    - <details>
          <summary>Users</summary>

        #### Users. Ex. `/admin/users/`

        ```http
          GET /admin/users/
          accept: application/json
          Authorization: Bearer ACCESS-TOKEN
        ```

        | Category | Type     | Description                |
        | :-------- | :------- | :------------------------- |
        | Optional: | | |
        | `page` | `int` | Page number to return |
        | ` size` | `int` | How many to return per page. Default:`50` Max:`200` |

        </details>

    - <details>
          <summary>User Disable</summary>

        #### User Disable. Ex. `/admin/userdisable/`

        ```http
          PUT /admin/userdisable/
          accept: application/json
          Authorization: Bearer ACCESS-TOKEN
          Content-Type: application/x-www-form-urlencoded

          username=USERNAME&disabled=True
        ```

        | Category | Type     | Description                |
        | :-------- | :------- | :------------------------- |
        | `username` | `string` | Username |
        | `disabled` | `bool` | Account disabled |

        </details>

    - <details>
        <summary>Change Scopes</summary>

      #### Change Scopes. Ex. `/admin/chscope/`

      <blockquote>

      ```http
        POST /admin/chscope/
        accept: application/json
        Authorization: Bearer ACCESS-TOKEN
        Content-Type: application/json
      ```
      ```json
        {
          "username": "USERNAME",
          "scopes": [
            "APIUser:Read",
            "APIUser:ChangePassword"
          ],
        }
      ```

      </blockquote>

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

  - Move the `.env` into the `api` folder

  - Install Python requirements.

    ```bash
      pip install -r requirements.txt
    ```

  - Import the [PalAPI.sql](mysqldb/PalAPI.sql) data from the mysqldb folder into your MySQL server.

  - If not using a reverse proxy run from in the api folder.

    ```bash
      uvicorn mainapi:app --host 0.0.0.0 --port 8000
    ```

  - With a reverse proxy run from in the api folder

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