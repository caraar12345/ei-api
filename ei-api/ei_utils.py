import base64
import math
import requests
import re
import sys

sys.path.append("ei-api/")

import proto.gen.ei_pb2 as ei_pb2
from constants import *

from fastapi import HTTPException, Header


def load_ei_first_contact_data(
    egg_inc_id,
) -> tuple[ei_pb2.EggIncFirstContactResponse, bool]:
    first_contact_req = ei_pb2.EggIncFirstContactRequest()
    first_contact_req.ei_user_id = egg_inc_id
    first_contact_req.client_version = 45

    first_contact_url = "https://www.auxbrain.com/ei/bot_first_contact"
    first_contact_data = {
        "data": base64.b64encode(first_contact_req.SerializeToString()).decode("utf-8")
    }
    response = requests.post(first_contact_url, data=first_contact_data)

    first_contact_response = ei_pb2.EggIncFirstContactResponse()
    first_contact_response.ParseFromString(base64.b64decode(response.text))
    if first_contact_response.error_message:
        return first_contact_response, False
    return first_contact_response, True


def verify_egg_inc_id(x_egg_inc_id: str | None = Header(default=None)) -> bool:
    # Check egg_inc_id is in the query string
    if x_egg_inc_id == None:
        raise HTTPException(status_code=400, detail="X-Egg-Inc-ID header missing")

    # Check that the egg_inc_id fits the expected format
    ei_id_pattern = re.compile("^EI[0-9]{16}$")
    if not ei_id_pattern.match(x_egg_inc_id):
        raise HTTPException(status_code=400, detail="X-Egg-Inc-ID header invalid")

    return True


def get_soul_power_oom(soul_power):
    return math.floor(max(soul_power, 0))


def get_farmer_role(oom):
    return (
        MAP_OOM_FARMER_ROLE[str(oom)]
        if oom < len(MAP_OOM_FARMER_ROLE)
        else MAP_OOM_FARMER_ROLE[str(len(MAP_OOM_FARMER_ROLE) - 1)]
    )
