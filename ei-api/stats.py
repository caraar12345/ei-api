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

import sys

sys.path.append("ei-api/")

import proto.gen.ei_pb2 as ei_pb2
from constants import *
from ei_utils import load_ei_first_contact_data


class StatsResource:
    def on_get(self, req, resp):
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

        first_contact_resp = load_ei_first_contact_data(egg_inc_id)
        doc = {
            "egg_inc_id": egg_inc_id,
            "total_eggs": [
                {
                    "egg_id": 1,
                    "egg_type": "edible",
                    "count": first_contact_resp.backup.stats.egg_totals[
                        EGG_TOTALS_IDS["edible"]
                    ],
                },
                {
                    "egg_id": 2,
                    "egg_type": "superfood",
                    "count": first_contact_resp.backup.stats.egg_totals[
                        EGG_TOTALS_IDS["superfood"]
                    ],
                },
                {
                    "egg_id": 3,
                    "egg_type": "medical",
                    "count": first_contact_resp.backup.stats.egg_totals[
                        EGG_TOTALS_IDS["medical"]
                    ],
                },
                {
                    "egg_id": 4,
                    "egg_type": "rocket_fuel",
                    "count": first_contact_resp.backup.stats.egg_totals[
                        EGG_TOTALS_IDS["rocket_fuel"]
                    ],
                },
                {
                    "egg_id": 5,
                    "egg_type": "super_material",
                    "count": first_contact_resp.backup.stats.egg_totals[
                        EGG_TOTALS_IDS["super_material"]
                    ],
                },
                {
                    "egg_id": 6,
                    "egg_type": "fusion",
                    "count": first_contact_resp.backup.stats.egg_totals[
                        EGG_TOTALS_IDS["fusion"]
                    ],
                },
                {
                    "egg_id": 7,
                    "egg_type": "quantum",
                    "count": first_contact_resp.backup.stats.egg_totals[
                        EGG_TOTALS_IDS["quantum"]
                    ],
                },
                {
                    "egg_id": 8,
                    "egg_type": "immortality",
                    "count": first_contact_resp.backup.stats.egg_totals[
                        EGG_TOTALS_IDS["immortality"]
                    ],
                },
                {
                    "egg_id": 9,
                    "egg_type": "tachyon",
                    "count": first_contact_resp.backup.stats.egg_totals[
                        EGG_TOTALS_IDS["tachyon"]
                    ],
                },
                {
                    "egg_id": 10,
                    "egg_type": "graviton",
                    "count": first_contact_resp.backup.stats.egg_totals[
                        EGG_TOTALS_IDS["graviton"]
                    ],
                },
                {
                    "egg_id": 11,
                    "egg_type": "dilithium",
                    "count": first_contact_resp.backup.stats.egg_totals[
                        EGG_TOTALS_IDS["dilithium"]
                    ],
                },
                {
                    "egg_id": 12,
                    "egg_type": "prodigy",
                    "count": first_contact_resp.backup.stats.egg_totals[
                        EGG_TOTALS_IDS["prodigy"]
                    ],
                },
                {
                    "egg_id": 13,
                    "egg_type": "terraform",
                    "count": first_contact_resp.backup.stats.egg_totals[
                        EGG_TOTALS_IDS["terraform"]
                    ],
                },
                {
                    "egg_id": 14,
                    "egg_type": "antimatter",
                    "count": first_contact_resp.backup.stats.egg_totals[
                        EGG_TOTALS_IDS["antimatter"]
                    ],
                },
                {
                    "egg_id": 15,
                    "egg_type": "dark_matter",
                    "count": first_contact_resp.backup.stats.egg_totals[
                        EGG_TOTALS_IDS["dark_matter"]
                    ],
                },
                {
                    "egg_id": 16,
                    "egg_type": "ai",
                    "count": first_contact_resp.backup.stats.egg_totals[
                        EGG_TOTALS_IDS["ai"]
                    ],
                },
                {
                    "egg_id": 17,
                    "egg_type": "nebula",
                    "count": first_contact_resp.backup.stats.egg_totals[
                        EGG_TOTALS_IDS["nebula"]
                    ],
                },
                {
                    "egg_id": 18,
                    "egg_type": "universe",
                    "count": first_contact_resp.backup.stats.egg_totals[
                        EGG_TOTALS_IDS["universe"]
                    ],
                },
                {
                    "egg_id": 19,
                    "egg_type": "enlightenment",
                    "count": first_contact_resp.backup.stats.egg_totals[
                        EGG_TOTALS_IDS["enlightenment"]
                    ],
                },
            ],
            "boosts_used": first_contact_resp.backup.stats.boosts_used,
            "video_doubler_uses": first_contact_resp.backup.stats.video_doubler_uses,
            "drone_takedowns": first_contact_resp.backup.stats.drone_takedowns,
            "drone_takedowns_elite": first_contact_resp.backup.stats.drone_takedowns_elite,
            "num_prestiges": first_contact_resp.backup.stats.num_prestiges,
            "num_piggy_breaks": first_contact_resp.backup.stats.num_piggy_breaks,
            "iap_packs_purchased": first_contact_resp.backup.stats.iap_packs_purchased,
            "piggy_full": first_contact_resp.backup.stats.piggy_full,
            "piggy_found_full": first_contact_resp.backup.stats.piggy_found_full,
            "time_piggy_filled_realtime": first_contact_resp.backup.stats.time_piggy_filled_realtime,
            "time_piggy_full_gametime": first_contact_resp.backup.stats.time_piggy_full_gametime,
            "lost_piggy_increments": first_contact_resp.backup.stats.lost_piggy_increments,
        }
        resp.text = json.dumps(doc)
