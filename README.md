<div align="center"><h1>Palworld API</h1>

More than just a paldex, includes a lot of game data.  

![GitHub Release](https://img.shields.io/github/v/release/stolenvw/pyPalworldAPI)
![GitHub top language](https://img.shields.io/github/languages/top/stolenvw/pyPalworldAPI)
![GitHub repo size](https://img.shields.io/github/repo-size/stolenvw/pyPalworldAPI)
![GitHub License](https://img.shields.io/github/license/stolenvw/pyPalworldAPI)
![Static Badge](https://img.shields.io/badge/3.10.12-gray?logo=python&label=Python&labelColor=gray&color=purple)
![Static Badge](https://img.shields.io/badge/v0.1.5.1-gray?label=Game%20Data&labelColor=gray&color=blue)
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

<details>
  <summary>Reference</summary>

#### Get Pal(s), use one of the following parameters. Ex. `/pals/?name=lamball`,  `/pals/?name=lamball&page=1&size=20`

```http
  GET /pals/?
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| | One Of | |
| `name` | `string` | Pal name |
| `dexkey` | `string` | Paldex string. Ex.`012B` |
| `type` | `string` | Pal type |
| `suitability` | `string` | Pal work type |
| `drop` | `string` | Item |
| `skill` | `string` | Pal skill |
| `nocturnal` | `bool` | If true returns night pals, false returns day pal |
| | Can be used with above parameters. | |
| `page` | `int` | Page number to return |
| ` size` | `int` | How many to return per page. Default:`50` Max:`200` |

#### Get Boss Pal(s), use one of the following parameters. Ex. `/bosspals/?name=Mammorest`,  `/bosspals/?name=Mammorest&page=1&size=20`

```http
  GET /bosspals/?
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| | One Of | |
| `name` | `string` | Pal name |
| `type` | `string` | Pal type |
| `suitability` | `string` | Pal work type |
| | Can be used with above parameters. | |
| `page` | `int` | Page number to return |
| ` size` | `int` | How many to return per page. Default:`50` Max:`200` |

#### Get breeding. Ex. `/breeding/?name=Anubis`,  `/breeding/?name=Anubis&page=1&size=20`

```http
  GET /breeding/?
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `name` | `string` | Pal you want get egg of |
| | Can be used with above parameters. | |
| `page` | `int` | Page number to return |
| ` size` | `int` | How many to return per page. Default:`50` Max:`200` |

#### Get sickness. Ex. `/sickness/?name=ulcer`,  `/sickness/?name=ulcer&page=1&size=20`

```http
  GET /sickness/?
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `name` | `string` | Sickness |
| | Can be used with above parameters. | |
| `page` | `int` | Page number to return |
| ` size` | `int` | How many to return per page. Default:`50` Max:`200` |

#### Get items, use one of the following parameters. Ex. `/items/?name=arrow`,  `/items/?name=Arrow&page=1&size=20`

```http
  GET /items/?
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| | One Of | |
| `name` | `string` | Item name |
| `type` | `string` | Item type |
| `suitability` | `string` | Pal work type |
| | Can be used with above parameters. | |
| `page` | `int` | Page number to return |
| ` size` | `int` | How many to return per page. Default:`50` Max:`200` |

#### Get crafting, use one of the following parameters. Ex. `/crafting/?name=arrow`,  `/crafting/?name=Arrow&page=1&size=20`

```http
  GET /crafting/?
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `name` | `string` | Item name to get recipe info for|
| | Can be used with above parameters. | |
| `page` | `int` | Page number to return |
| ` size` | `int` | How many to return per page. Default:`50` Max:`200` |

#### Get gear, use one of the following parameters. Ex. `/gear/?name=cloth%20outfit`,  `?name=cloth%20outfit&page=1&size=20`

```http
  GET /gear/?
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `name` | `string` | Gear to lookup |
| | Can be used with above parameters. | |
| `page` | `int` | Page number to return |
| ` size` | `int` | How many to return per page. Default:`50` Max:`200` |

#### Get foodeffect, use one of the following parameters. Ex. `/foodeffect/?name=salad`,  `?foodeffect=salad&page=1&size=20`

```http
  GET /foodeffect/?
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `name` | `string` | Food item |
| | Can be used with above parameters. | |
| `page` | `int` | Page number to return |
| ` size` | `int` | How many to return per page. Default:`50` Max:`200` |

#### Get tech, use one of the following parameters. Ex. `/tech/?name=Nail`,  `/tech/?name=Nail&page=1&size=20`

```http
  GET /tech/?
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| | One Of | |
| `name` | `string` | Tech tree item |
| `level` | `int` | Tech tree level |
| | Can be used with above parameters. | |
| `page` | `int` | Page number to return |
| ` size` | `int` | How many to return per page. Default:`50` Max:`200` |

#### Get build, use one of the following parameters. Ex. `/build/?name=Campfire`,  `/build/?name=Campfire&page=1&size=20`

```http
  GET /build/?
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| | One Of | |
| `name` | `string` | Building Object |
| `category` | `string` | Tech tree level |
| | Can be used with above parameters. | |
| `page` | `int` | Page number to return |
| ` size` | `int` | How many to return per page. Default:`50` Max:`200` |

#### Get passive, use one of the following parameters. Ex. `/passive/?name=Brave`,  `?passive=Brave&page=1&size=20`

```http
  GET /passive/?
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `name` | `string` | Passive skill |
| | Can be used with above parameters. | |
| `page` | `int` | Page number to return |
| ` size` | `int` | How many to return per page. Default:`50` Max:`200` |

</details>

## Deployment

- [Download latest release](https://github.com/stolenvw/pyPalworldAPI/releases/latest)

- Extract it somewhere.

- Edit the [example.env](example.env) file and rename to `.env`

- Edit the [compose.yaml](compose.yaml) file.

  - Uncomment

    ```
    #ports:
    #  - ${HTTP_PORT}:${HTTP_PORT}
    ```

- _If not running it behind a reversid proxy edit the Dockerfile_

  - <details>
      <summary>Dockerfile Edits</summary>

      Uncommont this line `# CMD ["sh", "-c", "uvicorn mainapi:app --host 0.0.0.0 --port $HTTP_PORT"]`  
      and commont this line `CMD ["sh", "-c", "uvicorn mainapi:app --host 0.0.0.0 --port $HTTP_PORT --proxy-headers     --forwarded-allow-ips='*'"]`
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

`MYSQL_RANDOM_ROOT_PASSWORD`

`SQL_HOST`

`MYSQL_PORT`

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