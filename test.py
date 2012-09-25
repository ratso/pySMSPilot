#!/usr/bin/env python
# -*- coding: utf-8 *-*
import unittest
import smspilot


class SmspilotTests(unittest.TestCase):

    def testNoApi(self):
        self.assertRaises(Exception, lambda _: smspilot.Sender(False))


def main():
    unittest.main()

if __name__ == '__main__':
    main()
