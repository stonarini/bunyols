from .book_scraper import book_scraper
from .get_page_source import get_page_source
from .get_book_isbn import get_book_isbn
from .get_categories import get_categories
import src.database as database


def bunyols(item):
    URL, categories = item
    content = get_page_source(URL)
    ISBN = get_book_isbn(content)

    if database.find_one({"ISBN_13": ISBN}):
        new_book_data = book_scraper.update_book_data(content)
        database.update_one(
            {"ISBN_13": ISBN},
            {
                "$push": {"price": new_book_data["price"][0]},
                "$set": {
                    "reviews": new_book_data["reviews"],
                },
            },
        )
    else:
        book_data = book_scraper.create_book_data(content, ISBN)
        if book_data:
            categories = get_categories(*categories)
            book_data.update(**categories)
            database.create_one(book_data)
