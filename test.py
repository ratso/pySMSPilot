#!/usr/bin/env python
# -*- coding: utf-8 *-*
import smspilot

api = u"Your API Key here"
try:
    Pilot = smspilot.Sender(api)
    Pilot.addSMS(u"75555555555", u"Что-то на русском для проверки!", u"A friend")
    Pilot.addSMS(u"75555555555", u"Tesing Python SMS module!")
    print Pilot.send()
    Pilot.batchsend([u'75555555555', u'75555555554'], u"Test batch")
    print Pilot.send()
    print Pilot.checkBalance()
    print Pilot.checkStatus([9876961, 9876452])
    print Pilot.userinfo()
    print Pilot.getInbox()
except Exception, e:
    print u"Error: ", e
