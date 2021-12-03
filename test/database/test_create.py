from pymongo.errors import WriteError
import pytest
from src.database.create import create_one


@pytest.mark.test_create_invalid_document
def test_create_invalid_document():
    try:
        create_one({"test": 1})
    except WriteError:
        assert True
    else:
        assert False
