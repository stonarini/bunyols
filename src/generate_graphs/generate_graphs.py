from generate_graphs.generate_price_graph import generate_price_graph
from generate_graphs.generate_reviews_graph import generate_reviews_graph


def generate_graphs(path, reviews, price):

    prices = [item["value"] for item in price]
    dates = [item["date"] for item in price]
    generate_price_graph(path, dates, prices)

    total_reviews = reviews.pop("total_reviews")
    generate_reviews_graph(path, total_reviews, reviews)
