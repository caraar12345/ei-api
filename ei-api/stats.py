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
    if ok != True:
        raise HTTPException(400, detail=first_contact_resp.error_message)

    egg_totals = first_contact_resp.backup.stats.egg_totals
    egg_counts = []
    for egg_id in range(1, len(egg_totals) + 1):
        egg_counts.append(
            {
                "egg_id": egg_id,
                "egg_type": ei_pb2.Egg.Name(egg_id).lower(),  # type: ignore -- it works fine, shush pyright
                "count": egg_totals[egg_id - 1],
            }
        )

    out_doc = {
        "egg_inc_id": x_egg_inc_id,
        "total_eggs": egg_counts,
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
    return out_doc
