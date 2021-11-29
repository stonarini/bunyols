from bs4 import BeautifulSoup
from src.book_scraper.get_book_source.get_page_content import get_page_content


def get_book_source(URL):
    
    assert isinstance(URL, str), 'URL should be str type object'
    
    webpage = get_page_content(URL)

    if webpage:
        return webpage.content
