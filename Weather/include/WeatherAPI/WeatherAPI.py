#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json

from sys import exit

class Client:
	def __init__(self, Key = None, URL = 'http://api.apixu.com/v1/'):
		self.Key = Key
		self.URL = URL

	def getCurrentWeatherWith(self, Query = None, ErrorDie = True):
		url = self.URL + 'current.json?key=' + self.Key + '&q=' + Query
		if ErrorDie == True:
			return self.checkAPIResponseForErrors(Data = requests.get(url).json())
		else:
			return requests.get(url).json()

	def getForecastWeatherWith(self, Query = None, Days = None, ErrorDie = True):
		url = self.URL + 'forecast.json?key=' + self.Key + '&q=' + Query +',days=' + Days
		if ErrorDie == True:
			return self.checkAPIResponseForErrors(Data = requests.get(url).json())
		else:
			return requests.get(url).json()

	def checkAPIResponseForErrors(self, Data = None):
		if "error" in Data:
			print "(!) ERROR " + str(Data["error"]["code"]) + ": " + Data["error"]["message"]
			exit()
		else: 
			return Data