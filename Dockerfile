FROM python:3.10.12

WORKDIR /api

COPY ./requirements.txt /requirements.txt

RUN pip install --no-cache-dir --upgrade -r /requirements.txt

COPY ./api /api

ARG HTTP_PORT

# CMD ["sh", "-c", "uvicorn mainapi:app --host 0.0.0.0 --port $HTTP_PORT"]

# If running behind a proxy like Nginx or Traefik add --proxy-headers
CMD ["sh", "-c", "uvicorn mainapi:app --host 0.0.0.0 --port $HTTP_PORT --proxy-headers --forwarded-allow-ips='*'"]
