import pytest
import src.database as database


@pytest.mark.test_update_invalid_data
def test_update_invalid_data():
    database.update_one({"ISBN_13": "978"}, {"$set": {"test": 1}})


@pytest.mark.test_update_family
def test_update_family():
    database.update_one({"ISBN_13": "978"}, {"$set": {"family": "family"}})


@pytest.mark.test_valid_update
def test_valid_update():
    new_data = {
        "price": [{"date": "", "value": "$00"}],
        "reviews": {"total_reviews": 80, "5": 10, "4": 8, "3": 6, "2": 4, "1": 2},
    }
    database.update_one(
        {"ISBN_13": "978"},
        {
            "$push": {"price": new_data["price"][0]},
            "$set": {
                "reviews": new_data["reviews"],
            },
        },
    )
