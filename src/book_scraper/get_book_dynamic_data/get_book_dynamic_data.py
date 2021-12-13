from bs4 import BeautifulSoup
from .get_book_price import get_book_price
from .get_book_reviews import get_book_reviews


def get_book_dynamic_data(content):
    soup = BeautifulSoup(content, "lxml")
    price = get_book_price(soup)
    reviews = get_book_reviews(soup)
    return {"price": price, "reviews": reviews}
