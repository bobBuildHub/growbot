import os
import subprocess
from pymongo import MongoClient

def install_dependencies():
    """
    Installs required Python packages.
    """
    print("Installing dependencies...")
    subprocess.run(
        ["pip", "install", "python-telegram-bot", "pymongo", "flask", "pytest", "colorama"],
        check=True
    )
    print("Dependencies installed.")

def setup_mongodb():
    """
    Sets up MongoDB collections and inserts sample microgreens data.
    """
    print("Setting up MongoDB...")
    client = MongoClient("mongodb://localhost:27017/")
    db = client["growbot_db"]

    microgreens_data = [
        {
            "name": "Sunflower",
            "light_hours": 16,
            "watering_stages": ["Daily misting until sprouted", "Twice daily thereafter"],
            "temperature_range": "20-25°C",
            "humidity": "60-70%",
        },
        {
            "name": "Wheatgrass",
            "light_hours": 12,
            "watering_stages": ["Daily soaking for germination", "Keep moist thereafter"],
            "temperature_range": "18-22°C",
            "humidity": "50-60%",
        },
    ]

    db.microgreens.drop()  # Clean up any old data
    db.microgreens.insert_many(microgreens_data)
    print("Microgreens data inserted into MongoDB.")

def create_env_file():
    """
    Creates a .env file for environment variables.
    """
    if not os.path.exists(".env"):
        with open(".env", "w") as f:
            f.write("CUSTOMER_BOT_TOKEN=your_customer_bot_token\n")
            f.write("ADMIN_BOT_TOKEN=your_admin_bot_token\n")
            f.write(f"MONGO_URI=mongodb+srv://bobik lez:bobbrowa@gbob.4dq6l.mongodb.net/?retryWrites=true&w=majority&appName=Gbob\n")

        print(".env file created. Update it with your bot tokens.")

def start_bots_and_web():
    """
    Starts the customer bot, admin bot, and Flask web server.
    """
    print("Starting bots and webpage...")
    subprocess.Popen(["python", "bots/customer_bot/customer_bot.py"])
    subprocess.Popen(["python", "bots/admin_bot/admin_bot.py"])
    subprocess.Popen(["python", "web/app.py"])
    print("Bots and webpage are running. Access the webpage at http://localhost:5000")

if __name__ == "__main__":
    print("=== GrowBot Setup ===")
    install_dependencies()
    setup_mongodb()
    create_env_file()
    print("\nRun the following command to start everything:")
    print("python setup.py start")
    print("\nUse 'python setup.py test' to run tests.")
