from fastapi import FastAPI, HTTPException
from . import epic_research, full_backup
from tomli import load as toml_load

import sentry_sdk

sentry_sdk.init(
    dsn="https://d1c1fed592bc4d1ca6e6daae67ff5640@o915576.ingest.sentry.io/4504628047183872",
    traces_sample_rate=0.1,
)

with open("pyproject.toml", "rb") as pyproject_file:
    pyproject = toml_load(pyproject_file)

tags_metadata = [
    {
        "name": "Full backup",
        "description": "Egg, Inc. counts the game data on the Auxbrain servers as a backup. That naming is followed here.",
    },
    {"name": "Epic research"},
]

app = FastAPI(
    title=pyproject["tool"]["poetry"]["name"],
    version=pyproject["tool"]["poetry"]["version"],
    openapi_tags=tags_metadata,
)
app.include_router(epic_research.router)
app.include_router(full_backup.router)


@app.get("/", include_in_schema=False)
async def root():
    raise HTTPException(status_code=418)


# from .stats import StatsResource

# stats = StatsResource()
# app.add_route("/stats", stats)

# from .contracts import ContractResource

# contracts = ContractResource()
# app.add_route("/contracts", contracts)

# from .full_output import FullBackupResource

# full_backup = FullBackupResource()
# app.add_route("/full_backup", full_backup)

# from .epic_research import EpicResearchData

# epic_research = EpicResearchData()
# app.add_route("/epic_research", epic_research)
