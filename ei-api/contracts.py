# TODO: Implement solo contracts
# https://github.com/fanaticscripter/EggContractor/blob/master/solo/contract.go

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


class ContractResource:
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

        first_contact_resp = load_ei_first_contact_data(egg_inc_id=egg_inc_id)

        contract_list = []
        for contract in first_contact_resp.backup.contracts.contracts:
            try:
                coop_id = contract.coop_identifier
            except KeyError:
                coop_id = None

            coop_contributors = []

            if coop_id != None:
                for coop in first_contact_resp.backup.contracts.current_coop_statuses:
                    if coop_id == coop.coop_identifier:
                        for contributor in coop.contributors:
                            coop_contributors.append(
                                {
                                    "active": contributor.active,
                                    "boost_tokens": contributor.boost_tokens,
                                    "boost_tokens_spent": contributor.boost_tokens_spent,
                                    "cash_on_hand": contributor.farm_info.cash_on_hand,
                                    "contribution_amount": contributor.contribution_amount,
                                    "contribution_rate": contributor.contribution_rate,
                                    "contributor_name": contributor.user_name,
                                    "eggs_of_prophecy": contributor.farm_info.eggs_of_prophecy,
                                    "farm_capacity": contributor.production_params.farm_capacity,
                                    "farm_population": contributor.production_params.farm_population,
                                    "hyperloop_station": contributor.farm_info.hyperloop_station,
                                    "time_cheat_detected": contributor.time_cheat_detected,
                                }
                            )
            try:
                max_coop_size = contract.contract.max_coop_size
            except KeyError:
                max_coop_size = 1

            leggacy = True if contract.contract.name[:7] == "LEGGACY" else False

            contract_doc = {
                "contract_id": contract.contract.identifier,
                "contract_name": contract.contract.name,
                "contract_description": contract.contract.description,
                "contract_expiration_epoch_time": contract.contract.expiration_time,
                "contract_start_epoch_time": contract.contract.start_time,
                "contract_length_seconds": contract.contract.length_seconds,
                "contract_boost_token_timer": contract.contract.minutes_per_token,
                "contract_egg_type": ei_pb2.Egg.Name(contract.contract.egg),
                "contract_leggacy": leggacy,
                "coop_allowed": contract.contract.coop_allowed,
                "coop_contributors": coop_contributors,
                "coop_id": coop_id,
            }
            contract_list.append(contract_doc)

        document = {
            "egg_inc_id": egg_inc_id,
            "contract_count": len(first_contact_resp.backup.contracts.contracts),
            "contracts": contract_list,
        }

        resp.text = json.dumps(document)
