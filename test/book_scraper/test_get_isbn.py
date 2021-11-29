import pytest
from src.get_book_isbn import get_book_isbn
from src.book_scraper.get_book_source.get_book_source import get_book_source

website = get_book_source()

@pytest.mark.test_get_isbn
def test_get_isbn():
    assert isinstance(get_book_isbn(website), str), 'ISBN has to be a string type object'
    