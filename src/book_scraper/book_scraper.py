from .get_book_static_data import get_book_static_data
from src.get_page_source import StatusCodeException
from .get_book_dynamic_data import get_book_dynamic_data


def create_book_data(content, ISBN):
    try:
        static_data = get_book_static_data(ISBN)
    except StatusCodeException as status_code:
        print("Error", status_code, "- Book not added")
    else:
        dynamic_data = get_book_dynamic_data(content)
        return {**static_data, **dynamic_data}


def update_book_data(content):
    return get_book_dynamic_data(content)
