from src import book_scraper, database
from .get_categories import get_categories


def create_bunyol(ISBN, content, categories):
    book_data = book_scraper.create_book_data(content, ISBN)
    if book_data:
        categories = get_categories(*categories)
        book_data.update(**categories)
        database.create_one(book_data)
