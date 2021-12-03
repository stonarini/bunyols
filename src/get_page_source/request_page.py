import requests
from fake_headers import Headers
from .exceptions import StatusCodeException


def request_page(URL):
    HEADERS = Headers(headers=True)
    new_header = HEADERS.generate()

    webpage = requests.get(URL, headers=new_header)
    if 599 >= webpage.status_code >= 400:
        raise StatusCodeException(webpage.status_code)

    return webpage
