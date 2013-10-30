#!/usr/bin/env python
# -*- coding: utf-8 *-*
import unittest
from pySMSPilot import sender

# emulator api key, no real sending
API = u'XXXXXXXXXXXXYYYYYYYYYYYYZZZZZZZZXXXXXXXXXXXXYYYYYYYYYYYYZZZZZZZZ'


class SmspilotTests(unittest.TestCase):

    def testNoApi(self):
        self.assertRaises(Exception, lambda _: sender.Sender(False))

    def testSingleSend(self):
        client = sender.Sender(API)
        client.addSMS(1,'75555555', u'Some text body')
        result = client.send()
        self.assertEqual(result[u'send'][0][u'text'], u'Some text body')
        self.assertEqual(result[u'send'][0][u'to'], u'75555555')

    def testInvalidMessageId(self):
        client = sender.Sender(API)
        try:
            client.addSMS(1, '75555555', u'Some test text')
        except Exception as inst:
            self.assertEqual(inst.message, u'SMS with this id already queried')
        try:
            client.addSMS('invalid_str_id', '75555555', u'Some test text')
        except Exception as inst:
            self.assertEqual(inst.message, u'sms_id must be integer')

    def testInvalidSendTime(self):
        client = sender.Sender(API)
        try:
            client.addSMS(1, '75555555', u'Happy birthday!', None, '20.12.2013')
        except Exception as inst:
            self.assertEqual(inst.message, u'Invalid datetime! Must be GMT timestamp or YYYY-MM-DD HH:MM:SS')

    def testMultiSend(self):
        client = sender.Sender(API)
        client.addSMS(1, '75555555', u'Some test text')
        client.addSMS(2, '74444444', u'Some test text')
        result = client.send()
        self.assertEqual(result[u'send'][0][u'to'], '75555555')
        self.assertEqual(result[u'send'][1][u'to'], '74444444')
        self.assertEqual(result[u'send'][0][u'text'], u'Some test text')
        self.assertEqual(result[u'send'][1][u'text'], u'Some test text')


def main():
    unittest.main()

if __name__ == '__main__':
    main()
