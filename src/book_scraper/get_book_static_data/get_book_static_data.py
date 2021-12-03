from .get_authors_names import get_authors_names
from .request_openlibary_page import request_openlibrary_page


def get_book_static_data(ISBN):
    data = request_openlibrary_page("isbn/" + ISBN)
    book = {
        "title": data["title"],
        "author": get_authors_names(data["works"][0]["key"]),
        "publisher": data["publishers"][0],
        "ISBN_13": data["isbn_13"][0],
        "publish_date": data["publish_date"],
    }
    return book
