from flask import Flask, jsonify
from utils import check_connection_status, cache

app = Flask(__name__)

# Initialize caching
cache.init_app(app)

@app.route('/')
def home():
    """Endpoint to show MongoDB connection status."""
    status = check_connection_status()
    return jsonify({"connection_status": status})

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=8000, debug=True)
