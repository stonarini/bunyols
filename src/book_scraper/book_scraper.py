from .get_book_static_data import get_book_static_data
from .get_book_source import get_book_source
from .get_book_isbn import get_book_isbn
from .get_book_dynamic_data import get_book_dynamic_data
from .get_categories import get_categories


def book_scraper(items):
    for item in items:
        URL, family, topics = item
        content = get_book_source(URL)
        ISBN = get_book_isbn(content)

        static_data = get_book_static_data("/isbn/" + ISBN)
        dynamic_data = get_book_dynamic_data(content)
        categories = get_categories(family, topics)

        book_data = {**static_data, **dynamic_data, **categories}
        print(book_data)
