from pathlib import Path
from requests_oauthlib import OAuth2Session
import config


class AuthHandler:

	def __init__(self, api, clientId, clientSecret):
		self.clientId = clientId
		self.clientSecret = clientSecret
		self.api = api
		self.cacheHandler = api.cacheHandler
		self.authUrl = config.bq_auth_url
		self.tokenUrl = config.bq_access_token_url
		self.redirectUri = None
		self.state = None
		self.token = None

	def getAuthURL(self, redirectUrl):
		self.redirectUrl = redirectUrl
		oauth = OAuth2Session(self.clientId, redirect_uri=self.redirectUri, scope='openid')
		return authorizationUrl

	def retrieveToken(self, response, state=None, redirectUri=None):
		if not redirectUri:
			if not self.redirectUri: print('redirect uri is not found. init the auth flow first or give the uri as a parameter.')
			redirectUri = self.redirectUri
		if not state:
			if not self.state: print('state is not found. init the auth flow first or give the state as a parameter.')
		state = self.state
		oauth = OAuth2Session(self.clientId, state=state, redirect_uri=redirectUri)
		oauthToken = oauth.fetch_token(self.tokenUrl, client_secret=self.clientSecret,authorization_response=response)
		self.token = oauth._client.access_token
		self.cacheHandler.setCache(self.clientId, self.token)
		return self.token

	def getToken(self):
		if self.token: return self.token
		print('token is not found. init the auth flow first.')

	def setTokenHeader(self, token):
		bearerStr = 'Bearer {token}'.format(token=token)
		self.api.headers.update({'Authorization' : bearerStr})

	def checkHeaderTokens(self):
		if 'Authorization' not in self.api.headers:
			token = self.cacheHandler.getCache(self.clientId)
			if token is None: token = self.getToken()
			self.setTokenHeader(token)
