from requests import ConnectionError, ConnectTimeout
from src.get_page_source.request_page import request_page
from .exceptions import StatusCodeException


def get_page_content(URL):
    try:
        webpage = request_page(URL)

    except StatusCodeException as status_code:
        print(f"Error {status_code}\nIs {URL} correct?\n")

    except ConnectTimeout:
        print(
            f"Connection Timeout while trying to connect to {URL}\nPlease, try again later."
        )

    except ConnectionError:
        print(
            f"Connection error while trying to connect to the {URL}\nAre you connected to the internet?"
        )

    else:
        return webpage
