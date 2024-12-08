import os
from pymongo import MongoClient
import requests
from flask import Flask, request, jsonify
from pymongo import MongoClient

# Load the MongoDB URI from environment variables
MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongodb:27017/GbobDB")

# Establish the MongoDB client
mongo_client = MongoClient(MONGO_URI)

# Explicitly specify the database name
db_name = "mydatabase"  # Replace with your database name
db = mongo_client[db_name]

# Test connection
try:
    mongo_client.server_info()  # This will raise an exception if MongoDB is unreachable
    print(f"Connected to MongoDB database: {db_name}")
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")

# The rest of your bot logic




