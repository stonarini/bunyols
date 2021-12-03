from .get_book_source import get_book_source
from .get_book_data import get_book_data


def book_scraper(items):
    for item in items:
        URL, item = item
        content = get_book_source(URL)

        book_data = get_book_data(content, item)
        print(book_data)
