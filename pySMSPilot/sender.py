# -*- coding: utf-8 *-*
# Filename: Sender.py
'''
SMSPilot.ru API 2.x Usage Implementation
by Stanislav Sokolov aka Ratso
v. 1.2
'''

import json
import urllib2
import re


class Sender:
    service_url = u"http://smspilot.ru/api2.php"
    defaultSender = u"Friend"
    headers = {
        'Content-type': 'application/json',
        'Accept': 'text/plain',
        'User-Agent': 'PySMSPilot/1.2 (+https://github.com/ratso/pySMSPilot)'
    }
    messages = []

    def __new__(self):
        self.messages = []

    def __init__(self, api_key):
        if not api_key:
            raise Exception(u"API Key is not defined")
        self.api = api_key
        self.messages = []

    def resetQueue(self):
        self.messages = []
        return self;

    def _checkPhone(self, phone):
        phonePattern = re.compile(r'(^7[0-9]+)$', re.VERBOSE)
        return phone is not None and phonePattern.search(phone)

    def _checkSender(self, sender):
        regxPattern = re.compile(r'^[a-zA-Z.\-\d]{3,11}$', re.VERBOSE)
        return regxPattern.search(sender)

    def addSMS(self, sms_id, phone, body, sender=None, send_datetime=None):
        if not isinstance(sms_id, int):
            raise Exception(u"sms_id must be integer")
        if any(index['id'] == sms_id for index in self.messages):
            raise Exception(u"SMS with this id already queried")
        if not self._checkPhone(phone):
            raise Exception(u"Not valid phone number")
        if len(body) == 0:
            raise Exception(u"Too short message")
        if sender is None:
            sender = self.defaultSender
        if not self._checkSender(sender):
            raise Exception(u"Invalid sender name or phone")
        if not (send_datetime is None):
            send_datetime = self._checkDate(send_datetime)
        message = {
            u"id": sms_id,
            u"from": sender,
            u"to": phone,
            u"text": body,
            u"send_datetime": send_datetime,
        }
        self.messages.append(message)
        return self

    def batchSend(self, queue, body, sender=None):
        if queue is None:
            raise Exception(u"No phones in list")
        # Чистим очередь по умолчанию
        self.resetQueue()
        for sms_id, phone in queue:
            self.addSMS(sms_id, phone, body, sender)

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
        if server_ids is None:
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

    def _checkDate(self, datetime = None):
        #в формате YYYY-MM-DD HH:MM:SS
        if re.match(r'\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}', datetime):
            return datetime
        return None