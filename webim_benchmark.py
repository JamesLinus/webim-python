#!/usr/bin/env python
#coding: utf-8

from webim import Client

user = {
    'id': 'uid1', 
    'nick': 'user1', 
    'show': 'available', 
    'status': ''
}

client = Client(user, "localhost", "public", timeout=30)

status, respdata = client.online(['uid1', 'uid2', 'uid3'], ['grp1'])

if status != 200:
	print "online error:"
	print respdata

else:
	while(True): print client.poll()

