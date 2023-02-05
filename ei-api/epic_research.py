import sentry_sdk
from sentry_sdk.integrations.falcon import FalconIntegration

sentry_sdk.init(
    dsn="https://d42921cbb87b4c26b1a91dc566d811f2@o915576.ingest.sentry.io/6596181",
    integrations=[
        FalconIntegration(),
    ],
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production,
    traces_sample_rate=0.1,
)

import falcon
import json
import re
from base64 import b64encode

import sys

sys.path.append("ei-api/")

import proto.gen.ei_pb2 as ei_pb2
from constants import *
from ei_utils import load_ei_first_contact_data


def getEpicResearch(first_contact_resp):
    epicResearch = first_contact_resp.backup.game.epic_research
    epicDict = {}
    for item in epicResearch:
        epicDict[item.id] = item.level
    return json.dumps(epicDict)


def epicCalculatorGen(first_contact_resp: ei_pb2.EggIncFirstContactResponse):
    game_backup = first_contact_resp.backup
    out_doc = {
        "eggs": game_backup.game.golden_eggs_earned
        - game_backup.game.golden_eggs_spent,
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

    return json.dumps(out_doc)


class EpicResearchData:
    def on_get(self, req: falcon.Request, resp: falcon.Response):
        # Check egg_inc_id is in the query string
        try:
            egg_inc_id = req.params["egg_inc_id"]
        except KeyError:
            resp.status = falcon.HTTP_400
            resp.text = json.dumps({"error": "No egg_inc_id provided"})
            return

        # Check that the egg_inc_id fits the expected format
        ei_id_pattern = re.compile("^EI[0-9]{16}$")
        if not ei_id_pattern.match(egg_inc_id):
            resp.status = falcon.HTTP_400
            resp.text = json.dumps({"error": "Invalid egg_inc_id"})
            return

        try:
            format = req.params["format"]
        except KeyError:
            format = "default"

        first_contact_resp = load_ei_first_contact_data(egg_inc_id)

        if format == "calculator_json":
            resp.text = epicCalculatorGen(first_contact_resp)
        elif format == "calculator_b64":
            resp.set_header("Content-Type", "text/plain")
            resp.text = b64encode(epicCalculatorGen(first_contact_resp).encode("ascii"))
        else:
            resp.text = getEpicResearch(first_contact_resp)
