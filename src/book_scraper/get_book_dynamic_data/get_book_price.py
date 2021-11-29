from datetime import datetime
from src.book_scraper.get_book_dynamic_data.scrap_price import scrap_price


def get_book_price(soup):
    price = scrap_price(soup)
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    price_element = [{"date": date, "value": price}]
    return price_element
