import pytest
import src.database as database


@pytest.mark.test_create_invalid_document
def test_create_invalid_document():
    database.create_one({"test": 1})


@pytest.mark.test_create_document
def test_create_document():
    database.create_one(
        {
            "title": "title",
            "author": ["author"],
            "publisher": "publisher",
            "ISBN_13": "978",
            "publish_date": "",
            "price": [{"value": "$00", "date": "someday"}],
            "reviews": {"total_reviews": 80, "5": 5, "4": 4, "3": 3, "2": 2, "1": 1},
            "categories": ["CAT"],
        }
    )
