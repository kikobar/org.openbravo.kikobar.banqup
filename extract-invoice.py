import requests
from config import *

url = ob_api_url+"Invoice?_where=documentNo='1001649'&_noActiveFilter=false"

payload = {}
headers = {
  'Authorization': 'Basic '+userpass_b64
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

