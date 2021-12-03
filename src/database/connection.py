from typing import Collection
from pymongo import MongoClient
from pymongo.errors import ConfigurationError
from .config import URI
from .create_collection import create_collection


def connection():

    assert isinstance(URI, str), "URI need to be a string type object"

    try:
        client = MongoClient(URI)
    except ConfigurationError:
        print("Connection failed")
    else:
        database = client["bunyols-library"]
        if "catalog" not in database.list_collection_names():
            create_collection(database)

        collection = database["catalog"]
        return collection
