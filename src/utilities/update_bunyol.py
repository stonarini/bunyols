from src import database, book_scraper


def update_bunyol(ISBN, content):
    new_book_data = book_scraper.update_book_data(content)
    database.update_one(
        {"ISBN_13": ISBN},
        {
            "$push": {"price": new_book_data["price"][0]},
            "$set": {
                "reviews": new_book_data["reviews"],
            },
        },
    )
