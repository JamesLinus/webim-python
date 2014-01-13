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
        self.user = {
                'id': 'uid1', 
                'nick': 'user1', 
                'show': 'available', 
                'status': ''}
        self.client = Client(self.user, "localhost", "public")

        self.buddies = ['uid1', 'uid2', 'uid3']
        self.groups = ['grp1', 'grp2', 'grp3']
        self.client.online(self.buddies, self.groups)
    
    def test_online(self):
        status, resp = self.client.online(self.buddies, self.groups)
        self.assertEqual(status, 200)
        self.assertTrue(resp['success'])

    def test_presence(self):
        presence = {
            'type': 'show',
            'show':  'away',
            'status': 'Away' 
            }
        status, resp = self.client.presence(presence)
        self.assertEqual(status, 200)

    def test_message(self):
        message = {
            'to': 'uid2',
            'nick': 'user1',
            'body': 'hahaha',
            'timestamp': time.time()*1000,
            'type': 'chat',
            'style': '' 
                }
        status, resp = self.client.message(message)
        self.assertEqual(status, 200)

    def test_push(self):
        c = Client(self.user, "localhost", "public")
        message = {
            'to': 'uid2',
            'nick': 'user3',
            'body': 'hahaha',
            'timestamp': time.time()*1000,
            'type': 'chat',
            'style': '' 
                }
        status, resp = c.push("uid3", message) 
        self.assertEqual(status, 200)
    
    def test_status(self):
        status = {
            'to': 'uid2',
            'show': 'typeing',
            'status': 'user1 is typing' 
                }
        status, resp = self.client.status(status)
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


