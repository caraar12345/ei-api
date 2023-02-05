# 🥚 ei-api

> 🫶 A massive thanks to [Auxbrain, Inc.](https://www.auxbrain.com) for creating this awesome game.
>
> 🗣️ And to the [Egg, Inc. Discord](https://discord.gg/egginc) for having an awesome community.

[![Docker Image Version (latest by date)](https://img.shields.io/docker/v/aaroncarson/ei-api?style=for-the-badge)](https://hub.docker.com/r/aaroncarson/ei-api)

A Python project taking the _Egg, Inc._ API protobufs kindly published in [**fanaticscripter/Egg**](https://github.com/fanaticscripter/Egg) - and created by Auxbrain - and using them to create a RESTful API for statistics.

---

> **Warning**
> This tool uses Sentry.io for error and performance tracking. 
> Your Egg, Inc. ID will be sent to the Sentry servers -- but it will be redacted on the server side **so I will not be able to see it**.
> _To disable Sentry entirely, set the environment variable `EI_DISABLE_SENTRY` to `true`._

---

## 💼 Use cases

- Egg counts in Grafana using Prometheus + [json_exporter](https://github.com/prometheus-community/json_exporter)
- Also drone takedown counts, boost use count, video doubler use count etc etc
  - Example config in the `examples` folder
- Contract / Coop data in JSON format
- Generate import data for the [Egg, Inc. Golden Eggs Costs Calculator](https://royalphysique.net/eggs/)
  - Huge thanks to https://github.com/SticklyMan for such a useful tool!
- ???

---

## 🛠️ Usage

### 🥚 Getting your Egg, Inc. ID
- You can get your EI ID from the Egg, Inc. app.
- Go to the 9 dots at the bottom, Settings, Privacy and Data. The EI ID is at the bottom.

### 📄 Relevant info
- OpenAPI docs are available at http://localhost:5648/docs
- The Egg, Inc. ID is provided as an HTTP header: `X-Egg-Inc-ID`
- Using [HTTPie](https://httpie.io) - `http http://localhost:5648/stats/ X-Egg-Inc-ID:EIxxxxxxxxxxxxxxxx`
- Using [curl](https://curl.se) - `curl http://localhost:5648/stats/ -H 'X-Egg-Inc-ID:EIxxxxxxxxxxxxxxxx'`


### 🐳 Docker (_recommended_)

- `ei-api` is available on Docker Hub ✨
- `docker run -d -p '5648:5648' aaroncarson/ei-api`
- There's an example [`docker-compose.yml`](examples/docker-compose.yml) file
- No config is required


### ⚙️ Install directly
- `ei-api` uses Poetry as its package manager
  - Install Poetry on your machine
    - `pip install poetry==1.3.2` _should_ work nicely
  - Run `poetry install` in the root of this repo
  - Once that's done, `poetry run uvicorn ei-api.app:app --reload --port 5648`

---

## ✏️ Config
- Only one thing can be configured - the path base / root path.
  - If you're using a reverse proxy, this means you can have multiple endpoints on one domain by changing the base of the path to something else.
  - The [FastAPI docs](https://fastapi.tiangolo.com/advanced/behind-a-proxy/) do a better job of explaining than I ever could!
- **Environment variable**: `EI_ROOT_PATH`
  - Defaults to `/`