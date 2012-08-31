# -*- coding: utf-8 *-*
# Filename: smspilot.py
'''
SMSPilot.ru API 2.x Usage Implementation
by Stanislav Sokolov aka Ratso
v. 1.1
'''

import json
import urllib2
import re
import random


class Sender:
    service_url = u"http://smspilot.ru/api2.php"
    defaultSender = u"Friend"
    headers = {
        'Content-type': 'application/json',
        'Accept': 'text/plain'
    }

    def __init__(self, api_key):
        if not api_key:
            raise Exception(u"API Key is not defined")
        self.api = api_key
        self.messages = []

    def checkPhone(self, phone):
        phonePattern = re.compile(r'(^7[0-9]+)$', re.VERBOSE)
        return phone is not None and phonePattern.search(phone)

    def checkSender(self, sender):
        regxPattern = re.compile(r'^[a-zA-Z.\-\d]{3,11}$', re.VERBOSE)
        return regxPattern.search(sender)

    def addSMS(self, phone, body, sender=None):
        if not self.checkPhone(phone):
            raise Exception(u"Not valid phone number")
        if len(body) == 0:
            raise Exception(u"Too short message")
        if sender == None:
            sender = self.defaultSender
        if not self.checkSender(sender):
            raise Exception(u"Invalid sender name or phone")
        message = {
            u"id": random.choice(range(1, 9999)),
            u"from": sender,
            u"to": phone,
            u"text": body
        }
        self.messages.append(message)
        return True

    def batchsend(self, phones, body, sender=None, resetQueue=True):
        if phones == None:
            raise Exception(u"No phones in list")
        if resetQueue:
            self.messages = []
        for phone in phones:
            self.addSMS(phone, body, sender)

    def callServer(self, data):
        request = urllib2.Request(
            self.service_url,
            json.dumps(data),
            headers=self.headers
        )
        Result = urllib2.urlopen(request)
        return json.loads(Result.read())

    def send(self):
        if len(self.messages) == 0:
            raise  Exception(u"No messages to send. Add one first")
        data = {
            u"apikey": self.api,
            u"send": self.messages
        }
        Result = self.callServer(data)
        self.messages = []
        return Result

    def checkStatus(self, server_ids):
        if server_ids == None:
            raise Exception(u"Ids list is empty")
        check_ids = []
        for server_id in server_ids:
            if isinstance(server_id, int):
                check_ids.append({u"server_id": server_id})

        data = {
            u"apikey": self.api,
            u"check": check_ids
        }
        return self.callServer(data)

    def checkPacketStatus(self, server_packet_id):
        if not server_packet_id.isdigit():
            raise  Exception(u"server_packet_id must be integer!")
        data = {
            u"apikey": self.api,
            u"check": True,
            u"server_packet_id": server_packet_id
        }
        return self.callServer(data)

    def checkBalance(self):
        data = {
            u"apikey": self.api,
            u"balance": True
        }
        return self.callServer(data)

    def userinfo(self):
        data = {
            u"apikey": self.api,
            u"info": True
        }
        return self.callServer(data)

    def getInbox(self):
        data = {
            u"apikey": self.api,
            u"inbound": True
        }
        return self.callServer(data)
