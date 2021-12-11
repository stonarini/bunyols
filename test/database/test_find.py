import pytest
import src.database as database


@pytest.mark.test_read_nonexisting_document
def test_read_nonexisting_document():
    ISBN = {"ISBN_13": "2"}
    book = database.find_one(ISBN)
    assert book is None


@pytest.mark.test_read_document
def test_read_document():
    ISBN = {"ISBN_13": "9780735619678"}
    book = database.find_one(ISBN)
    assert book is not None
