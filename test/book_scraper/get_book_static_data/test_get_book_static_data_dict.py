import pytest
from src.book_scraper.get_book_static_data.request_openlibary_page import (
    request_openlibrary_page,
)
from src.book_scraper.get_book_static_data.get_book_static_data import (
    get_book_static_data,
)
from src.book_scraper.get_book_source.exceptions import StatusCodeException


@pytest.mark.test_static_data_is_dict
def test_static_data_dict():
    assert isinstance(request_openlibrary_page("books/OL7353617M"), dict)


@pytest.mark.test_get_book_static_data_keys
def test_static_data_dict_keys():
    book = get_book_static_data("/isbn/9780590353427")

    static_data_structure = {
        "title": "test",
        "author": "test",
        "publisher": "test",
        "ISBN_13": "test",
        "publish_date": "test",
    }

    assert book.keys() == static_data_structure.keys()
