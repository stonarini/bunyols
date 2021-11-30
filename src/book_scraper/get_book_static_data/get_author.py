import requests, json
from src.book_scraper.get_book_static_data.request_openlibary_page import (
    request_openlibrary_page,
)


def get_author(authors_data):

    for author in authors_data["authors"]:
        data = author["key"]

    author_info = requests.get("https://openlibrary.org" + data + ".json").content
    author_info = json.loads(author_info)
    author_name = author_info["name"]
    return author_name
