import requests
from requests_oauthlib import OAuth2Session
import json
import sys
import webbrowser
from config import *
from cachehandler import CacheHandler
from authhandler import AuthHandler
from api import OpenbravoToBanqupAPI
from datetime import timedelta, date

def paid_invoice(document):

	api = OpenbravoToBanqupAPI(bq_client_id,bq_client_secret)
	authUrl = api.authHandler.getAuthURL(bq_redirect_uri)
	webbrowser.open(authUrl)
	response = input('Paste response: ')
	token = api.authHandler.retrieveToken(response, redirectUri=bq_redirect_uri)
	#print(token)
	invoice_list = api.get('sales-invoices?client_id='+banqup_client_id+'&sales_invoice_number='+document,None,None)
	if not invoice_list[2]['results']:
		print('***********************')
		print('The invoice number provided does not exist in the Banqup portal.')
		print('Please verify and try again.')
		print('***********************')
		return
	invoice_id = str(invoice_list[2]['results'][0]['id'])
	#print(invoice_id)
	payload = json.dumps({
		"type": "MARK_AS_PAID"
	})
	invoice_action = api.post('sales-invoices/'+invoice_id+'/action',json.loads(payload),None,None)
	print(invoice_action)


if __name__ == '__main__':
	paid_invoice(str(sys.argv[1]))
