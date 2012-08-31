# -*- coding: utf-8 *-*
# Filename: smspilot.py
'''
SMSPilot.ru API 2.x Usage Implementation
by Stanislav Sokolov aka Ratso
v. 1.0
'''

import json
import urllib2
import re
import random


class SenderException(Exception):
    pass


class Sender:
    service_url = u"http://smspilot.ru/api2.php"
    defaultSender = u"Friend"

    def __init__(self, api_key):
        if not api_key:
            raise SenderException("API Key is not defined")
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
            raise Exception("Not valid phone number")
        if len(body) == 0:
            raise Exception("Too short message")
        if sender == None:
            sender = self.defaultSender
        if not self.checkSender(sender):
            raise Exception("Invalid sender name or phone")
        message = {
            u"id": random.choice(range(1, 9999)),
            u"from": sender,
            u"to": phone,
            u"text": body
        }
        self.messages.append(message)
        return True

    def send(self):
        if len(self.messages) == 0:
            raise  Exception("No messages to send. Add one first")
        data = {
            u"apikey": self.api,
            u"send": self.messages
        }
        rheaders = {
            'Content-type': 'application/json',
            'Accept': 'text/plain'
        }
        request = urllib2.Request(
            self.service_url,
            json.dumps(data),
            headers=rheaders
        )
        Result = urllib2.urlopen(request)
        self.messages = []
        return json.loads(Result.read())
