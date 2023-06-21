import requests
import json
import sys
from config import *

document = str(sys.argv[1])

url = ob_api_url+"Invoice?_where=documentNo='"+document+"'&_noActiveFilter=false"

payload = {}
headers = {
  'Authorization': 'Basic '+userpass_b64
}

response = requests.request("GET", url, headers=headers, data=payload) #extracts invoice header

print(response.text)
invoice = json.loads(response.text)
#print (invoice['response']['data'][0]['client'])

url = ob_api_url+"InvoiceLine?_where=invoice='"+invoice['response']['data'][0]['id']+"'&_noActiveFilter=false"

response = requests.request("GET", url, headers=headers, data=payload) #extracts invoice lines
print(response.text)



payload = json.dumps({
    "sales_invoice_number": invoice['response']['data'][0]['documentNo'],
    "sales_invoice_date": invoice['response']['data'][0]['invoiceDate']+"T00:00:00Z",
    "sales_invoice_due_date": "2023-06-17T00:00:00Z", #needs to be replaced by invoiceDate+"daysTillDue"
    "platform_id": banqup_platform_id,
    "debtor_id": 136328, #needs to be fetch from database using the "client_debtor_number"
    "currency_code": invoice['response']['data'][0]['currency$_identifier'],
    "client_id": banqup_client_id,
    "delivery_channel": "openpeppol",
    "invoice_lines": [
        {
            "service_name": "161218",
            "service_description": "Cavendish Banana 18.8Kg BOX",
            "service_quantity": 10,
            "service_price": 1.75,
            "service_vat": 8
        }
    ]
})
print(payload)
