import os
from dotenv import load_dotenv
from pymongo import MongoClient, errors
from pymongo.collection import Collection
from time import sleep

# Load environment variables from .env file
load_dotenv()

# Retrieve MongoDB URI from environment variables
MONGO_URI = os.getenv("MONGO_URI")

# Retry logic settings
MAX_RETRIES = 5
RETRY_DELAY = 5  # seconds

# Initialize the MongoClient
client = None

# MongoDB database name
DB_NAME = "Gbob"  # Replace with your database name
COLLECTION_NAME = "users"  # Default collection name for users

def connect_to_mongo():
    global client
    attempts = 0
    while attempts < MAX_RETRIES:
        try:
            print("Connecting to MongoDB...")
            # Establish a connection with the MongoDB server
            client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)  # Timeout after 5 seconds
            # Try to fetch server information (this will throw an exception if connection fails)
            client.admin.command('ping')
            print("MongoDB connected successfully!")
            return client  # Return the client object if successful
        except errors.ServerSelectionTimeoutError as err:
            attempts += 1
            print(f"Connection failed (attempt {attempts}/{MAX_RETRIES}): {err}")
            sleep(RETRY_DELAY)  # Wait before retrying
        except Exception as err:
            print(f"Unexpected error: {err}")
            break
    if attempts == MAX_RETRIES:
        print("Unable to connect to MongoDB after multiple attempts.")
    return None

def get_user_collection():
    """Returns the users collection object."""
    if client:
        db = client[DB_NAME]  # Access the database
        return db[COLLECTION_NAME]  # Access the 'users' collection
    return None

def ensure_users_collection_exists():
    """Ensure that the users collection exists."""
    collection = get_user_collection()
    if collection is None:
        print("Error: users collection does not exist!")
        return False
    return True

def create_user(username, password, email):
    """Create a new user in the database."""
    collection = get_user_collection()
    if collection:
        # Ensure that the user doesn't already exist
        if collection.find_one({"username": username}):
            print(f"Error: User with username '{username}' already exists.")
            return False
        # Insert the new user document
        user = {
            "username": username,
            "password": password,  # In practice, hash the password
            "email": email
        }
        collection.insert_one(user)
        print(f"User '{username}' created successfully.")
        return True
    return False

def get_user(username):
    """Get a user by their username."""
    collection = get_user_collection()
    if collection:
        return collection.find_one({"username": username})
    return None

def update_user(username, new_data):
    """Update user data."""
    collection = get_user_collection()
    if collection:
        result = collection.update_one({"username": username}, {"$set": new_data})
        if result.modified_count > 0:
            print(f"User '{username}' updated successfully.")
            return True
        else:
            print(f"No changes made for user '{username}'.")
            return False
    return False

def delete_user(username):
    """Delete a user by their username."""
    collection = get_user_collection()
    if collection:
        result = collection.delete_one({"username": username})
        if result.deleted_count > 0:
            print(f"User '{username}' deleted successfully.")
            return True
        else:
            print(f"Error: User '{username}' not found.")
            return False
    return False

def list_users():
    """List all users."""
    collection = get_user_collection()
    if collection:
        users = collection.find()
        for user in users:
            print(user)
    else:
        print("Error: Cannot list users - users collection not available.")

# Example usage
if __name__ == "__main__":
    # Connect to MongoDB
    if connect_to_mongo():
        # Ensure the 'users' collection exists
        if ensure_users_collection_exists():
            # Create, read, update, delete users for testing
            create_user("testuser", "password123", "testuser@example.com")
            create_user("anotheruser", "password456", "anotheruser@example.com")

            # Get user by username
            user = get_user("testuser")
            print("Fetched user:", user)

            # Update user info
            update_user("testuser", {"email": "newemail@example.com"})

            # List all users
            list_users()

            # Delete user
            delete_user("anotheruser")
