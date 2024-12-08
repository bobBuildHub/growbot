import os
import subprocess
import sys

# GitHub repository details
REPO_PATH = os.getcwd()  # Assuming this script runs from the root of your local repository
BRANCH_NAME = "main"  # Update if you are working with a different branch

# MongoDB configuration file details
MONGOD_CONFIG_PATH = r"C:\Users\drost\Desktop\GROW\growbot\complete_project_v2\mongod.cfg"  # Adjust as needed
CONFIG_CONTENT = """
storage:
  dbPath: C:\\data\\db
  journal:
    enabled: true

systemLog:
  destination: file
  path: C:\\Program Files\\MongoDB\\Server\\8.0\\log\\mongod.log
  logAppend: true
  verbosity: 1

net:
  bindIp: 127.0.0.1
  port: 27017

operationProfiling:
  mode: slowOp
  slowOpThresholdMs: 100
"""

# Function to execute shell commands
def execute_command(command):
    print(f"Executing: {' '.join(command)}")
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        sys.exit(result.returncode)
    return result.stdout

# Function to update the MongoDB config file
def update_mongo_config():
    print(f"Updating MongoDB config file at {MONGOD_CONFIG_PATH}...")
    try:
        with open(MONGOD_CONFIG_PATH, 'w') as f:
            f.write(CONFIG_CONTENT)
        print("MongoDB configuration updated successfully.")
    except Exception as e:
        print(f"Error updating MongoDB config: {e}")
        sys.exit(1)

# Function to commit and push changes to GitHub
def commit_and_push_changes():
    print("Committing and pushing changes to GitHub...")
    try:
        # Navigate to the repo path
        os.chdir(REPO_PATH)
        print(f"Working directory: {os.getcwd()}")

        # Add changes
        execute_command(["git", "add", "."])

        # Commit changes
        execute_command(["git", "commit", "-m", "Updated MongoDB configuration and other local changes"])

        # Push changes to the specified branch
        execute_command(["git", "push", "origin", BRANCH_NAME])

        print("Changes pushed to GitHub successfully.")
    except Exception as e:
        print(f"Error during Git operations: {e}")
        sys.exit(1)

# Main script execution
if __name__ == "__main__":
    try:
        # Update MongoDB config
        update_mongo_config()

        # Commit and push changes
        commit_and_push_changes()

        print("Local changes have been successfully pushed to GitHub.")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
