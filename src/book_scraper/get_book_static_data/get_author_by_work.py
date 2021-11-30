import requests, json
from src.book_scraper.get_book_static_data.request_openlibary_page import (
    request_openlibrary_page,
)


def get_author_by_work(works):

    author_page_address = []

    for work in works["authors"]:
        author_page_address.append(work["author"])

    print(author_page_address)

    author_page = []
    for index in author_page_address:
        author_page.append(list(index.values()))

    print(author_page)

    names_list = []

    for author in author_page:
        work_info = requests.get(
            "https://openlibrary.org" + str(author) + ".json"
        ).content
        work_info = json.loads(work_info)
        author_name = work_info["name"]
        names_list.append(author_name)

    # for key in author_page_address:
    #   author_page_values.append(key.values())

    author_page_content = []


#    for address in author_page_address:
#       works_info = requests.get("https://openlibrary.org" + address + ".json").content
#       author_page_content.append(works_info)

# works_info = requests.get("https://openlibrary.org" + data + ".json").content
# works_info = json.loads(works_info)

x = request_openlibrary_page("/works/OL20757294W")
get_author_by_work(x)
