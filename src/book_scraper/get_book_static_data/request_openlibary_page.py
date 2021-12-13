import json
from src.get_page_source import request_page


def request_openlibrary_page(page):

    URL = f"https://openlibrary.org/{page}.json"
    webpage = request_page(URL)
    data = json.loads(webpage.content)
    return data
