from fastapi import APIRouter, Depends, HTTPException, Header
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
    prefix="/stats",
    dependencies=[Depends(verify_egg_inc_id)],
    responses={404: {"description": "Not found"}},
    tags=["Statistics"],
)


@router.get(
    "/",
    name="GameStatistics",
    summary="Current stats surrounding the user's progress in Egg, Inc.",
)
def get_game_data(x_egg_inc_id: str | None = Header(default=None)):
    first_contact_resp, ok = load_ei_first_contact_data(x_egg_inc_id)
    if not ok:
        raise HTTPException(400, detail=first_contact_resp.error_message)

    backup = first_contact_resp.backup
    stats = backup.stats
    egg_totals_list = stats.egg_totals
    egg_totals_len = len(egg_totals_list)
    egg_counts = {}

    # 1. Standard Eggs (Indices 0-18 -> IDs 1-19)
    for i in range(min(19, egg_totals_len)):
        egg_id = i + 1
        name = ei_pb2.Egg.Name(egg_id).lower()
        egg_counts[egg_id] = {"egg_id": egg_id, "egg_type": name, "count": egg_totals_list[i]}

    # 2. Special Eggs (Indices 20-24 -> IDs 50-54)
    for i in range(20, min(25, egg_totals_len)):
        egg_id = i + 30
        name = ei_pb2.Egg.Name(egg_id).lower()
        egg_counts[egg_id] = {"egg_id": egg_id, "egg_type": name, "count": egg_totals_list[i]}

    # 3. Contract & Custom Eggs
    # Combine both active contracts and archived contracts
    all_contracts = list(backup.contracts.contracts or []) + list(backup.contracts.archive or [])

    # Contract-only eggs that should always be calculated from contracts
    contract_only_eggs = [
        ei_pb2.Egg.CHOCOLATE,
        ei_pb2.Egg.EASTER,
        ei_pb2.Egg.WATERBALLOON,
        ei_pb2.Egg.FIREWORK,
        ei_pb2.Egg.PUMPKIN
    ]

    # Helper function to get contribution from a contract
    def get_contribution(local_contract):
        # Priority: coopLastUploadedContribution > lastAmountWhenRewardGiven > 0
        return (
            getattr(local_contract, "coop_last_uploaded_contribution", None) or
            getattr(local_contract, "last_amount_when_reward_given", None) or
            0.0
        )

    # Calculate eggs laid for contract-only eggs (100-104)
    for egg_id in contract_only_eggs:
        egg_name = ei_pb2.Egg.Name(egg_id).lower()
        total = sum(
            get_contribution(c) for c in all_contracts
            # Only count contracts where egg matches AND no custom_egg_id is set
            if c.contract and c.contract.egg == egg_id and not c.contract.HasField("custom_egg_id")
        )
        egg_counts[egg_id] = {"egg_id": egg_id, "egg_type": egg_name, "count": total}

    # Calculate custom eggs (each custom egg gets its own entry)
    custom_egg_totals = {}
    for local_contract in all_contracts:
        if not local_contract.contract:
            continue

        contract_meta = local_contract.contract
        # Check if custom_egg_id field exists AND has a non-empty value
        if contract_meta.HasField("custom_egg_id") and contract_meta.custom_egg_id:
            custom_id = contract_meta.custom_egg_id.strip()
            if custom_id:  # Double-check it's not just whitespace
                contribution = get_contribution(local_contract)
                custom_egg_totals[custom_id] = custom_egg_totals.get(custom_id, 0.0) + contribution

    # Add custom eggs to egg_counts - use custom_id as part of the key
    for custom_id, total in custom_egg_totals.items():
        # Use a unique key for each custom egg (e.g., "custom_silicon", "custom_carbon-fiber")
        egg_key = f"custom_{custom_id.lower()}"
        egg_name = f"custom_{custom_id.lower()}"
        egg_counts[egg_key] = {"egg_id": 200, "egg_type": egg_name, "count": total}

    return {
        "egg_inc_id": x_egg_inc_id,
        "total_eggs": list(egg_counts.values()),
        "boosts_used": stats.boosts_used,
        "video_doubler_uses": stats.video_doubler_uses,
        "drone_takedowns": stats.drone_takedowns,
        "drone_takedowns_elite": stats.drone_takedowns_elite,
        "num_prestiges": stats.num_prestiges,
        "num_piggy_breaks": stats.num_piggy_breaks,
        "iap_packs_purchased": stats.iap_packs_purchased,
        "piggy_full": stats.piggy_full,
        "piggy_found_full": stats.piggy_found_full,
        "time_piggy_filled_realtime": stats.time_piggy_filled_realtime,
        "time_piggy_full_gametime": stats.time_piggy_full_gametime,
        "lost_piggy_increments": stats.lost_piggy_increments,
    }
