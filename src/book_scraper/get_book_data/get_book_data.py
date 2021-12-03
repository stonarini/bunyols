from src.book_scraper.get_book_source import StatusCodeException
from .get_book_dynamic_data import get_book_dynamic_data
from .get_book_static_data import get_book_static_data
from .get_book_isbn import get_book_isbn
from .get_categories import get_categories


def get_book_data(content, item):
    ISBN = get_book_isbn(content)
    # todo: if isbn is in the database, skip static data
    try:
        static_data = get_book_static_data("isbn/" + ISBN)
    except StatusCodeException as status_code:
        print("Error", status_code, "- Book not added")
    else:
        dynamic_data = get_book_dynamic_data(content)
        categories = get_categories(*item)
        return {**static_data, **dynamic_data, **categories}
