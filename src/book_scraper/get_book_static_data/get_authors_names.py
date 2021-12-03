from .get_authors_address import get_authors_address
from .request_openlibary_page import request_openlibrary_page


def get_authors_names(work_address):
    work = request_openlibrary_page(work_address)
    author_pages = get_authors_address(work["authors"])

    author_names = []
    for author in author_pages:
        author_info = request_openlibrary_page(author)
        author_names.append(author_info["name"])

    return author_names
