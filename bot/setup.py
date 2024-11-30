import os
import subprocess
import sys
import time
from colorama import Fore, Style, init

init(autoreset=True)  # Initialize Colorama for colorized output

def pretty_print_section(title):
    """
    Prints a visually distinct section header.
    """
    print(Fore.YELLOW + "=" * 60)
    print(Fore.CYAN + f"{' ' * ((60 - len(title)) // 2)}{title}")
    print(Fore.YELLOW + "=" * 60)


def progress_bar(task, seconds=2):
    """
    Simulates a progress bar for a given task.
    """
    print(Fore.GREEN + f"Starting: {task}")
    for i in range(1, 21):
        sys.stdout.write(Fore.GREEN + "█")
        sys.stdout.flush()
        time.sleep(seconds / 20)
    print(Fore.GREEN + f" {task} complete!\n")


def create_directory_structure(base_dir):
    """
    Creates the required directory structure for the GrowBot project.
    """
    pretty_print_section("CREATING DIRECTORY STRUCTURE")
    directories = [
        "logs",
        "bots/customer_bot",
        "bots/admin_bot",
        "bots/commands",
        "tests",
    ]
    for directory in directories:
        path = os.path.join(base_dir, directory)
        os.makedirs(path, exist_ok=True)
        print(Fore.YELLOW + f"✅ Created directory: {path}")


def create_file(filepath, content):
    """
    Creates a file with the specified content.
    """
    with open(filepath, "w") as f:
        f.write(content)
    print(Fore.GREEN + f"✅ Created: {filepath}")


def install_dependencies():
    """
    Installs required Python packages.
    """
    pretty_print_section("INSTALLING DEPENDENCIES")
    print(Fore.BLUE + "Installing required Python packages...")
    try:
        subprocess.run(
            ["pip", "install", "python-telegram-bot", "pymongo", "pytest", "colorama"],
            check=True
        )
        print(Fore.GREEN + "✅ Dependencies installed successfully!")
    except subprocess.CalledProcessError as e:
        print(Fore.RED + "❌ Failed to install dependencies!")
        sys.exit(1)


def setup_mongodb_connection():
    """
    Returns the MongoDB connection code as a string.
    """
    return """\
from pymongo import MongoClient

def get_db():
    \"\"\"Returns a MongoDB client for the GrowBot database.\"\"\"
    client = MongoClient("mongodb://localhost:27017/")  # Replace with MongoDB Atlas URI if needed
    return client["growbot_db"]
"""


def main():
    base_dir = os.getcwd()

    pretty_print_section("GROWBOT SETUP")
    print(Fore.CYAN + "Welcome to the GrowBot setup wizard. Let's get started!\n")

    # Create directory structure
    progress_bar("Setting up directories")
    create_directory_structure(base_dir)

    # Shared Logger
    progress_bar("Creating logger file")
    create_file(
        os.path.join(base_dir, "bots", "growbot_logger.py"),
        """\
import logging
import os

# Initialize logging
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/growbot.log",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger("GrowBotLogger")
"""
    )

    # MongoDB Connection
    progress_bar("Creating MongoDB connection file")
    create_file(
        os.path.join(base_dir, "bots", "mongodb.py"),
        setup_mongodb_connection()
    )

    # Install Dependencies
    progress_bar("Installing dependencies")
    install_dependencies()

    pretty_print_section("SETUP COMPLETE")
    print(Fore.GREEN + "🎉 GrowBot setup is complete!")
    print(Fore.CYAN + "You can now start the bots:\n")
    print(Fore.MAGENTA + "Customer bot: " + Fore.YELLOW + "python bots/customer_bot/customer_bot.py")
    print(Fore.MAGENTA + "Admin bot:    " + Fore.YELLOW + "python bots/admin_bot/admin_bot.py")
    print(Fore.GREEN + "\nHappy Growing with GrowBot! 🌱")


if __name__ == "__main__":
    main()
