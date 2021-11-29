from bs4 import BeautifulSoup


def get_book_isbn(website):

    start = str(website).find("ISBN")
    start = str(website).find("9", start)
    ISBN = str(website)[start : start + 14]

    return ISBN.replace("-", "")
