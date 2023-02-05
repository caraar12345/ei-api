from fastapi import APIRouter, Depends, HTTPException, Header
from fastapi.responses import PlainTextResponse


import sentry_sdk

sentry_sdk.init(
    dsn="https://d1c1fed592bc4d1ca6e6daae67ff5640@o915576.ingest.sentry.io/4504628047183872",
    traces_sample_rate=0.1,
)

import json
from base64 import b64encode

from .proto.gen import ei_pb2
from .constants import *
from .ei_utils import load_ei_first_contact_data, verify_egg_inc_id

router = APIRouter(
    prefix="/epic_research",
    dependencies=[Depends(verify_egg_inc_id)],
    responses={404: {"description": "Not found"}},
    tags=["Epic research"],
)


@router.get(
    "/",
    name="BasicEpicResearchData",
    summary="Egg, Inc. epic research types and the user's current levels",
)
def get_epic_research(x_egg_inc_id: str | None = Header(default=None)):
    first_contact_resp, ok = load_ei_first_contact_data(x_egg_inc_id)
    if ok != True:
        raise HTTPException(400, detail=first_contact_resp.error_message)

    epicResearch = first_contact_resp.backup.game.epic_research
    epicDict = {}
    for item in epicResearch:
        epicDict[item.id] = item.level
    return epicDict


@router.get(
    "/calculator/json",
    name="GoldenEggsCalculatorGeneratorJSON",
    summary="Generates JSON blob for the Egg, Inc. Golden Eggs Costs Calculator from user ID",
)
def epic_calculator_gen_json(x_egg_inc_id: str | None = Header(default=None)):
    first_contact_resp, ok = load_ei_first_contact_data(x_egg_inc_id)
    if ok != True:
        raise HTTPException(400, detail=first_contact_resp.error_message)

    game_backup = first_contact_resp.backup
    out_doc = {
        # fmt: off
        "eggs": game_backup.game.golden_eggs_earned - game_backup.game.golden_eggs_spent,
        # fmt: on
        "piggyLevel": game_backup.stats.num_piggy_breaks + 1,
        "piggyBank": game_backup.game.piggy_bank,
        "piggyDiscount": 0,
        "epicCalcOnlyDesired": False,
        "epicCalcIncludePiggy": False,
        "epicCalcTruckType": 0,
        "epicDiscount": 0,
        "hideCompleted": False,
        "columns": {
            "desc": True,
            "bonus": True,
            "spent": True,
            "remaining": True,
            "total": True,
        },
        "upgrades": {},
        "increase": {},
    }

    for research_item in game_backup.game.epic_research:
        calc_id = MAP_EPIC_EI_TO_CALC[research_item.id]
        out_doc["upgrades"][calc_id] = research_item.level
        out_doc["increase"][calc_id] = 0

    return out_doc


@router.get(
    "/calculator",
    name="GoldenEggsCalculatorGenerator",
    summary="Generates Base64 data for the Egg, Inc. Golden Eggs Costs Calculator from user ID",
    response_class=PlainTextResponse,
)
def epic_calculator_gen_b64(x_egg_inc_id: str | None = Header(default=None)):
    return b64encode(json.dumps(epic_calculator_gen_json(x_egg_inc_id)).encode("ascii"))
