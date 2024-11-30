from flask import Flask, jsonify, render_template, request, abort, redirect, url_for
from flask_socketio import SocketIO, emit
from pymongo import MongoClient
from bson.json_util import dumps
from datetime import datetime
import logging

# Initialize Flask app and SocketIO
app = Flask(__name__)
app.config["SECRET_KEY"] = "super_secret_key"
socketio = SocketIO(app)

# MongoDB configuration
MONGO_URI = "mongodb+srv://bob:bobbrowa@gbob.4dq6l.mongodb.net/?retryWrites=true&w=majority&appName=Gbob"
client = MongoClient(MONGO_URI)
db = client["growbot_db"]

# Set up logging
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Routes

@app.route("/")
def home():
    """Render the main dashboard with gardens."""
    try:
        gardens = list(db.gardens.find({}, {"_id": 0, "name": 1, "location": 1}))
        return render_template("dashboard.html", gardens=gardens)
    except Exception as e:
        logging.error(f"Error loading gardens: {str(e)}")
        abort(500, description="Error loading gardens.")

@app.route("/admin")
def admin_panel():
    """Render the admin panel with user and garden management."""
    try:
        users = list(db.users.find({}, {"_id": 0, "name": 1, "email": 1}))
        gardens = list(db.gardens.find({}, {"_id": 0, "name": 1, "location": 1, "user_id": 1}))
        return render_template("admin.html", users=users, gardens=gardens)
    except Exception as e:
        logging.error(f"Error loading admin data: {str(e)}")
        abort(500, description="Error loading admin data.")

@app.route("/api/gardens", methods=["GET"])
def get_gardens():
    """Fetch all gardens."""
    try:
        gardens = list(db.gardens.find({}, {"_id": 0}))
        return jsonify(gardens)
    except Exception as e:
        logging.error(f"Error fetching gardens: {str(e)}")
        return jsonify({"error": "Error fetching gardens"}), 500

@app.route("/api/gardens", methods=["POST"])
def add_garden():
    """Add a new garden."""
    data = request.json
    try:
        new_garden = {
            "name": data["name"],
            "location": data["location"],
            "user_id": data.get("user_id", 0),
            "created_at": datetime.utcnow()
        }
        db.gardens.insert_one(new_garden)
        logging.info(f"New garden added: {new_garden}")
        return jsonify({"message": "Garden added successfully"}), 201
    except Exception as e:
        logging.error(f"Error adding garden: {str(e)}")
        return jsonify({"error": "Error adding garden"}), 500

@app.route("/api/gardens/<int:garden_id>/analytics", methods=["GET"])
def garden_analytics(garden_id):
    """Fetch analytics for a specific garden."""
    try:
        sensors = list(db.sensors.find({"garden_id": garden_id}, {"_id": 0}))
        if not sensors:
            return jsonify({"message": "No analytics data available"}), 404
        return jsonify(sensors)
    except Exception as e:
        logging.error(f"Error fetching analytics for garden {garden_id}: {str(e)}")
        return jsonify({"error": "Error fetching analytics"}), 500

@app.route("/api/users", methods=["GET"])
def get_users():
    """Fetch all users."""
    try:
        users = list(db.users.find({}, {"_id": 0}))
        return jsonify(users)
    except Exception as e:
        logging.error(f"Error fetching users: {str(e)}")
        return jsonify({"error": "Error fetching users"}), 500

@app.route("/api/users", methods=["POST"])
def add_user():
    """Add a new user."""
    data = request.json
    try:
        new_user = {
            "name": data["name"],
            "email": data["email"],
            "created_at": datetime.utcnow()
        }
        db.users.insert_one(new_user)
        logging.info(f"New user added: {new_user}")
        return jsonify({"message": "User added successfully"}), 201
    except Exception as e:
        logging.error(f"Error adding user: {str(e)}")
        return jsonify({"error": "Error adding user"}), 500

@app.route("/api/gardens/<int:garden_id>", methods=["DELETE"])
def delete_garden(garden_id):
    """Delete a garden by ID."""
    try:
        result = db.gardens.delete_one({"id": garden_id})
        if result.deleted_count == 0:
            return jsonify({"message": "Garden not found"}), 404
        logging.info(f"Garden deleted: {garden_id}")
        return jsonify({"message": "Garden deleted successfully"})
    except Exception as e:
        logging.error(f"Error deleting garden {garden_id}: {str(e)}")
        return jsonify({"error": "Error deleting garden"}), 500

@app.route("/charts")
def charts_dashboard():
    """Embed MongoDB Charts into the dashboard."""
    try:
        return render_template("charts.html")
    except Exception as e:
        logging.error(f"Error loading charts: {str(e)}")
        abort(500, description="Error loading charts.")

@socketio.on("connect")
def handle_connect():
    """Handle client connection."""
    logging.info("Client connected to SocketIO.")

@socketio.on("disconnect")
def handle_disconnect():
    """Handle client disconnection."""
    logging.info("Client disconnected from SocketIO.")

# Error Handlers

@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors."""
    return jsonify({"error": "Not Found", "message": str(error)}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({"error": "Internal Server Error", "message": str(error)}), 500

# Main Execution
if __name__ == "__main__":
    logging.info("Starting GrowBot application...")
    socketio.run(app, host="0.0.0.0", port=5000)
