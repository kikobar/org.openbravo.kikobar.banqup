#    api.py
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

import requests
from requests_oauthlib import OAuth2Session
import json
import sys
from config import *
from cachehandler import CacheHandler
from authhandler import AuthHandler

class OpenbravoToBanqupAPI:

	def __init__(self, clientId, clientSecret, demo=False):
		self.clientId = clientId
		self.clientSecret = clientSecret
		self.demo = demo
		self.headers = {
			'Accept' : 'application/json',
			'Content-Type' : 'application/json',
		}
		self.baseUrl = bq_base_url
		self.cacheHandler = CacheHandler()
		self.authHandler = AuthHandler(self, self.clientId, self.clientSecret)

	def doRequest(self, method, url, data=None, headers=None, files=None):
		if headers:
			mergedHeaders = self.headers
			mergedHeaders.update(headers)
			headers = mergedHeaders
		else: headers = self.headers

		reqUrl = '{base}/{url}'.format(base=self.baseUrl, url=url)

		if method == 'GET':
			response = requests.get(reqUrl, params=data, headers=headers)
		elif method == 'POST':
			if files: response = requests.post(reqUrl, data=json.dumps(data), files=files, headers=headers)
			else: response = requests.post(reqUrl, data=json.dumps(data), headers=headers)
		elif method == 'PUT':
			response = requests.put(reqUrl, data=json.dumps(data), headers=headers)
		elif method == 'DELETE':
			response = requests.delete(reqUrl, params=json.dumps(data), headers=headers)
		return response

	def request(self, method, url, data=None, headers=None, files=None):

		self.authHandler.checkHeaderTokens()
		response = self.doRequest(method, url, data, headers, files)

		if response.status_code != 204:
			if 'json' in response.headers['Content-Type']:
				respContent = response.json()
			elif 'pdf' in response.headers['Content-Type']:
				respContent = response.content
		else:
			respContent = ''

		return response.status_code, response.headers, respContent

	def get(self, url, data=None, headers=None):
		status, headers, response = self.request('GET', url, data, headers)
		return status, headers, response

	def post(self, url, data=None, headers=None, files=None):
		status, headers, response = self.request('POST', url, data, headers, files)
		return status, headers, response

	def put(self, url, data=None, headers=None):
		status, headers, response = self.request('PUT', url, data, headers)
		return status, headers, response

	def delete(self, url, data=None, headers=None):
		status, headers, response = self.request('DELETE', url, data, headers)
		return status, headers, response
