import os
import shutil
import subprocess
import sys
import glob

def clear_unused_files():
    """Clear unnecessary files such as .pyc, .git directories, etc."""
    print("Clearing unused files...")

    # Remove .pyc files
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.pyc'):
                os.remove(os.path.join(root, file))
                print(f"Deleted: {file}")

    # Remove __pycache__ folders
    for root, dirs, files in os.walk('.'):
        for dir in dirs:
            if dir == '__pycache__':
                shutil.rmtree(os.path.join(root, dir))
                print(f"Deleted: {dir} (pycache)")

    # Remove .git directory (be careful with this one, only if you're sure)
    if os.path.isdir('.git'):
        shutil.rmtree('.git')
        print(".git directory deleted.")

    # Remove other temporary files if necessary
    temp_files = ['.DS_Store', '*.log']
    for temp_file in temp_files:
        for file in glob.glob(temp_file):
            os.remove(file)
            print(f"Deleted temporary file: {file}")

def install_dependencies():
    """Install the necessary Python dependencies."""
    print("Installing dependencies...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def run_linter():
    """Run code linter to check for style issues."""
    print("Running linter (flake8)...")
    subprocess.check_call(["flake8", "."])

def format_code():
    """Format the code using black."""
    print("Formatting code with black...")
    subprocess.check_call(["black", "."])

def run_tests():
    """Run the test suite."""
    print("Running tests (pytest)...")
    subprocess.check_call(["pytest", "--maxfail=1", "--disable-warnings", "-q"])

def check_for_outdated_dependencies():
    """Check for outdated dependencies."""
    print("Checking for outdated dependencies...")
    subprocess.check_call([sys.executable, "-m", "pip", "list", "--outdated"])

def clean_pip_cache():
    """Clean pip cache."""
    print("Cleaning pip cache...")
    subprocess.check_call([sys.executable, "-m", "pip", "cache", "purge"])

def create_virtualenv():
    """Create a virtual environment if it does not exist."""
    print("Creating virtual environment...")
    if not os.path.exists("venv"):
        subprocess.check_call([sys.executable, "-m", "venv", "venv"])
        print("Virtual environment created.")
    else:
        print("Virtual environment already exists.")

def update_requirements():
    """Update requirements.txt file."""
    print("Updating requirements.txt...")
    subprocess.check_call([sys.executable, "-m", "pip", "freeze"], stdout=open('requirements.txt', 'w'))
    print("requirements.txt updated.")

def main():
    """Run the necessary setup steps."""
    print("=======================================")
    print("Running setup...")
    print("=======================================")

    clear_unused_files()       # Clean up unnecessary files
    install_dependencies()     # Install dependencies
    run_linter()               # Lint the code
    format_code()              # Format the code with black
    run_tests()                # Run tests with pytest
    check_for_outdated_dependencies()  # Check for outdated dependencies
    clean_pip_cache()          # Clean pip cache
    create_virtualenv()        # Create virtual environment if needed
    update_requirements()      # Update the requirements.txt file

    print("\nSetup complete!")

if __name__ == '__main__':
    main()
