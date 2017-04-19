#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json

class Client:
	def __init__(self, Key = None, URL = 'http://api.apixu.com/v1/'):
		self.Key = Key
		self.URL = URL

	def getCurrentWeatherWith(self, Query = None):
		url = self.URL + 'current.json?key=' + self.Key + '&q=' + Query
		return requests.get(url).json()

	def getForecastWeatherWith(self, Query = None, Days = None):
		url = self.URL + 'forecast.json?key=' + self.Key + '&q=' + Query +',days=' + Days
		return requests.get(url).json()
		

