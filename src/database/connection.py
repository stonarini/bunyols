from pymongo import MongoClient
from pymongo.errors import ConfigurationError
from .config import URI


def connection():

    assert isinstance(URI, str), "URI need to be a string type object"

    try:
        client = MongoClient(URI)
    except ConfigurationError:
        print("Connection failed")
    else:
        database = client.library
        # serverStatusResult = database.command("serverStatus")
        # print(serverStatusResult)
        return database


connection()
