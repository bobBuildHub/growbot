from flask import Flask, jsonify, request
from web.utils import connect_to_mongo, cache
import os
import time
from flask_caching import Cache

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})


app = Flask(__name__)

@app.route('/')
def index():
    return "Flask app is running!"

@app.route('/api/data', methods=['GET'])
@cache.cached(timeout=60)  # Cache the response for 60 seconds
def get_data():
    try:
        db = connect_to_mongo()
        if db:
            collection = db.my_collection
            data = list(collection.find())
            return jsonify(data)
        else:
            return jsonify({"error": "Database connection failed"}), 500
    except Exception as e:
        return jsonify({"error": f"Error fetching data: {e}"}), 500

@app.route('/api/data', methods=['POST'])
def insert_data():
    try:
        data = request.get_json()
        if not data or "name" not in data or "value" not in data:
            return jsonify({"error": "Invalid data. 'name' and 'value' are required."}), 400

        db = connect_to_mongo()
        if db:
            collection = db.my_collection
            collection.insert_one(data)
            return jsonify({"message": "Data inserted successfully!"}), 201
        else:
            return jsonify({"error": "Database connection failed"}), 500
    except Exception as e:
        return jsonify({"error": f"Error inserting data: {e}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
