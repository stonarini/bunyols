from .book_scraper import book_scraper
from .get_page_source import get_page_source
from .get_book_isbn import get_book_isbn
from .get_categories import get_categories


def bunyols(item):
    URL, categories = item
    content = get_page_source(URL)
    ISBN = get_book_isbn(content)
    # if isbn in database
    # new_book_data = book_scraper.update_book_data(content)
    # database.update(new_book_data)
    # else
    book_data = book_scraper.create_book_data(content, ISBN)
    categories = get_categories(categories)
    book_data = {**book_data, **categories}
