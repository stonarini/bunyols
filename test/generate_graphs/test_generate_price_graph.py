import os
import pytest
import shutil
from src.generate_graphs.generate_price_graph import generate_price_graph


def test_gen_price_graph():
    os.mkdir("test/generate_graphs/svg/")
    price = [
        {"date": "2021-12-06 16:56:17", "value": "$15.43"},
        {"date": "2021-12-07 16:56:17", "value": "$16.43"},
        {"date": "2021-12-08 16:56:17", "value": "$17.43"},
        {"date": "2021-12-09 16:56:17", "value": "$16.43"},
        {"date": "2022-12-09 16:56:17", "value": "$16.43"},
    ]

    prices = [item["value"] for item in price if item["value"] != "Na"]
    dates = [item["date"] for item in price if item["value"] != "Na"]

    generate_price_graph("test/generate_graphs/svg", dates, prices)
    shutil.rmtree("test/generate_graphs/svg/")
