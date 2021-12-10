from src import markdownify, get_page_source
import src.database as database
import src.utilities as utilities


def bunyols(item_list, path):
    for item in item_list:
        URL, categories = item
        content = get_page_source(URL)
        ISBN = utilities.get_book_isbn(content)

        if database.find_one({"ISBN_13": ISBN}):
            utilities.update_bunyol(ISBN, content)
        else:
            utilities.create_bunyol(ISBN, content, categories)

    books = database.find_all()
    for book in books:
        del book["_id"]
        ISBN = book["ISBN_13"]
        price, reviews = book.pop("price"), book.pop("reviews")
        markdown = markdownify(book)
        utilities.write_to_file(path, f"{ISBN}.md", markdown)


if __name__ == "__main__":
    import sys

    item_list = [
        ("https://www.amazon.com/-/Aldous-Huxley/dp/0060850523/", (None, ["Fantasy"]))
    ]
    path = sys.argv[1]
    bunyols(item_list, path)
