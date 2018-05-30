import requests

def check_load_time(url):
    """
    Requests the url of a service and returns the total time taken
    to render the url.
    :param url:
    :return: dictionary of items...
    """

    if url is None:
        return {'status': '404'}
    else:
        result = requests.get(url)
        return {'status': result.status_code, 'response_time': result.elapsed.time_elapsed}