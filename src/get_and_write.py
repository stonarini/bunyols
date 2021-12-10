from os import write
from src.database import find_all
from src.markdownify import markdownify
from src.write_to_file import write_to_file


def get_and_write(path):
    books = find_all()
    for book in books:
        del book["_id"]
        ISBN = book["ISBN_13"]
        price, reviews = book.pop("price"), book.pop("reviews")
        markdown = markdownify(book)
        write_to_file(path, f"{ISBN}.md", markdown)
