#    authhandler.py
#    Copyright (C) 2021  Alexander Schillemans
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

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

	def getAuthURL(self, redirectUri):
		self.redirectUri = redirectUri
		oauth = OAuth2Session(self.clientId, redirect_uri=self.redirectUri, scope='openid')
		authorizationUrl, self.state = oauth.authorization_url(self.authUrl)
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
