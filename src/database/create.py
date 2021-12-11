from .connection import connection
from pymongo.errors import WriteError


def create_one(document):

    assert isinstance(document, dict), "document need to be a dictionary type object"

    database = connection()
    print("Inserting:", document)
    try:
        database.insert_one(document)
    except WriteError:
        print("Error, does the document follow json schema?")
