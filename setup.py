# -*- coding: utf-8 -*-
# !/usr/bin/env python

from distutils.core import setup

setup(
    name='PySMSPilot',
    version='1.3',
    description='API wrapper for SMSPilot sms gateway <http://www.smspilot.ru>',
    author='Stanislav Sokolov aka Ratso',
    author_email='sokolst@gmail.com',
    license='LICENSE.txt',
    url='https://github.com/ratso/pySMSPilot',
    long_description=open('README.md').read(),
    packages=['pySMSPilot', 'pySMSPilot.test'],
)