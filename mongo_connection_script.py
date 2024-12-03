import os
import time
from pymongo import MongoClient, errors
from colorama import init, Fore
from tqdm import tqdm

# Initialize colorama for colored console output
init(autoreset=True)

# MongoDB URI - Replace this with your MongoDB URI
MONGO_URI = "mongodb+srv://bob:bobbrowa@gbob.4dq6l.mongodb.net/?retryWrites=true&w=majority&appName=Gbob"

# Default database name - Specify a database to use
DB_NAME = "GbobDB"  # Replace with your actual database name

# Initialize the MongoDB client
client = None

# Retry configuration
MAX_RETRIES = 5
RETRY_DELAY = 5  # seconds


def connect_to_mongo():
    """Connect to MongoDB Atlas with retries."""
    global client
    attempts = 0
    with tqdm(total=MAX_RETRIES, desc="MongoDB Connection", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} attempts") as pbar:
        while attempts < MAX_RETRIES:
            try:
                print(Fore.YELLOW + f"Attempting to connect to MongoDB Atlas... (Attempt {attempts + 1}/{MAX_RETRIES})")
                client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
                client.admin.command('ping')  # Ping the server to check connectivity
                print(Fore.GREEN + "MongoDB connection successful!")
                pbar.update(MAX_RETRIES - attempts)  # Full progress
                return client
            except errors.ServerSelectionTimeoutError as err:
                attempts += 1
                print(Fore.RED + f"Connection failed: {err}")
                if attempts < MAX_RETRIES:
                    print(Fore.YELLOW + f"Retrying in {RETRY_DELAY} seconds...")
                time.sleep(RETRY_DELAY)
            except Exception as err:
                print(Fore.RED + f"Unexpected error: {err}")
                break
            pbar.update(1)  # Update progress bar on each attempt

    if attempts == MAX_RETRIES:
        print(Fore.RED + "Unable to connect to MongoDB after multiple attempts.")
    return None


def get_collection(collection_name):
    """Get a MongoDB collection."""
    if client:
        db = client[DB_NAME]  # Use the specified database
        return db[collection_name]  # Return the specified collection
    return None


def create_user(username, email):
    """Create a new user in the MongoDB collection."""
    collection = get_collection('users')
    if collection is not None:  # Fixed the comparison here (previously `if collection:`)
        existing_user = collection.find_one({"username": username})
        if existing_user:
            print(Fore.RED + f"User with username {username} already exists.")
            return
        print(Fore.YELLOW + f"Creating user '{username}'...")
        with tqdm(total=100, desc="Creating User", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} %") as pbar:
            collection.insert_one({"username": username, "email": email})
            time.sleep(1)  # Simulate some time taken for insertion
            pbar.update(100)
            print(Fore.GREEN + f"User {username} created successfully!")
    else:
        print(Fore.RED + "Error: MongoDB connection is not established.")


def get_user(username):
    """Retrieve a user from the MongoDB collection by username."""
    collection = get_collection('users')
    if collection is not None:  # Fixed the comparison here
        print(Fore.YELLOW + f"Fetching user '{username}'...")
        with tqdm(total=100, desc="Fetching User", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} %") as pbar:
            user = collection.find_one({"username": username})
            time.sleep(1)  # Simulate some time taken for fetching
            pbar.update(100)
            if user:
                print(Fore.GREEN + f"User found: {user}")
            else:
                print(Fore.YELLOW + f"No user found with username {username}.")
    else:
        print(Fore.RED + "Error: MongoDB connection is not established.")


def update_user(username, update_data):
    """Update user information."""
    collection = get_collection('users')
    if collection is not None:  # Fixed the comparison here
        print(Fore.YELLOW + f"Updating user '{username}'...")
        with tqdm(total=100, desc="Updating User", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} %") as pbar:
            result = collection.update_one({"username": username}, {"$set": update_data})
            time.sleep(1)  # Simulate some time taken for updating
            pbar.update(100)
            if result.matched_count > 0:
                print(Fore.GREEN + f"User {username} updated successfully.")
            else:
                print(Fore.YELLOW + f"No user found with username {username}.")
    else:
        print(Fore.RED + "Error: MongoDB connection is not established.")


def delete_user(username):
    """Delete a user from the MongoDB collection."""
    collection = get_collection('users')
    if collection is not None:  # Fixed the comparison here
        print(Fore.YELLOW + f"Deleting user '{username}'...")
        with tqdm(total=100, desc="Deleting User", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} %") as pbar:
            result = collection.delete_one({"username": username})
            time.sleep(1)  # Simulate some time taken for deletion
            pbar.update(100)
            if result.deleted_count > 0:
                print(Fore.GREEN + f"User {username} deleted successfully.")
            else:
                print(Fore.YELLOW + f"No user found with username {username}.")
    else:
        print(Fore.RED + "Error: MongoDB connection is not established.")


def main():
    """Main function to connect and run basic tests."""
    print(Fore.CYAN + "="*40)
    print(Fore.CYAN + "Starting MongoDB connection test...\n")

    # Try to connect to MongoDB Atlas
    if not connect_to_mongo():
        print(Fore.RED + "MongoDB connection failed. Exiting.")
        return

    # Test basic CRUD operations
    print("\nCreating user 'testuser'...")
    create_user('testuser', 'testuser@example.com')

    print("\nFetching 'testuser'...")
    get_user('testuser')

    print("\nUpdating 'testuser' email...")
    update_user('testuser', {"email": "newemail@example.com"})

    print("\nFetching updated 'testuser'...")
    get_user('testuser')

    print("\nDeleting 'testuser'...")
    delete_user('testuser')

    print("\nFetching 'testuser' after deletion...")
    get_user('testuser')

    print(Fore.CYAN + "="*40)
    print(Fore.GREEN + "All operations completed successfully!")


if __name__ == "__main__":
    main()
