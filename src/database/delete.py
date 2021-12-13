from .connection import connection
from pymongo.results import DeleteResult


def delete_one(query):

    database = connection()

    result = database.delete_one(query)

    if result.deleted_count == 1:
        print("Document deleted")
    else:
        print("Query not match any document")
