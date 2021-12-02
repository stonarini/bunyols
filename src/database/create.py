from .connection import connection


def create_one(document):

    assert isinstance(document, dict), "document need to be a dictionary type object"

    database = connection()
    database.catalog.insert_one(document)
