import pytest
import src.database as database


@pytest.mark.test_update_invalid_data
def test_update_invalid_data():
    database.update_one({"ISBN_13": "1"}, {"$set": {"test": 1}})


@pytest.mark.test_update_family
def test_update_family():
    database.update_one({"ISBN_13": "1"}, {"$set": {"family": "my family"}})


@pytest.mark.test_valid_update
def test_valid_update():
    new_data = {
        "price": [{"date": "34/89/3", "value": "$32"}],
        "reviews": {"total_reviews": 1234, "5": 2, "4": 75, "3": 89, "2": 67, "1": 0},
    }
    database.update_one(
        {"ISBN_13": "1"},
        {
            "$push": {"price": new_data["price"][0]},
            "$set": {
                "reviews": new_data["reviews"],
            },
        },
    )
