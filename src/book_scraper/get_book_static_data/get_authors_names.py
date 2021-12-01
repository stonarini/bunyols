from src.book_scraper.get_book_static_data.get_authors_address import (
    get_authors_address,
)
from src.book_scraper.get_book_static_data.request_openlibary_page import (
    request_openlibrary_page,
)
import requests, json


def get_authors_names(authors_list):

    authors_names = []
    incrementator = 0
    while incrementator != len(authors_list):
        authors_info = requests.get(
            "https://openlibrary.org" + authors_list[incrementator] + ".json"
        ).content
        authors_info = json.loads(authors_info)
        authors_names.append(authors_info["name"])
        incrementator += 1

    return authors_names


content = request_openlibrary_page("/works/OL8305641W")
list = get_authors_address(content)
get_authors_names(list)
