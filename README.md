# ei-api

A Python project taking the _Egg, Inc._ API protobufs kindly published in [**fanaticscraper/Egg**](https://github.com/fanaticscraper/Egg) and using them to create a RESTful API for statistics.

---

## Use cases

- Egg counts in Grafana using Prometheus + [json_exporter](https://github.com/prometheus-community/json_exporter)
- Also drone takedown counts, boost use count, video doubler use count etc etc
- Contract / Co-Op data in JSON format
- ???

---

## Usage

- Uses Poetry as the package manager
  - Install Poetry on your machine
  - Run `poetry install` in the root of this repo
- Once that's done, `poetry run gunicorn ei-api.app`
- `http localhost:8000/stats?egg_inc_id=EIxxxxxxxxxxxxxxxx`
  - You can get your EI ID from the Egg, Inc. app.
  - Go to the 9 dots at the bottom, Settings, Privacy and Data. The EI ID is at the bottom.
