import os
import subprocess
from pymongo import MongoClient
from flask import Flask, render_template, jsonify
import threading
import time

# Project constants
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WEB_DIR = os.path.join(BASE_DIR, "web")
LOGS_DIR = os.path.join(BASE_DIR, "logs")
CHARTS_EMBED_URL = "https://charts.mongodb.com/charts-project-0-jtbjnkn/dashboards/674ab727-0ae2-4a05-82f9-8b370f272d61"

# MongoDB connection string
MONGO_URI = os.getenv(
    "MONGO_URI",
    "mongodb+srv://bob:bobmanas@gbob.4dq6l.mongodb.net/?retryWrites=true&w=majority&appName=Gbob",
)

# Flask app setup
app = Flask(__name__)

# Set up logging
def setup_logging():
    if not os.path.exists(LOGS_DIR):
        os.makedirs(LOGS_DIR)
    log_file = os.path.join(LOGS_DIR, "growbot.log")
    if not os.path.exists(log_file):
        open(log_file, "w").close()
    print(f"✅ Logging initialized at {log_file}")

# MongoDB setup
def setup_mongodb():
    print("🔧 Setting up MongoDB...")
    try:
        client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
        client.server_info()  # Trigger a connection attempt
        db = client["growbot_db"]

        # Sample data for testing
        microgreens_data = [
            {"name": "Sunflower", "light_hours": 16, "temperature_range": "20-25°C", "humidity": "60-70%"},
            {"name": "Wheatgrass", "light_hours": 12, "temperature_range": "18-22°C", "humidity": "50-60%"},
        ]

        db.microgreens.drop()
        db.microgreens.insert_many(microgreens_data)
        print("✅ MongoDB setup complete.")
    except Exception as e:
        print(f"❌ MongoDB setup failed: {e}")
        raise

# Real-time updates using change streams
def monitor_changes():
    print("🔧 Setting up MongoDB change streams...")
    try:
        client = MongoClient(MONGO_URI)
        db = client["growbot_db"]
        with db.microgreens.watch() as stream:
            print("✅ Watching for real-time changes...")
            for change in stream:
                print(f"🔔 Change detected: {change}")
    except Exception as e:
        print(f"❌ Failed to set up change streams: {e}")

# Start monitoring changes in a background thread
def start_change_stream_monitor():
    thread = threading.Thread(target=monitor_changes, daemon=True)
    thread.start()

# Flask routes
@app.route("/")
def dashboard():
    """
    Main dashboard route to embed MongoDB Charts.
    """
    return render_template("dashboard.html", charts_url=CHARTS_EMBED_URL)

@app.route("/data")
def get_microgreens_data():
    """
    API endpoint to fetch microgreens data.
    """
    try:
        client = MongoClient(MONGO_URI)
        db = client["growbot_db"]
        microgreens = list(db.microgreens.find({}, {"_id": 0}))
        return jsonify(microgreens)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Create or update the .env file
def create_env_file():
    env_path = os.path.join(BASE_DIR, ".env")
    if not os.path.exists(env_path):
        with open(env_path, "w") as f:
            f.write("CUSTOMER_BOT_TOKEN=7586067879:AAFtBcPcu8_eQYVmUqmpDltASX7TLZObwkI\n")
            f.write("ADMIN_BOT_TOKEN=7809993846:AAH9wZfc0sdJu2aLInLj-G5rTyAZjNPRRK4\n")
            f.write(f"MONGO_URI=mongodb+srv://bob:<db_password>@gbob.4dq6l.mongodb.net/?retryWrites=true&w=majority&appName=Gbob\n")
        print("✅ .env file created. Update it with your bot tokens.")
    else:
        print("✅ .env file already exists. Ensure it contains the correct tokens.")

# Replace web template for embedding MongoDB Charts
def replace_dashboard_template():
    template_path = os.path.join(WEB_DIR, "templates", "dashboard.html")
    os.makedirs(os.path.dirname(template_path), exist_ok=True)
    with open(template_path, "w") as f:
        f.write(f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>GrowBot Dashboard</title>
        </head>
        <body>
            <h1>GrowBot Dashboard</h1>
            <iframe
                src="{CHARTS_EMBED_URL}"
                width="100%"
                height="600"
                frameborder="0">
            </iframe>
        </body>
        </html>
        """)
    print(f"✅ Dashboard template replaced at {template_path}")

# Start Flask app
def start_flask_app():
    print("🚀 Starting Flask app at http://localhost:5000...")
    app.run(debug=True, host="0.0.0.0", port=5000)

if __name__ == "__main__":
    print("=== GrowBot MongoDB Charts Integration Script ===")
    try:
        setup_logging()
        setup_mongodb()
        create_env_file()
        replace_dashboard_template()
        start_change_stream_monitor()
        start_flask_app()
    except Exception as e:
        print(f"❌ Setup failed: {e}")
