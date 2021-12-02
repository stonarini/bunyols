import pytest
from src.database.create import create_one


@pytest.mark.test_create_one
def test_create_one():
    create_one({"test": 1})
