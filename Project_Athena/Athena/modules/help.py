import re
from slackbot.bot import respond_to

"""Provide help to users in channels or in private messages"""


@respond_to('^what can you do\?$', re.IGNORECASE)
def help_general(message):
    print(message)
    print(message._get_bot_name())
    message.reply("Currently I can listen out for basic queries and respond to direct requests. "
                  'However if you tag me (`@{bot}` and then say `list commands`, '
                  "I'll write you a list of what I can do.. :smiley:")