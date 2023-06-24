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
