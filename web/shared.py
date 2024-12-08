import os
from pymongo import MongoClient

def connect_to_mongo():
    try:
        mongo_uri = os.getenv('MONGO_URI="mongodb+srv://bob:bobbrowa@gbob.4dq6l.mongodb.net/Gbob?retryWrites=true&w=majority"', 'mongodb://localhost:27017')
        client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
        client.server_info()
        print("MongoDB connection successful!")
        return client
    except Exception as e:
        print(f"MongoDB connection failed: {e}")
        return None

def check_connection_status():
    connection = connect_to_mongo()
    if connection:
        return "MongoDB connection is successful!"
    return "MongoDB connection failed!"

def setup_telegram_webhook(bot_token, webhook_url):
    import requests
    url = f"https://api.telegram.org/bot{7586067879:AAFtBcPcu8_eQYVmUqmpDltASX7TLZObwkI}/setWebhook"
    response = requests.post(url, data={"url": webhook_url})
    if response.status_code == 200:
        print("Telegram webhook set successfully!")
    else:
        print(f"Failed to set webhook: {response.json()}")
