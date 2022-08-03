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
  traces_sample_rate=1.0,
)

import falcon
import json
import re

import sys
sys.path.append('ei-api/')

import proto.gen.ei_pb2 as ei_pb2
from constants import *
from ei_utils import load_ei_first_contact_data
from google.protobuf.json_format import MessageToJson

class FullBackupResource:
    def on_get(self, req, resp):
      # Check egg_inc_id is in the query string
      try:
        egg_inc_id = req.params['egg_inc_id']
      except KeyError:
        resp.status = falcon.HTTP_400
        resp.text = json.dumps({'error': 'No egg_inc_id provided'})
        return

      # Check that the egg_inc_id fits the expected format
      ei_id_pattern = re.compile("^EI[0-9]{16}$")
      if not ei_id_pattern.match(egg_inc_id):
        resp.status = falcon.HTTP_400
        resp.text = json.dumps({'error': 'Invalid egg_inc_id'})
        return
      
      first_contact_resp = load_ei_first_contact_data(egg_inc_id)
      resp.text = MessageToJson(first_contact_resp, preserving_proto_field_name=True)
