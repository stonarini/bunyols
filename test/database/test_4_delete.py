import pytest
import pytest
import src.database as database


@pytest.mark.test_delete
def test_delete():
    database.delete_one({"title": "title"})


@pytest.mark.test_invalid_delete
def test_invalid_delete():
    database.delete_one({"title": "title don't exist"})
