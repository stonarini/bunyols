import requests, json


def get_author(authors_data):

    for author in authors_data["authors"]:
        data = author["key"]

    author_info = requests.get("https://openlibrary.org" + data + ".json").content
    author_info = json.loads(author_info)
    author_name = author_info["name"]
    return author_name
