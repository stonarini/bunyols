from .get_authors_names import get_authors_names
from .request_openlibary_page import request_openlibrary_page
from .get_publisher import get_publisher


def get_book_static_data(ISBN):
    data = request_openlibrary_page("isbn/" + ISBN)
    book = {
        "title": data["title"],
        "author": get_authors_names(data["works"][0]["key"]),
        "publisher": get_publisher(data),
        "ISBN_13": ISBN,
        "publish_date": data["publish_date"],
    }
    return book
