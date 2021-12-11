from .connection import connection


def find_one(query):
    database = connection()
    book = database.find_one(query)
    return book
