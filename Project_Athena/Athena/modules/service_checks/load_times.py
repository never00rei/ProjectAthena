import requests

def check_load_time(url):
    """
    Requests the url of a service and returns the total time taken
    to render the url.
    :param url:
    :return:
    """
    if url == None:
        return "Empty URL"
    else:
        time_elapsed = requests.get(url).elapsed.total_seconds()
        return time_elapsed