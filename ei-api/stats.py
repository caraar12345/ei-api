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

class StatsResource:
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
      doc = {
          'total_eggs': {
            '01_edible': first_contact_resp.backup.stats.egg_totals[EGG_TOTALS_IDS["edible"]],
            '02_superfood': first_contact_resp.backup.stats.egg_totals[EGG_TOTALS_IDS["superfood"]],
            '03_medical': first_contact_resp.backup.stats.egg_totals[EGG_TOTALS_IDS["medical"]],
            '04_rocket_fuel': first_contact_resp.backup.stats.egg_totals[EGG_TOTALS_IDS["rocket_fuel"]],
            '05_super_material': first_contact_resp.backup.stats.egg_totals[EGG_TOTALS_IDS["super_material"]],
            '06_fusion': first_contact_resp.backup.stats.egg_totals[EGG_TOTALS_IDS["fusion"]],
            '07_quantum': first_contact_resp.backup.stats.egg_totals[EGG_TOTALS_IDS["quantum"]],
            '08_immortality': first_contact_resp.backup.stats.egg_totals[EGG_TOTALS_IDS["immortality"]],
            '09_tachyon': first_contact_resp.backup.stats.egg_totals[EGG_TOTALS_IDS["tachyon"]],
            '10_graviton': first_contact_resp.backup.stats.egg_totals[EGG_TOTALS_IDS["graviton"]],
            '11_dilithium': first_contact_resp.backup.stats.egg_totals[EGG_TOTALS_IDS["dilithium"]],
            '12_prodigy': first_contact_resp.backup.stats.egg_totals[EGG_TOTALS_IDS["prodigy"]],
            '13_terraform': first_contact_resp.backup.stats.egg_totals[EGG_TOTALS_IDS["terraform"]],
            '14_antimatter': first_contact_resp.backup.stats.egg_totals[EGG_TOTALS_IDS["antimatter"]],
            '15_dark_matter': first_contact_resp.backup.stats.egg_totals[EGG_TOTALS_IDS["dark_matter"]],
            '16_ai': first_contact_resp.backup.stats.egg_totals[EGG_TOTALS_IDS["ai"]],
            '17_nebula': first_contact_resp.backup.stats.egg_totals[EGG_TOTALS_IDS["nebula"]],
            '18_universe': first_contact_resp.backup.stats.egg_totals[EGG_TOTALS_IDS["universe"]],
            '19_enlightenment': first_contact_resp.backup.stats.egg_totals[EGG_TOTALS_IDS["enlightenment"]]
          },
          'boosts_used': first_contact_resp.backup.stats.boosts_used,
          'video_doubler_uses': first_contact_resp.backup.stats.video_doubler_uses,
          'drone_takedowns': first_contact_resp.backup.stats.drone_takedowns,
          'drone_takedowns_elite': first_contact_resp.backup.stats.drone_takedowns_elite,
          'num_prestiges': first_contact_resp.backup.stats.num_prestiges,
          'num_piggy_breaks': first_contact_resp.backup.stats.num_piggy_breaks,
          'iap_packs_purchased': first_contact_resp.backup.stats.iap_packs_purchased,
          'piggy_full': first_contact_resp.backup.stats.piggy_full,
          'piggy_found_full': first_contact_resp.backup.stats.piggy_found_full,
          'time_piggy_filled_realtime': first_contact_resp.backup.stats.time_piggy_filled_realtime,
          'time_piggy_full_gametime': first_contact_resp.backup.stats.time_piggy_full_gametime,
          'lost_piggy_increments': first_contact_resp.backup.stats.lost_piggy_increments,
        }
      resp.text = json.dumps(doc)