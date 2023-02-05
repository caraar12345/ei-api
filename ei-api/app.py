from fastapi import FastAPI, HTTPException
from . import epic_research, full_backup, contracts, stats
from tomli import load as toml_load
import os

if os.getenv("EI_DISABLE_SENTRY", default="false").lower() != "true":
    import sentry_sdk

    sentry_sdk.init(
        dsn="https://d1c1fed592bc4d1ca6e6daae67ff5640@o915576.ingest.sentry.io/4504628047183872",
        traces_sample_rate=0.1,
    )
else:
    print("Sentry disabled.")
    
with open("pyproject.toml", "rb") as pyproject_file:
    pyproject = toml_load(pyproject_file)

tags_metadata = [
    {
        "name": "Full backup",
        "description": "Egg, Inc. counts the game data on the Auxbrain servers as a backup. That naming is followed here.",
    },
    {"name": "Epic research"},
    {"name": "Contracts"},
    {"name": "Stats"},
]

app = FastAPI(
    title=pyproject["tool"]["poetry"]["name"],
    version=pyproject["tool"]["poetry"]["version"],
    openapi_tags=tags_metadata,
    root_path=os.getenv("EI_ROOT_PATH", "/"),
)
app.include_router(epic_research.router)
app.include_router(full_backup.router)
app.include_router(contracts.router)
app.include_router(stats.router)


@app.get("/", include_in_schema=False)
async def root():
    raise HTTPException(status_code=418)