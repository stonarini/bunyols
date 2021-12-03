from .get_book_source import get_book_source
from .get_book_data import get_book_data
from src.database import create_one


def book_scraper(items):
    for item in items:
        URL, item = item
        content = get_book_source(URL)

        book_data = get_book_data(content, item)
        if book_data:
            create_one(book_data)
