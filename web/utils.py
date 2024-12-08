import os
from pymongo import MongoClient

def connect_to_mongo():
    """Connect to MongoDB using the URI from environment variables."""
    try:
        mongo_uri = os.getenv(
            'MONGO_URI',
            'mongodb+srv://bob:bobbrowa@gbob.4dq6l.mongodb.net/?retryWrites=true&w=majority&appName=Gbob'
        )
        client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
        client.server_info()  # Test connection
        print("MongoDB connection successful!")
        return client.get_database()
    except Exception as e:
        print(f"MongoDB connection failed: {e}")
        return None

def check_connection_status():
    """Check MongoDB connection status."""
    db = connect_to_mongo()
    return "MongoDB connection is successful!" if db else "MongoDB connection failed!"
