import pytest
from bs4 import BeautifulSoup
from src.book_scraper.get_book_data.get_book_dynamic_data.get_book_reviews import (
    get_book_reviews,
)


@pytest.mark.test_reviews_are_none
def test_reviews_are_none():
    soup = "reviews are none"
    assert get_book_reviews(soup) == {"total_reviews": "Na"}


@pytest.mark.test_reviews_are_correct
def test_reviews_are_correct():
    soup = BeautifulSoup(
        '<span id="acrCustomerReviewText">114 reviews</span> \
        <a class="a-link-normal 5star" title="5 stars represent 77% of rating"></a> \
        <a class="a-link-normal 4star" title="4 stars represent 15% of rating"></a> \
        <a class="a-link-normal 3star" title="3 stars represent 2% of rating"></a> \
        <a class="a-link-normal 2star" title="2 stars represent 1% of rating"></a> \
        <a class="a-link-normal 1star" title="1 stars represent 6% of rating"></a> \
        ',
        "lxml",
    )
    assert get_book_reviews(soup) == {
        "total_reviews": 114,
        "5": 88,
        "4": 17,
        "3": 2,
        "2": 1,
        "1": 6,
    }
