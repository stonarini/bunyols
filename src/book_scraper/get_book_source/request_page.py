import requests
from .exceptions import StatusCodeException


def request_page(URL):
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
        "Accept-Language": "en-US, en;q=0.5",
    }

    webpage = requests.get(URL, headers=HEADERS)
    if 599 >= webpage.status_code >= 400:
        raise StatusCodeException(webpage.status_code)

    return webpage
