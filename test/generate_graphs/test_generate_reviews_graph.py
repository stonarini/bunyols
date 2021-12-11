import os
import shutil
import pytest
from src.generate_graphs.generate_reviews_graph import generate_reviews_graph


def test_gen_reviews_graph():
    os.mkdir("test/generate_graphs/svg/")
    reviews = {"5": 40, "4": 20, "3": 10, "2": 5, "1": 5}
    total_reviews = 80
    generate_reviews_graph("test/generate_graphs/svg", total_reviews, reviews)
    shutil.rmtree("test/generate_graphs/svg/")
