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
        try:
            time_elapsed = requests.get(url).elapsed.total_seconds()
            return {'status': '200', 'response_time': time_elapsed}
        except:
            return {'status': '503'}