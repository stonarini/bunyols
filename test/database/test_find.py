import pytest
from bson import ObjectId
import src.database as database


@pytest.mark.test_read_nonexisting_document
def test_read_nonexisting_document():
    ISBN = {"ISBN_13": "2"}
    book = database.find_one(ISBN)
    assert book is None


@pytest.mark.test_read_document
def test_read_document():
    ISBN = {"ISBN_13": "1"}
    book = database.find_one(ISBN)
    assert book == {
        "_id": ObjectId("61ae17b2e391be83527988a0"),
        "title": "lol",
        "author": ["someone"],
        "publisher": "lol",
        "ISBN_13": "1",
        "publish_date": "someday",
        "price": [
            {"value": "$43", "date": "someday"},
            {"date": "34/89/3", "value": "$32"},
        ],
        "reviews": {"total_reviews": 1234, "5": 2, "4": 75, "3": 89, "2": 67, "1": 0},
        "categories": ["IT"],
        "family": "my family",
    }
