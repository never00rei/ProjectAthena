#coding: UTF-8

"""
Athena settings:
    - Slackbot API tokens go here, along with custom plugins.
"""

from os import getenv

API_TOKEN = getenv('API_TOKEN')
DEBUG = True

init_resps = ["Give me two seconds.", "Ok, I'll see what we've got.", "On it.."]
std_resps = ["So here's what I found:", "This is what we've got on file:"]
err_resps = ["Sorry cap'n, but she just ain't choochin'...."]
missing_resps = ["I can't find what you asked me for: {0}", "Sorry, I tried my best but I can't find anything for {0}.."]


# Custom plugin override list.
PLUGINS = [
    'modules'
]