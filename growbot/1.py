import os

def create_directory(path):
    """
    Ensure a directory exists.
    """
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")

def create_file(file_path, content=""):
    """
    Create a file with optional content.
    """
    with open(file_path, "w") as f:
        f.write(content)
        print(f"Created file: {file_path}")

def setup_project():
    """
    Setup GrowBot project with required directories and files.
    """
    print("Setting up the GrowBot project...")

    # Directories
    create_directory("logs")
    create_directory("data")
    create_directory("db")
    create_directory("config")

    # Files
    create_file("config/token.env", "# Add your bot tokens here\n")
    create_file("db/growbot.json")
    create_file("data/notifications.json", "{}")
    create_file("logs/main.log")
    create_file("logs/customer_bot.log")
    create_file("logs/admin_bot.log")

    print("Setup complete.")

if __name__ == "__main__":
    setup_project()
