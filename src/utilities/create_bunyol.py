from src import book_scraper, database, utilities


def create_bunyol(ISBN, content, categories):
    book_data = book_scraper.create_book_data(content, ISBN)
    if book_data:
        categories = utilities.get_categories(*categories)
        book_data.update(**categories)
        database.create_one(book_data)
