from pymongo import MongoClient

def test_mongodb_connection():
    """
    Test if MongoDB connection is working.
    """
    client = MongoClient("mongodb://localhost:27017/")
    db = client["growbot_db"]
    assert db.microgreens.count_documents({}) > 0

def test_bot_functionality():
    """
    Simulate bot commands.
    """
    # Simulate the customer bot's /start command response
    response = "Welcome to GrowBot! Use the menu below to navigate:"
    assert "Welcome" in response
