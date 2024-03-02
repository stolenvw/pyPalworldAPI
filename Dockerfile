FROM python:3.10.12

WORKDIR /api

COPY ./requirements.txt /requirements.txt

RUN pip install --no-cache-dir --upgrade -r /requirements.txt

COPY ./api /api

ARG HTTP_PORT

# CMD ["uvicorn", "mainapi:app", "--host", "0.0.0.0", "--port", "8000"]

# If running behind a proxy like Nginx or Traefik add --proxy-headers
CMD ["uvicorn", "mainapi:app", "--host", "0.0.0.0", "--port", "8000", "--proxy-headers"]
