#coding: UTF-8

"""
Athena settings:
    - Slackbot API tokens go here, along with custom plugins.
"""

from os import getenv

API_TOKEN = getenv('API_TOKEN')
DEBUG = True

# Custom plugin override list.
PLUGINS = [
    'modules.commands',
    'modules.greetings'
]