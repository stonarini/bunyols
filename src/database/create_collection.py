from collections import OrderedDict
import json


def create_collection(database):
    with open("src/database/schema.json", "r") as schema:
        database_schema = json.loads(schema.read())

    database_schema = OrderedDict(database_schema)

    database.create_collection("catalog")
    database.command(database_schema)
