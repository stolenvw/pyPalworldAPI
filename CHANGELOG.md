# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added

- Game data from v0.2.0.6

### Changed

- Some images to new version from v0.2.0.6

## [0.0.2] - 2024-3-13

### Added

- Get paginate return of full category
    ```http
    GET /all/{category}
    ```
- NPC information.

### Changed

- fastapi to version 0.110.0
- fastapi-pagination to version 0.12.19
- pydantic to version 2.6.3
- SQLAlchemy to version 2.0.28
- uvicorn to version 0.28.0
- get pals to take multiple params to filter results more
- get bosspals to take multiple params to filter results more

### Fixed

- Docs successful response example value, to show example instead of just "string"
