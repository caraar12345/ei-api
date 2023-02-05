# ei-api

[![Docker Image Version (latest by date)](https://img.shields.io/docker/v/aaroncarson/ei-api?style=for-the-badge)](https://hub.docker.com/aaroncarson/ei-api)

A Python project taking the _Egg, Inc._ API protobufs kindly published in [**fanaticscripter/Egg**](https://github.com/fanaticscripter/Egg) and using them to create a RESTful API for statistics.

---

## Use cases

- Egg counts in Grafana using Prometheus + [json_exporter](https://github.com/prometheus-community/json_exporter)
- Also drone takedown counts, boost use count, video doubler use count etc etc
  - Example config in the `examples` folder
- Contract / Coop data in JSON format
- ???

---

## Usage

### Relevant regardless
- OpenAPI docs are available at http://localhost:5648/docs
- The Egg, Inc. ID is provided as an HTTP header: `X-Egg-Inc-ID`
- Using [HTTPie](https://httpie.io) - `http http://localhost:5648/stats/ X-Egg-Inc-ID:EIxxxxxxxxxxxxxxxx`
- Using [curl](https://curl.se) - `curl http://localhost:5648/stats/ -H 'X-Egg-Inc-ID:EIxxxxxxxxxxxxxxxx'`
- You can get your Egg, Inc. ID from the Egg, Inc. app.
- Go to the 9 dots at the bottom, Settings, Privacy and Data. The EI ID is at the bottom.


### Docker (_recommended_)
- `ei-api` is available on Docker Hub ✨
- `docker run -d -p '5648:5648' aaroncarson/ei-api`
- There's an example [`docker-compose.yml`](examples/docker-compose.yml) file
- No config is required


### Install directly
- `ei-api` uses Poetry as its package manager
  - Install Poetry on your machine
    - `pip install poetry==1.3.2` _should_ work nicely
  - Run `poetry install` in the root of this repo
  - Once that's done, `poetry run uvicorn ei-api.app:app --reload --port 5648`
