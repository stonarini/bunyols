import json
from src.book_scraper.get_book_source.request_page import request_page


def request_openlibrary_page(page):

    URL = f"https://openlibrary.org/{page}.json"
    webpage = request_page(URL)
    content = webpage.text
    data = json.loads(content)
    return data
