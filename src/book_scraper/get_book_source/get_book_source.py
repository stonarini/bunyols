from bs4 import BeautifulSoup
from src.book_scraper.get_book_source.get_page_content import get_page_content


def get_book_source(URL):
    webpage = get_page_content(URL)

    if webpage:
        soup = BeautifulSoup(webpage.content, "lxml")
        return soup
