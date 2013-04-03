# -*- coding: utf-8 -*-
#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='PySMSPilot',
    version='1.1',
    description='API wrapper for SMSPilot sms gateway <http://www.smspilot.ru>',
    author='Stanislav Sokolov aka Ratso',
    author_email='sokolst@gmail.com',
    url='https://github.com/ratso/pySMSPilot',
    package_data = {'':['*.py', 'README']},
    packages = find_packages(),
)