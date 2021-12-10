import pytest
from src.generate_graphs.generate_reviews_graph import generate_reviews_graph


def test_gen_reviews_graph():
    reviews = {"total_reviews": 80, "5": 40, "4": 20, "3": 10, "2": 5, "1": 5}
    generate_reviews_graph("test/generate_graphs/svg/", reviews)
