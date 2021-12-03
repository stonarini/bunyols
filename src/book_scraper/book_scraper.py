from .get_book_source import get_book_source
<<<<<<< HEAD
from .get_book_isbn import get_book_isbn
from .get_book_dynamic_data import get_book_dynamic_data
from .get_categories import get_categories
from src.database import create_one
=======
from .get_book_data import get_book_data
>>>>>>> book-scraper


def book_scraper(items):
    for item in items:
        URL, item = item
        content = get_book_source(URL)

<<<<<<< HEAD
        static_data = get_book_static_data("/isbn/" + ISBN)
        dynamic_data = get_book_dynamic_data(content)
        categories = get_categories(family, topics)

        book_data = {**static_data, **dynamic_data, **categories}

        create_one(book_data)
=======
        book_data = get_book_data(content, item)
        print(book_data)
>>>>>>> book-scraper
