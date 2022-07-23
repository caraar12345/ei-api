import base64
import requests
import sys
sys.path.append('ei-api/')

import proto.gen.ei_pb2 as ei_pb2
from constants import *

def load_ei_first_contact_data(egg_inc_id):
  first_contact_req = ei_pb2.EggIncFirstContactRequest()
  first_contact_req.ei_user_id = egg_inc_id
  first_contact_req.client_version = 38

  first_contact_url = 'https://www.auxbrain.com/ei/bot_first_contact'
  first_contact_data = { 'data' : base64.b64encode(first_contact_req.SerializeToString()).decode('utf-8') }
  response = requests.post(first_contact_url, data = first_contact_data)

  first_contact_response = ei_pb2.EggIncFirstContactResponse()
  first_contact_response.ParseFromString(base64.b64decode(response.text))
  
  return first_contact_response
