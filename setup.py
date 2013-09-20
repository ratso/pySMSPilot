# -*- coding: utf-8 -*-
#!/usr/bin/env python

from setuptools import setup

setup(
    name='PySMSPilot',
    version='1.2',
    description='API wrapper for SMSPilot sms gateway <http://www.smspilot.ru>',
    author='Stanislav Sokolov aka Ratso',
    author_email='sokolst@gmail.com',
    url='https://github.com/ratso/pySMSPilot',
    packages = ['pySMSPilot'],
    install_requires=[
        'setuptools',
    ],
)