#coding: UTF-8

from slackbot.bot import respond_to
from slackbot.bot import default_reply

import re
import random
import os
import arrow
import uuid

import matplotlib
matplotlib.use('AGG')
import matplotlib.pyplot as plt


def mock_stats(start_date=None, end_date=None):
    if start_date is not None and end_date is not None:
        if start_date.lower() in ['now', 'today']:
            start_date = arrow.now()
        else:
            start_date = arrow.get(start_date, 'DD/MM/YYYY')

        if end_date.lower() in ['now', 'today']:
            end_date = arrow.now()
        else:
            end_date = arrow.get(end_date, 'DD/MM/YYYY')
    else:
        end_date = arrow.now()
        start_date = end_date.shift(days=-(random.randint(1, 200)))

    dates = [date.naive for date in arrow.Arrow.range(frame='day', start=start_date, end=end_date)]

    data = []

    for date in dates:
        point = random.randint(1, 12)
        data.append(point)

    return dates, data


def gen_chart(x, y, file, title=None, x_label=None, y_label=None):
    fig, ax = plt.subplots(nrows=1, ncols=1,figsize=(20, 10))
    ax.plot(x, y, 'b-')
    if title is not None:
        fig.suptitle(title)
    if x_label is not None:
        ax.set_xlabel(x_label)
    if y_label is not None:
        ax.set_ylabel(y_label)
    ax.xaxis_date()
    try:
        fig.savefig(file)
        plt.close(fig)
        return True
    except:
        raise
        plt.close(fig)
        return False


@default_reply
def my_default_handler(message):
    default_replies = ["I don't understand", "Eh???", "I don't know how to take that.."]
    reply = random.choice(default_replies)
    message.reply('{0}'.format(reply))


@respond_to('show me (.*) from (.*) to (.*)', re.IGNORECASE)
@respond_to('send me the (.*) from (.*) to (.*)', re.IGNORECASE)
@respond_to('send me (.*) from (.*) to (.*)', re.IGNORECASE)
# @respond_to('show me (.*) between (.*) until (.*)', re.IGNORECASE)
def statistics(message, metric, start_date=None, end_date=None):
    """
    :param message:
    :param user:
    :param start_date:
    :param end_date:
    :return:
    """
    replies = ["Here's what you asked for. ", "Ok, I this is what I got back. ", "Here you go. "]
    reply_message = random.choice(replies)
    dates, data = mock_stats(start_date=start_date, end_date=end_date)
    start_date = arrow.get(start_date)
    end_date = arrow.get(end_date)

    message.reply('Sure, let me grab {} for you.'.format(metric))

    file_name = '{0}-{1}-{2}.png'.format(metric, start_date.format('DD.MM.YYYY'), end_date.format('DD.MM.YYYY'))
    print(metric, start_date, end_date, file_name)
    file = '/tmp/{}.png'.format(uuid.uuid4())

    if gen_chart(x=dates, y=data, file=file, title=file_name, x_label='Date Period', y_label=metric) is True:
        message.channel.upload_file(file_name, file, reply_message)
    else:
        message.reply("I tried to generate the graph but failed miserably..")

    if os.path.exists(file):
        os.remove(file)

