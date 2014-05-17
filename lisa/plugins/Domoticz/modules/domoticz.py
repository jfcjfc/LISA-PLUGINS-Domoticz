# -*- coding: UTF-8 -*-
#
# V0.12
#
#
#
#
# V001 juste test de son
#  introduction de import requests (V002) et de fichier xml (V003) pour les parametres.
# 	(importation bibliotheque 'xml.dom.minidom' ????)
#
#
# from datetime import datetime
from lisa.server.plugins.IPlugin import IPlugin
import gettext
import inspect
import os
import requests


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
        return {"plugin": "Domoticz",
                "method": "devices",
                "body": self._('temperature')
        }

    def switchlight(self, jsonInput):
# url6off = 'http://127.0.0.1:8080/json.hTwm?type=command&param=switchlight&idx=6&switchcmd=Off&level=0'
# /json.htm?type=command&param=switchlight&idx=&switchcmd=&level=0
# resp = requests.get(url6on, auth=('XXXX','YYYYY'))
# entities : wit/location, wit/on_off
# wit/location = salon, bureau un, bureau deux.
# wit/location = on, off
	if jsonInput['outcome']['entities']['wit/location']['value'] :
		location = jsonInput['outcome']['entities']['wit/location']['value']
	else:
		body = self._('probleme un')
#
        if jsonInput['outcome']['entities']['wit/on_off']['value'] :
                on_off = jsonInput['outcome']['entities']['wit/location']['value']
	else:
		body = self._('probleme deux')
#
	if location = "bureau deux" and on_off ="on" :
		resp = requests.get ('http://127.0.0.1:8080/json.htm?type=command&param=switchlight&idx=xx&switchcmd=On&level=0')
	elif location = "bureau deux" and on_off ="off" :
		resp = requests.get ('http://127.0.0.1:8080/json.htm?type=command&param=switchlight&idx=xx&switchcmd=Off&level=0')
	else:
 		body = self._('probleme trois')
#
        return {"plugin": "Domoticz",
                "method": "switchlight",
                "body": self._('lumiere')
        }

    def heatingcontrol(self, jsonInput):
        return {"plugin": "Domoticz",
                "method": "heatingcontrol",
                "body": self._('chaudiere')
        }
