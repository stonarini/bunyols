import pytest
from src.book_scraper.get_book_dynamic_data import get_book_dynamic_data


@pytest.mark.test_dynamic_data_input_is_valid
def test_dynamic_data_input_is_valid():
    soup = '<span class="a-color-price">\n$36.48\n</span> \
        <span id="acrCustomerReviewText">114 reviews</span> \
        <a class="a-link-normal 5star" title="5 stars represent 77% of rating"></a> \
        <a class="a-link-normal 4star" title="4 stars represent 15% of rating"></a> \
        <a class="a-link-normal 3star" title="3 stars represent 2% of rating"></a> \
        <a class="a-link-normal 2star" title="2 stars represent 1% of rating"></a> \
        <a class="a-link-normal 1star" title="1 stars represent 6% of rating"></a> \
        '
    book_data = get_book_dynamic_data(soup)
    assert book_data["price"][0]["value"] == "$36.48"
    assert book_data["reviews"] == {
        "total_reviews": 114,
        "5": 88,
        "4": 17,
        "3": 2,
        "2": 1,
        "1": 6,
    }


@pytest.mark.test_dynamic_data_input_is_not_valid
def test_dynamic_data_input_is_not_valid():
    soup = "price and reviews are none"
    book_data = get_book_dynamic_data(soup)
    assert book_data["price"][0]["value"] == "Na"
    assert book_data["reviews"] == {"total_reviews": "Na"}
