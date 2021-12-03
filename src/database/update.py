from .connection import connection
from pymongo.errors import WriteError


def update_one(document, filter):

    assert isinstance(document, dict), "document need to be a dictionary type object"

    database = connection()
    try:
        database.update_one(filter, document)
    except WriteError:
        print("Error, does the document follow json schema?")
