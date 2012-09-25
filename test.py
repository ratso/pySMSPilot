#!/usr/bin/env python
# -*- coding: utf-8 *-*
import unittest
from smspilot import Sender

# emulator api key, no real sending
API = u'XXXXXXXXXXXXYYYYYYYYYYYYZZZZZZZZXXXXXXXXXXXXYYYYYYYYYYYYZZZZZZZZ'


class SmspilotTests(unittest.TestCase):

    def testNoApi(self):
        self.assertRaises(Exception, lambda _: Sender(False))

    def testSingleSend(self):
        sms = Sender(API)
        sms.addSMS('75555555', u'Some text body')
        result = sms.send()
        self.assertEqual(result[u'send'][0][u'text'], u'Some text body')
        self.assertEqual(result[u'send'][0][u'to'], u'75555555')

    def testMultiSend(self):
        sms = Sender(API)
        sms.addSMS('75555555', u'Some test text')
        sms.addSMS('74444444', u'Some test text')
        result = sms.send()
        self.assertEqual(result[u'send'][0][u'to'], '75555555')
        self.assertEqual(result[u'send'][1][u'to'], '74444444')
        self.assertEqual(result[u'send'][0][u'text'], u'Some test text')
        self.assertEqual(result[u'send'][1][u'text'], u'Some test text')


def main():
    unittest.main()

if __name__ == '__main__':
    main()
