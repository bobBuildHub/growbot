from flask import Flask, jsonify
from flask_caching import Cache
from utils import check_connection_status

app = Flask(__name__)
cache = Cache(config={'CACHE_TYPE': 'simple'})
cache.init_app(app)

@app.route('/')
def home():
    """Root endpoint."""
    return jsonify({"message": "Welcome to the Web Service!"})

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({"status": "running", "connection": check_connection_status()})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
