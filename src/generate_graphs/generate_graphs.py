import os
from .generate_price_graph import generate_price_graph
from .generate_reviews_graph import generate_reviews_graph


def generate_graphs(path, reviews, price):
    if not os.path.exists(path):
        os.makedirs(path)

    prices = [item["value"] for item in price if item["value"] != "Na"]
    dates = [item["date"] for item in price if item["value"] != "Na"]
    if prices:
        generate_price_graph(path, dates, prices)

    total_reviews = reviews.pop("total_reviews")
    generate_reviews_graph(path, total_reviews, reviews)
