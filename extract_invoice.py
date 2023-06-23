import requests
import json
import sys
from config import *

def extract_invoice(document):
	
	url = ob_api_url+"Invoice?_where=documentNo='"+document+"'&_noActiveFilter=false"

	payload = {}
	headers = {
	  'Authorization': 'Basic '+userpass_b64
	}

	response = requests.request("GET", url, headers=headers, data=payload) #extracts invoice header

	#print(response.text)
	invoice = json.loads(response.text)
	#print (invoice['response']['data'][0]['client'])

	url = ob_api_url+"InvoiceLine?_where=invoice='"+invoice['response']['data'][0]['id']+"'&_noActiveFilter=false"

	response = requests.request("GET", url, headers=headers, data=payload) #extracts invoice lines
	#print(response.text)
	lines = json.loads(response.text)['response']['data']
	lines_json = json.dumps(lines)
	#print(lines_json)
	lines = json.loads(lines_json)
	lines_output = '['
	first_line = True
	for key in lines:
		#print (key)
		linetemp_json = json.dumps(key)
		linetemp = json.loads(linetemp_json)
		if linetemp['product'] != None:
			if not first_line:
				lines_output = lines_output+','
			first_line = False
			lines_output = lines_output + '{"service_name": "'+linetemp['product']+'","service_description": "'+linetemp['product$_identifier']+'","service_quantity": '+str(linetemp['invoicedQuantity'])+',"service_price": '+str(linetemp['unitPrice'])+',"service_vat": '+'8'+'}'
	lines_output = lines_output+']'
	#print(lines_output)

	payload = json.dumps({
	    "sales_invoice_number": invoice['response']['data'][0]['documentNo'],
	    "sales_invoice_date": invoice['response']['data'][0]['invoiceDate']+"T00:00:00Z",
	    "sales_invoice_due_date": "2023-06-17T00:00:00Z", #needs to be replaced by invoiceDate+"daysTillDue"
	    "platform_id": banqup_platform_id,
	    "debtor_id": 136328, #needs to be fetch from database using the "client_debtor_number"
	    "currency_code": invoice['response']['data'][0]['currency$_identifier'],
	    "client_id": banqup_client_id,
	    "delivery_channel": "openpeppol",
	    "invoice_lines": json.loads(lines_output)
	})
	print(payload)

if __name__ == '__main__':
	extract_invoice(str(sys.argv[1]))
