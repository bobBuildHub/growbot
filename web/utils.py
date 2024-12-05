import os
from flask_caching import Cache
from pymongo import MongoClient

# Configure Flask-Caching
cache = Cache(config={'CACHE_TYPE': 'simple'})

def connect_to_mongo():
    """Connect to MongoDB and return the database instance."""
    try:
        mongo_uri = os.getenv('MONGO_URI', 'mongodb+srv://bob:bobbrowa@gbob.4dq6l.mongodb.net/?retryWrites=true&w=majority&appName=Gbob')
        client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)  # Set timeout to handle connection issues
        db = client.get_database()
        # Test if the database is available
        client.server_info()
        print("MongoDB connection successful!")
        return db
    except Exception as e:
        print(f"MongoDB connection failed: {e}")
        return None

def check_connection_status():
    """Check the status of MongoDB connection."""
    connection = connect_to_mongo()
    if connection:
        return "MongoDB connection is successful!"
    return "MongoDB connection failed!"
