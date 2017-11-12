#coding: UTF-8


import re
import random
from slackbot.bot import respond_to
from slackbot.bot import default_reply


@default_reply
def my_default_handler(message):
    default_replies = ["I don't understand", "Eh???", "I don't know how to take that.."]
    reply = random.choice(default_replies)
    message.reply('{0}'.format(reply))


@respond_to('stats$|statistics$|stats|statistics', re.IGNORECASE)
@respond_to('stats (.*) (.*)', re.IGNORECASE)
@respond_to('statistics from (.*) to (.*)', re.IGNORECASE)
@respond_to('send (.*) statistics from (.*) between (.*) and (.*)')
def statistics(message, user=None, start_date=None, end_date=None):
    """
    :param message:
    :param user:
    :param start_date:
    :param end_date:
    :return:
    """
    replies = ["Yeah sure, here's what you need: ", "Ok, I think it's this: ", "No problem boss: "]
    reply = random.choice(replies)

    if start_date and end_date:
        message.reply('{0} {1}, {2}'.format(reply, start_date, end_date))
    else:
        message.reply('{0}'.format(reply))