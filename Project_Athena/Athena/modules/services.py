import re
import random
import json

from slackbot.bot import listen_to
from slackbot.bot import respond_to
from slackbot import settings

# This throws an error in the python console but it's required for the SlackBot Package..
from modules.db_adapter.db_model import Service, ServiceCheck
from modules.db_adapter import postgres
from modules.service_checks.load_times import check_load_time


def choose_replies(init_resps=None, std_resps=None, err_resps=None, missing_resps=None):
    """
    This function randomly selects from a list of responses and returns two values
    :param init_resps: List of initial responses
    :param std_resps: List of standard responses
    :return:
    """
    if init_resps is None:
        init_resp = random.choice(settings.init_resps)
    else:
        init_resp = random.choice(init_resps)

    if std_resps is None:
        std_resp = random.choice(settings.std_resps)
    else:
        std_resp = random.choice(std_resps)

    if err_resps is None:
        err_resp = random.choice(settings.err_resps)
    else:
        err_resp = random.choice(err_resps)

    if missing_resps is None:
        missing_resp = random.choice(settings.missing_resps)
    else:
        missing_resp = random.choice(missing_resps)


    return init_resp, std_resp, err_resp, missing_resp


def gen_keyword_regex():
    """
    Scans services and builds a list of keywords for use in searches.
    :return:
    """
    services = postgres.db_session.query(Service).all()
    keywords = []
    for service in services:
        if service.keywords is not None:
            for keyword in service.keywords:
                keywords.append(keyword)

    return keywords


@listen_to('list all services', re.IGNORECASE)
@listen_to('list services', re.IGNORECASE)
@listen_to('What services do we have', re.IGNORECASE)
def channel_service_message(message):
    """
    Scans channel for messages asking about what services currently have integration.
    :param message: Object for slack messaging service.
    :return:
    """
    attachments = []  # Create list element for Slack attachments
    initial_reply, std_reply, err_reply, missing_reply = choose_replies()  # Choose replies
    # Send initial reply
    message.reply("{0} :smiley:".format(initial_reply),
                  in_thread=True)

    services = postgres.db_session.query(Service).all() # Get list of services
    counted_services = len(services)
    # Generate attachments
    for service in services:
        attachments.append({'title': service.service_name, 'fields': \
        [{'title': 'Service ID', 'value': service.id, 'short': True}, \
        {'title': 'Service Description', 'value': service.service_description, 'short': True}]})
    # Send attachments
    message.reply_webapi(std_reply,
                         json.dumps(attachments),
                         in_thread=True)


@respond_to('list all services', re.IGNORECASE)
@respond_to('list services', re.IGNORECASE)
@respond_to('What services do we have', re.IGNORECASE)
def direct_service_message(message):
    """
    Listens for direct messages asking about what services currently have integration.
    :param message: Object for slack messaging service.
    :return:
    """
    attachments = []  # Create list element for Slack attachments
    initial_reply, std_reply, err_reply, missing_reply = choose_replies()  # Choose replies
    # Send initial reply
    message.reply("{0} :smiley:".format(initial_reply))

    services = postgres.db_session.query(Service).all()  # Get list of services
    counted_services = len(services)
    # Generate attachments
    for service in services:
        attachments.append({'title': service.service_name, 'fields': \
            [{'title': 'Service ID', 'value': service.id, 'short': True}, \
             {'title': 'Service Description', 'value': service.service_description, 'short': True}]})
    # Send attachments
    message.reply_webapi(std_reply,
                         json.dumps(attachments))


@listen_to('Is (.*) going slow', re.IGNORECASE)
@listen_to('Is (.*) running slow', re.IGNORECASE)
def service_check(message, service):
    init_replies = ["I'll check on that for you. :smiley:", "Let's have a look! :smiley:"]
    std_replies = ["So this came back, {0} took {1} seconds to load.", \
                   "Wow, {1} seconds to load - such awesome {0}.."]
    init_reply, std_reply, err_reply, missing_reply = choose_replies(init_resps=init_replies,
                                                      std_resps=std_replies)
    message.reply(init_reply)
    query = postgres.db_session.query(Service).filter(Service.keywords.any(service)).all()
    if query is None:
        message.reply(missing_reply.format(service))
    else:
        staged = postgres.db_session.query(ServiceCheck).filter(ServiceCheck.service_id == query[0].id).all()
        if staged is not None:
            response = check_load_time(staged[0].check_url)
            print(response)
            if response is not None:
                message.reply(std_reply.format(query[0].service_name, response['response_time']))
            elif response['status'] == '503':
                message.reply(err_reply)
            elif response['status'] == '404':
                message.reply(missing_reply)
            else:
                message.reply(err_reply)
        else:
            message.reply(err_reply)


