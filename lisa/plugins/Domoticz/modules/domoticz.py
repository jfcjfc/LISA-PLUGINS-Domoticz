# -*- coding: UTF-8 -*-
#
# V0.3
#
# manque scenario et panel securité
# manque devices -temp
# doit marcher et a tester on/off - switch et HC 
#
from lisa.server.plugins.IPlugin import IPlugin
import gettext
import inspect
import os
import requests
#
import json
json_data=open('domoticz2.json')
data = json.load(json_data)
res1 = data['param_dz']
ipc = data['configuration']

# #######################
# besoin données jsoninput
# temperature : ['outcome']['entities']['wit/temperature']['value']
# lieu : ['outcome']['entities']['wit/location']['value'] 
# on/ off : ['outcome']['entities']['wit/on_off']['value'] 
# methode :  :['outcome']['entities']["configuration"][intents]   "dz_devices": {"method":
#
# #######################

inconf = ipc["ip"]
pt = ipc["port"]

if jsonInput['outcome']['entities']['wit/temperature']['value'] :
	location = jsonInput['outcome']['entities']['wit/temperature']['value']
else:
	body = self._('pas de temperature')

if jsonInput['outcome']['entities']['wit/location']['value'] :
	location = jsonInput['outcome']['entities']['wit/location']['value']
else:
	body = self._('pas de lieu')

if jsonInput['outcome']['entities']['wit/on_off']['value'] :
	on_off = jsonInput['outcome']['entities']['wit/on_off']['value']
else:
	body = self._('pas de on/off')

idex= location + "_" + on_off

# #######################  EX #####
# recherche et variable rss[]
# "ids" : "bureau_deux_on",
# "meth" : "switchlight", 
# "idx" : "59",
# "idx_sec" : "",
# "boy" : "la lumiere bureau deux est allume"
# #################################

for rs in res1:
	if rs['ids'] == idex :
		rss = rs

class Domoticz(IPlugin):
	def __init__(self):
		super(Domoticz, self).__init__()
		self.configuration_plugin = self.mongo.lisa.plugins.find_one({"name": "Domoticz"})
		self.path = os.path.realpath(os.path.abspath(os.path.join(os.path.split(
		inspect.getfile(inspect.currentframe()))[0],os.path.normpath("../lang/"))))
		self._ = translation = gettext.translation(domain='domoticz',
			localedir=self.path,
                        languages=[self.configuration_lisa['lang']]).ugettext

	def devices(self, jsonInput):
	#	http://192.168.0.3:8080/json.htm?type=devices&filter=temp&rid=74
	# parse result : Temp
		return {"plugin": "Domoticz",
			"method": "devices",
			"body": self._(rss(boy))
	}
	
	def switchlight(self, jsonInput):
		resp = requests.get ('http://192.168.0.3:8080/json.htm?type=command&param=switchlight&idx=%02d&switchcmd=%s&level=0' % (rss[idx],on_off.capitalize()))
		return {"plugin": "Domoticz",
			"method": "switchlight",
			"body": self._(rss(boy))
	}

	def heatingcontrol(self, jsonInput):
		resp = requests.get ('http://192.168.0.3:8080/json.htm?type=command&param=switchlight&idx=%02d&switchcmd=%s&level=0' % (rss[idx],on_off))
		return {"plugin": "Domoticz",
			"method": "heatingcontrol",
			"body": self._(rss(boy))
	
