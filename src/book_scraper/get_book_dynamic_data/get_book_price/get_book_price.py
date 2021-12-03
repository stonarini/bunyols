from datetime import datetime
from .scrap_price import scrap_price


def get_book_price(soup):
    price = scrap_price(soup)
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    price_element = [{"date": date, "value": price}]
    return price_element
