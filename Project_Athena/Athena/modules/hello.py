#coding: UTF-8

import re
import datetime
import random

from slackbot.bot import listen_to
from slackbot.bot import respond_to

@listen_to('^Hello|^Greetings|^Aloha|^Bonjour|^Hey|^Hi there&|^Hi$', re.IGNORECASE)
def greetings_channel(message):
    """
    Return a greeting.
    :param message:
    :return:
    """
    replies = ["Hi There!", "Aloha!!", "Salut.", "Yo!", "Greetings to you to!"]
    reply = random.choice(replies)
    message.reply("{0} :smiley:".format(reply), in_thread=True)


@respond_to('^Hello|^Greetings|^Aloha|^Bonjour|^Hey|^Hi there&|^Hi$', re.IGNORECASE)
def greetings_at(message):
    """
    Return a greeting.
    :param message:
    :return:
    """
    replies = ["Hi There! :)", "Aloha!!", "Salut.", "Yo!", "Greetings to you to!"]
    reply = random.choice(replies)
    message.reply("{0}".format(reply))


@listen_to('^Good (evening|afternoon|morning)$', re.IGNORECASE)
def greetings_time_based_channel(message, period=None):
    now = datetime.datetime.now()
    if now.hour > 0 and now.hour < 12:
        current_period = 'morning'
    elif now.hour > 12 and now.hour < 17:
        current_period = 'afternoon'
    else:
        current_period = 'evening'

    if period.lower() == current_period.lower():
        message.reply(f'Good {current_period} :smiley:',
                      in_thread=True)
    else:
        message.reply(f"It's currently {now.time()}, so it should be {current_period} "
                      f"- but all the same, good {period} :smiley:",
                      in_thread=True)


@respond_to('^Good (evening|afternoon|morning)$', re.IGNORECASE)
def greetings_time_based_at(message, period=None):
    now = datetime.datetime.now()
    if now.hour > 0 and now.hour < 12:
        current_period = 'morning'
    elif now.hour > 12 and now.hour < 18:
        current_period = 'afternoon'
    else:
        current_period = 'evening'

    if period.lower() == current_period.lower():
        message.reply(f'Good {current_period} :smiley:')
    else:
        message.reply(f"It's currently {now.time()}, so it should be {current_period} "
                      f"- but all the same, good {period} :smiley:")


