#coding: UTF-8

import sys
import logging
import logging.config
from slackbot import settings
from slackbot.bot import Bot

def main():
    if settings.API_TOKEN is not None:
        kw = {
            'format': '[%(asctime)s] %(message)s',
            'datefmt': '%m/%d/%Y %H:%M:%S',
            'level': logging.DEBUG if settings.DEBUG else logging.INFO,
            'stream': sys.stdout,
        }
        logging.basicConfig(**kw)
        logging.getLogger('requests.packages.urllib3.connectionpool').setLevel(logging.WARNING)
        bot = Bot()
        bot.run()
    else:
        print('Your Slack API_TOKEN is not set, please add it to your environment variables..')
        sys.exit()


if __name__ == "__main__":
    main()