FROM python:3.10-slim as builder

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.3.2

RUN pip install "poetry==${POETRY_VERSION}"

WORKDIR /app
COPY . /app/
RUN poetry install --no-interaction --no-ansi --without dev

EXPOSE 5648/tcp
ENTRYPOINT ["poetry", "run", "uvicorn", "--host", "0.0.0.0", "--port", "5648", "ei-api.app:app"]
