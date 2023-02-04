FROM python:3.9-buster as builder

ENV POETRY_VERSION=1.3.2 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_HOME=/opt/poetry
RUN curl -sSL https://install.python-poetry.org | python
ENV PATH /opt/poetry/bin:$PATH

WORKDIR /app
COPY . /app/
RUN poetry install --no-interaction --no-ansi
COPY ./helpers/sentry_falcon.py /usr/local/lib/python3.9/site-packages/sentry_sdk/integrations/falcon.py

EXPOSE 5648/tcp
ENTRYPOINT ["poetry", "run", "gunicorn", "--bind", "0.0.0.0:5648", "ei-api.app"]
