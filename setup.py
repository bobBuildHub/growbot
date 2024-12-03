import os
import subprocess
import sys

# GitHub repository details
BRANCH_NAME = "main"  # Replace with the branch you are working on

# MongoDB config file path and content
MONGOD_CONFIG_PATH = r"C:\Program Files\MongoDB\Server\8.0\bin\mongod.cfg"  # Adjust as necessary
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
    print(f"Executing: {command}")
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        sys.exit(result.returncode)
    return result.stdout

# Function to force-update files on GitHub
def force_update_github():
    print("Adding, committing, and force-pushing changes to GitHub...")
    execute_command(["git", "add", "."])
    execute_command(["git", "commit", "-m", "Force update MongoDB configuration and other changes"])
    execute_command(["git", "push", "origin", BRANCH_NAME, "--force"])
    print("Changes have been successfully force-pushed to GitHub.")

# Function to update the MongoDB configuration file
def update_mongo_config():
    print(f"Updating MongoDB configuration at {MONGOD_CONFIG_PATH}...")
    try:
        # Temporarily write to a user-writable location
        temp_path = os.path.join(os.getcwd(), "mongod_temp.cfg")
        with open(temp_path, 'w') as f:
            f.write(CONFIG_CONTENT)
        print("Configuration written to temporary file.")

        # Copy the file to the final location using 'robocopy' for admin privilege bypass
        execute_command(["robocopy", os.getcwd(), os.path.dirname(MONGOD_CONFIG_PATH), "mongod_temp.cfg", "/NFL", "/NDL", "/NJH", "/NJS", "/nc", "/ns", "/np", "/MOV"])
        os.rename(os.path.join(os.path.dirname(MONGOD_CONFIG_PATH), "mongod_temp.cfg"), MONGOD_CONFIG_PATH)
        print(f"MongoDB configuration successfully updated at {MONGOD_CONFIG_PATH}.")
    except Exception as e:
        print(f"Error updating MongoDB config: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    try:
        # Update MongoDB configuration file
        update_mongo_config()

        # Force push changes to GitHub
        force_update_github()

        print("Script execution completed successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)
