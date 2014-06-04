#
import gettext
import inspect
import os
import json
import requests
json_data=open('domoticz.json')
data = json.load(json_data)
res1 = data['param_dz'] 
ipc = data['configuration']

idex = "bureau_deux_on"

for rs in res1:
#	# print "*** ", rs
#	print rs['ids']
# affichage ligne et index
	if rs['ids'] == idex :
		print "zzzz++W ", rs ,
		# print "$$$$$$$$", res1.index(rs)
		rss = rs
print "$$$$$$$$", res1.index(rss)
print 

resp = requests.get ('http://192.168.0.3:8080/json.htm?type=command&param=switchlight&idx=59&switchcmd=On&level=0')
print "$$$ => ", resp
