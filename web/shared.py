from pymongo import MongoClient
from pymongo.errors import ConnectionError

def connect_to_mongo():
    try:
        client = MongoClient("mongodb://localhost:27017")  # Replace with actual MongoDB URI
        client.admin.command("ping")  # Ping MongoDB to test the connection
        return client
    except ConnectionError:
        return None

cache = {}
