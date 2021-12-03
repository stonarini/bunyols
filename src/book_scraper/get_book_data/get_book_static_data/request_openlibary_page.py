import json
from src.book_scraper.get_book_source import request_page


def request_openlibrary_page(page):

    URL = f"https://openlibrary.org/{page}.json"
    webpage = request_page(URL)
    data = json.loads(webpage.content)
    return data
