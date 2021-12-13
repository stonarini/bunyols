from src import markdownify, get_page_source, generate_graphs
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
        utilities.write_to_file(path + "content/bunyols/", f"{ISBN}.md", markdown)
        generate_graphs(path + "static/images/" + ISBN, reviews, price)


if __name__ == "__main__":
    import sys
    import os
    from items import items
    
    if len(sys.argv) < 2:
        print("No path provided")
    elif len(sys.argv) > 2:
        print("Too many arguments")
    else:
        path = sys.argv[1]
        if os.path.isdir(path):
            bunyols(items, path)
        else:
            print("Error path does not exist or it's not a directory")
