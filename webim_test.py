#!/usr/bin/env python
#coding: utf-8

"""
python webim client test

"""

import time
import unittest

from webim import Client

class TestWebimMethods(unittest.TestCase):

    def setUp(self):
        self.endpoint = {
                'id': 'uid1', 
                'nick': 'user1', 
                'show': 'available', 
                'status': ''}
        self.client = Client(self.endpoint, "localhost", "public", host="t.nextalk.im")

        self.buddies = ['uid1', 'uid2', 'uid3']
        self.rooms = ['room1', 'room2', 'room3']
        self.client.online(self.buddies, self.rooms)
    
    def test_online(self):
        resp = self.client.online(self.buddies, self.rooms)
        self.assertTrue(resp['success'])

    def test_presence(self):
        self.client.presence('away', 'Away')

    def test_message(self):
        message = {
            'to': 'uid2',
            'nick': 'user1',
            'body': 'hahaha',
            'timestamp': time.time()*1000,
            'type': 'chat',
            'style': '' 
                }
        self.client.message(message)

    def test_push(self):
        c = Client(self.endpoint, "localhost", "public", host="t.nextalk.im")
        message = {
            'to': 'uid2',
            'from': 'uid3',
            'nick': 'user3',
            'body': 'hahaha',
            'timestamp': time.time()*1000,
            'type': 'chat',
            'style': '' 
        }
        c.message(message) 
    
    def test_status(self):
        status = {
            'to': 'uid2',
            'show': 'typeing',
            'status': 'user1 is typing' 
        }
        self.client.status(status)

    def test_presences(self):
        self.client.presences(['uid1', 'uid2'])

    def test_members(self):
        self.client.members("gid1")

    def test_join(self):
        self.client.join("gid4")

    def test_leave(self):
        self.client.leave("gid4")

if __name__ == '__main__':
    unittest.main()



