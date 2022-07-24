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

import sys
sys.path.append('ei-api/')

app = application = falcon.App()

from .stats import StatsResource
stats = StatsResource()
app.add_route('/stats', stats)

from .contracts import ContractResource
contracts = ContractResource()
app.add_route('/contracts', contracts)