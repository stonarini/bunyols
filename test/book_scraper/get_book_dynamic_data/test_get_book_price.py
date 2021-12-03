import pytest
from bs4 import BeautifulSoup
from src.book_scraper.get_book_data.get_book_dynamic_data.get_book_price import (
    get_book_price,
)


@pytest.mark.test_price_exists
def test_price_exists():
    soup = BeautifulSoup('<span class="a-color-price">\n$36.48\n</span>', "lxml")
    assert get_book_price(soup)[0]["value"] == "$36.48"


@pytest.mark.test_price_is_none
def test_price_is_none():
    soup = "price is none"
    assert get_book_price(soup)[0]["value"] == "Na"
