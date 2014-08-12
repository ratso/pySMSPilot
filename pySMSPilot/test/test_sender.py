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
        client.addSMS(1, '79201234567', u'Some text body')
        result = client.send()
        self.assertEqual(result[u'send'][0][u'text'], u'Some text body')
        self.assertEqual(result[u'send'][0][u'to'], u'79201234567')

    def testInvalidMessageId(self):
        client = sender.Sender(API)
        try:
            client.addSMS(1, '79201234567', u'Some test text')
        except Exception as inst:
            self.assertEqual(inst.message, u'SMS with this id already queried')
        try:
            client.addSMS('invalid_str_id', '79201234567', u'Some test text')
        except Exception as inst:
            self.assertEqual(inst.message, u'sms_id must be integer')

    def testInvalidSendTime(self):
        client = sender.Sender(API)
        try:
            client.addSMS(1, '79201234567', u'Happy birthday!', None, '20.12.2013')
        except Exception as inst:
            self.assertEqual(inst.message, u'Invalid datetime! Must be GMT timestamp or YYYY-MM-DD HH:MM:SS')

    def testValidDateTimeSendTime(self):
        client = sender.Sender(API)
        import datetime
        send_date = datetime.datetime.now()+ datetime.timedelta(hours=1)
        client.addSMS(1, '79201234567', u'Happy birthday!', None, send_date)
        result = client.send()
        self.assertEqual(result[u'send'][0][u'text'], u'Happy birthday!')
        self.assertEqual(result[u'send'][0][u'to'], u'79201234567')
        self.assertEquals(send_date.strftime("%Y-%m-%d %H:%M:%S"), result[u'send'][0]['send_datetime'])

    def testTTL(self):
        client = sender.Sender(API)
        try:
            client.addSMS(1, '79201234567', u'Happy birthday!', ttl=10)
            client.addSMS(2, '79201234567', u'Happy birthday!', ttl=1440)
        except Exception, e:
            self.fail()

        self.assertRaises(Exception, client.addSMS, 3, '79201234567', u'Happy birthday!', ttl=1441)
        self.assertRaises(Exception, client.addSMS, 4, '79201234567', u'Happy birthday!', ttl=1)
        self.assertRaises(Exception, client.addSMS, 5, '79201234567', u'Happy birthday!', ttl="Test")

    def test_callback_request(self):
        try:
            client = sender.Sender(API, callback="http://ya.ru/", callback_method="post")
        except Exception, e:
            self.fail("Valid callback method but %s" % e.message)
        client.addSMS(1, '79201234567', u'Some test text')
        self.assertEqual(client.messages[0][u'callback'], "http://ya.ru/")
        self.assertEqual(client.messages[0][u'callback_method'], "post")
        try:
            client = sender.Sender(API, callback="http://ya.ru/", callback_method="get")
        except Exception, e:
            self.fail("Valid callback method but %s" % e.message)
        client.addSMS(1, '79201234567', u'Some test text')
        self.assertEqual(client.messages[0][u'callback'], "http://ya.ru/")
        self.assertEqual(client.messages[0][u'callback_method'], "get")

    def test_callback(self):
        # set method without url
        self.assertRaises(Exception, sender.Sender, API, callback_method="post")
        # set invalid url
        self.assertRaises(Exception, sender.Sender, API, callback="https://ya.ru/")
        # set invalid method
        self.assertRaises(Exception, sender.Sender, API, callback="http://ya.ru/", callback_method="put")

        try:
            client = sender.Sender(API, callback="http://ya.ru/")
        except Exception, e:
            self.fail("Valid callback but %s" % e.message)



    def testMultiSend(self):
        client = sender.Sender(API)
        client.addSMS(1, '79201234567', u'Some test text')
        client.addSMS(2, '79201234568', u'Some test text')
        result = client.send()
        self.assertEqual(result[u'send'][0][u'to'], '79201234567')
        self.assertEqual(result[u'send'][1][u'to'], '79201234568')
        self.assertEqual(result[u'send'][0][u'text'], u'Some test text')
        self.assertEqual(result[u'send'][1][u'text'], u'Some test text')


def main():
    unittest.main()

if __name__ == '__main__':
    main()
