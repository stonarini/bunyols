from .connection import connection
from pymongo.errors import WriteError


def update_one(query, document):

    database = connection()
    try:
        database.update_one(query, document)
    except WriteError:
        print("Error, does the document follow json schema?")
