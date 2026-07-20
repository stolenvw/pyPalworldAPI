FROM ghcr.io/astral-sh/uv:python3.14-trixie-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential default-libmysqlclient-dev pkg-config \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml uv.lock ./

ENV UV_NO_DEV=1
ARG HTTP_PORT

RUN uv sync --frozen

COPY ./pyPalworldAPI /app/pyPalworldAPI

# CMD ["sh", "-c", "uv run uvicorn pyPalworldAPI.mainapi:app --host 0.0.0.0 --port $HTTP_PORT"]

# If running behind a proxy like Nginx or Traefik add --proxy-headers
CMD ["sh", "-c", "uv run uvicorn pyPalworldAPI.mainapi:app --host 0.0.0.0 --port $HTTP_PORT --proxy-headers --forwarded-allow-ips='*'"]
