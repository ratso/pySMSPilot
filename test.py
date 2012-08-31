#!/usr/bin/env python
# -*- coding: utf-8 *-*
import smspilot

api = u"Your API Key here"
try:
    Pilot = smspilot.Sender(api)
    Pilot.addSMS(u"75555555555", u"Что-то на русском для проверки!", u"A friend")
    Pilot.addSMS(u"75555555555", u"Tesing Python SMS module!")
    Result = Pilot.send()
    print Result
except Exception, e:
    print u"Error: ", e
