import pytest
from src.book_scraper.get_book_source.get_book_source import get_book_source


@pytest.mark.test_link_does_not_exist
def test_link_does_not_exist():
    link = "https://amazon.com/this-page-is-to-test/my-web-scraper/"
    assert get_book_source(link) is None
