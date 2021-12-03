import pytest
from src.get_book_isbn import get_book_isbn
from src.get_page_source import get_page_source

website = get_page_source(
    "https://www.amazon.com/Code-Complete-Practical-Handbook-Construction/dp/0735619670/"
)


@pytest.mark.test_isbn_is_string
def test_isbn_is_string():
    assert isinstance(get_book_isbn(website), str)


@pytest.mark.test_isbn_lenght
def test_isbn_lenght():
    assert len(get_book_isbn(website)) == 14 or 13
