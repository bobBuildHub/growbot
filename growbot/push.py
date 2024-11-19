import os
import subprocess

# Configuration
GITHUB_REPO_URL = "https://github.com/bobBuildHub/growbot.git"  # Repository URL
LOCAL_DIR = os.getcwd()  # Current project directory

def run_command(command):
    """Run a shell command and print output."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr.strip()}")
    else:
        print(result.stdout.strip())
    return result.returncode == 0

def initialize_git():
    """Initialize Git repository."""
    print("Initializing Git repository...")
    run_command("git init")
    run_command("git add .")
    run_command('git commit -m "Initial commit"')

def add_remote_and_push():
    """Add GitHub remote repository and push the code."""
    print("Adding remote and pushing to GitHub...")
    run_command(f"git remote add origin {GITHUB_REPO_URL}")
    run_command("git branch -M main")
    run_command("git push -u origin main")

def main():
    """Main script execution."""
    if not os.path.exists(".git"):
        initialize_git()
    else:
        print("Git repository already initialized.")
    
    # Set up the remote and push
    add_remote_and_push()
    print("Project successfully pushed to GitHub!")

if __name__ == "__main__":
    main()
