from .connection import connection


def create_one(document):

    assert isinstance(document, dict), "document need to be a dictionary type object"

    database = connection()
    print("Inserting:", document)
    database.insert_one(document)
