# TODO: Implement solo contracts
# https://github.com/fanaticscripter/EggContractor/blob/master/solo/contract.go

from fastapi import APIRouter, Depends, HTTPException, Header
import json
import os

if os.getenv("EI_DISABLE_SENTRY", default="false").lower() != "true":
    import sentry_sdk

    sentry_sdk.init(
        dsn="https://d1c1fed592bc4d1ca6e6daae67ff5640@o915576.ingest.sentry.io/4504628047183872",
        traces_sample_rate=0.1,
    )
else:
    print("Sentry disabled.")

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

    # Build coop lookup dictionary once - O(n) instead of O(n*m)
    coop_lookup = {
        coop.coop_identifier: coop
        for coop in first_contact_resp.backup.contracts.current_coop_statuses
    }

    backup_contracts = first_contact_resp.backup.contracts.contracts
    contract_list = []

    for contract in backup_contracts:
        coop_id = getattr(contract, 'coop_identifier', None)
        coop_contributors = []
        coop_grade = None
        coop_total = None

        # Direct lookup instead of nested loop - O(1)
        if coop_id and coop_id in coop_lookup:
            coop = coop_lookup[coop_id]
            coop_grade = coop.grade
            coop_total = coop.total_amount

            for contributor in coop.contributors:
                coop_contributors.append({
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
                })

        # Cache contract object to avoid repeated attribute access
        contract_obj = contract.contract
        max_coop_size = getattr(contract_obj, "max_coop_size", 1)
        custom_egg_id = contract_obj.custom_egg_id if contract_obj.HasField("custom_egg_id") else ""
        leggacy = contract_obj.leggacy or contract_obj.name.startswith("LEGGACY")

        contract_doc = {
            "contract_id": contract_obj.identifier,
            "contract_name": contract_obj.name,
            "contract_description": contract_obj.description,
            "contract_expiration_epoch_time": contract_obj.expiration_time,
            "contract_start_epoch_time": contract_obj.start_time,
            "contract_length_seconds": contract_obj.length_seconds,
            "contract_boost_token_timer": contract_obj.minutes_per_token,
            "contract_egg_type": ei_pb2.Egg.Name(contract_obj.egg),
            "custom_egg_id": custom_egg_id,
            "contract_leggacy": leggacy,
            "coop_allowed": contract_obj.coop_allowed,
            "coop_contributors": coop_contributors,
            "coop_id": coop_id,
            "coop_grade": ei_pb2.Contract.PlayerGrade.Name(coop_grade) if coop_grade is not None else None,
            "coop_total": coop_total
        }
        contract_list.append(contract_doc)

    return {
        "egg_inc_id": x_egg_inc_id,
        "contract_count": len(backup_contracts),
        "contracts": contract_list,
    }
