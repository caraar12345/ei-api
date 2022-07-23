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

import os
import base64
import requests
import falcon
import json

import sys
sys.path.append('ei-api/')

import proto.gen.ei_pb2 as ei_pb2
from constants import *
from ei_utils import load_ei_first_contact_data

from .stats import StatsResource

app = application = falcon.App()

stats = StatsResource()
app.add_route('/stats', stats)
