import pytest
from src.book_scraper.get_book_static_data.request_openlibary_page import (
    request_openlibrary_page,
)
from src.book_scraper.get_book_static_data.get_book_static_data import (
    get_book_static_data,
)
from src.book_scraper.get_book_source.exceptions import StatusCodeException


@pytest.mark.test_static_data_is_dict
def test_static_data_dicc():
    assert isinstance(request_openlibrary_page("books/OL7353617M"), dict)


data = "/isbn/97805903427"


@pytest.mark.test_get_book_static_data
def test_get_book_static_data():
    try:
        get_book_static_data(data)
    except StatusCodeException:
        assert True
    else:
        assert False



