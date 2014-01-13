#!/usr/bin/env python
#coding: utf-8

from webim import Client, Endpoint, Message

endpoint = Endpoint('uid1', 'user1')

client = Client(endpoint, "localhost", "public", timeout=30)

status, respdata = client.online(['uid1', 'uid2', 'uid3'], ['grp1'])

if status != 200:
	print "online error:"
	print respdata

else:
	while(True): print client.poll()

