#!/usr/bin/env python
#coding: utf-8

"""
python webim client test

"""

import time
import unittest

from webim import Client, Endpoint, Status, Message, Presence

class TestWebimMethods(unittest.TestCase):

    def setUp(self):
        self.endpoint = Endpoint('uid1', 'user1')
        self.client = Client(self.endpoint, "localhost", "public")

        self.buddies = ['uid1', 'uid2', 'uid3']
        self.groups = ['grp1', 'grp2', 'grp3']
        self.client.online(self.buddies, self.groups)
    
    def test_online(self):
        status, resp = self.client.online(self.buddies, self.groups)
        self.assertEqual(status, 200)
        self.assertTrue(resp['success'])

    def test_presence(self):
        status, resp = self.client.presence(Presence('online', 'away', 'Away'))
        self.assertEqual(status, 200)

    def test_message(self):
        status, resp = self.client.message(Message('uid2', 'user1', 'hahahha', time.time()*1000))
        self.assertEqual(status, 200)

    def test_push(self):
        c = Client(self.endpoint, "localhost", "public")
        status, resp = c.push("uid3", Message('uid2', 'user3', 'hahahha', time.time()*1000)) 
        self.assertEqual(status, 200)
    
    def test_status(self):
        status, resp = self.client.status(Status('uid2', 'typing', 'User1 is typing'))
        self.assertEqual(status, 200)

    def test_presences(self):
        status, resp = self.client.presences(['uid1', 'uid2'])
        self.assertEqual(status, 200)

    def test_members(self):
        status, resp = self.client.members("gid1")
        self.assertEqual(status, 200)

    def test_join(self):
        status, resp = self.client.join("gid4")
        self.assertEqual(status, 200)

    def test_leave(self):
        status, resp = self.client.leave("gid4")
        self.assertEqual(status, 200)


if __name__ == '__main__':
    unittest.main()


