from pymongo import MongoClient

def get_db():
    """Returns a MongoDB client for the GrowBot database."""
    client = MongoClient("mongodb://localhost:27017/")  # Replace with MongoDB Atlas URI if needed
    return client["growbot_db"]
