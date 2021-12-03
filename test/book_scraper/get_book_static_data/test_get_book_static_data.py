import pytest
from src.get_page_source.exceptions import StatusCodeException
from src.book_scraper.get_book_static_data import get_book_static_data

data = "97805903427"


@pytest.mark.test_get_book_static_data
def test_get_book_static_data():
    try:
        get_book_static_data(data)
    except StatusCodeException:
        assert True
    else:
        assert False
