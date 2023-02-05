from fastapi import APIRouter, Depends, Header, HTTPException
import os

import json

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
from .ei_utils import load_ei_first_contact_data, verify_egg_inc_id
from google.protobuf.json_format import MessageToJson

router = APIRouter(
    prefix="/full_backup",
    dependencies=[Depends(verify_egg_inc_id)],
    responses={404: {"description": "Not found"}},
    tags=["Full backup"],
)


@router.get(
    "/",
    name="GameBackupJSON",
    summary="JSON blob of full Egg, Inc. data backup from Auxbrain servers",
)
def get_full_backup(x_egg_inc_id: str | None = Header(default=None)):
    first_contact_resp, ok = load_ei_first_contact_data(x_egg_inc_id)
    if ok != True:
        raise HTTPException(400, detail=first_contact_resp.error_message)

    return json.loads(
        MessageToJson(first_contact_resp, preserving_proto_field_name=True)
    )
