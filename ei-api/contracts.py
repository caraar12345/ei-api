# TODO: Implement solo contracts
# https://github.com/fanaticscripter/EggContractor/blob/master/solo/contract.go

from fastapi import APIRouter, Depends, HTTPException, Header

import sentry_sdk

sentry_sdk.init(
    dsn="https://d1c1fed592bc4d1ca6e6daae67ff5640@o915576.ingest.sentry.io/4504628047183872",
    traces_sample_rate=0.1,
)

from .proto.gen import ei_pb2
from .constants import *
from .ei_utils import *

router = APIRouter(
    prefix="/contracts",
    dependencies=[Depends(verify_egg_inc_id)],
    responses={404: {"description": "Not found"}},
    tags=["Contracts"],
)


@router.get(
    "/active",
    name="ActiveContracts",
    summary="Current contracts that the user is part of",
)
def get_coop_data(x_egg_inc_id: str | None = Header(default=None)):
    first_contact_resp, ok = load_ei_first_contact_data(x_egg_inc_id)
    if ok != True:
        raise HTTPException(400, detail=first_contact_resp.error_message)

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
                                "name": contributor.user_name,
                                "boost_tokens": contributor.boost_tokens,
                                "boost_tokens_spent": contributor.boost_tokens_spent,
                                "cash_on_hand": contributor.farm_info.cash_on_hand,
                                "eggs_laid": contributor.contribution_amount,
                                "eggs_per_hour": contributor.contribution_rate * 3600,
                                # fmt: off
                                "earning_bonus_percentage": 10 ** contributor.soul_power * 100,
                                # fmt: on
                                "farmer_role": get_farmer_role(
                                    get_soul_power_oom(contributor.soul_power)
                                ),
                                "earning_bonus_oom": get_soul_power_oom(
                                    contributor.soul_power
                                ),
                                "eggs_of_prophecy": contributor.farm_info.eggs_of_prophecy,
                                "farm_capacity": contributor.production_params.farm_capacity,
                                "farm_population": contributor.production_params.farm_population,
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

    out_doc = {
        "egg_inc_id": x_egg_inc_id,
        "contract_count": len(first_contact_resp.backup.contracts.contracts),
        "contracts": contract_list,
    }

    return out_doc
