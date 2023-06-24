import requests
from requests_oauthlib import OAuth2Session
import json
import sys
import webbrowser
from config import *
from cachehandler import CacheHandler
from authhandler import AuthHandler
from api import OpenbravoToBanqupAPI

api = OpenbravoToBanqupAPI(bq_client_id,bq_client_secret)
authUrl = api.authHandler.getAuthURL(bq_redirect_uri)
print(authUrl)
webbrowser.open(authUrl)
response = input('paste response: ')
token = api.authHandler.retrieveToken(response, redirectUri=bq_redirect_uri)
print(token)
businessPartner='BCD9D8F839AE46BF8481F20A71EF467C'
debtor_list = api.get('debtors?client_id='+banqup_client_id+'&client_debtor_number='+businessPartner,None,None)
print(debtor_list)
print(debtor_list[0])
print(debtor_list[1])
print(debtor_list[2])
print(debtor_list[2]['results'])
print(debtor_list[2]['results'][0])
print(debtor_list[2]['results'][0]['id'])
print(debtor_list[2]['results'][0]['preferred_channel'])

