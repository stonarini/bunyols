import pytest
from src.get_page_source import get_page_source


@pytest.mark.test_link_does_not_exist
def test_link_does_not_exist():
    link = "https://amazon.com/this-page-is-to-test/my-web-scraper/"
    assert get_page_source(link) is None
