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

content = client.online(['uid1', 'uid2', 'uid3'], ['room1'])

print "Response: "

print content

while(True): print client.poll()

