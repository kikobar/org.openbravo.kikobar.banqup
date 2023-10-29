#    cachehandler.py
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
import config

class CacheHandler:

	def __init__(self):
		self.rootDir = Path(__file__).parent.absolute()
		self.cacheDir = '{root}/cache'.format(root=self.rootDir)

	def getCache(self, key):
		if key in config.CACHE[key]: return config.CACHE[key]
		keyPath = '{cache}/{key}.txt'.format(cache=self.cacheDir, key=key)

		try:
			with open(keyPath, 'r') as f:
				value = f.readlines()[0]
			config.CACHE[key] = value
			return value

		except IOError:
			return None

	def setCache(self, key, value):
		keyPath = '{cache}/{key}.txt'.format(cache=self.cacheDir, key=key)

		try:
			with open(keyPath, 'w+') as f:
				f.write(value)

			config.CACHE[key] = value
			return value

		except IOError:
			return None
