import os
import dotenv

def load_secrets(env_path="config/secret.env"):
    """
    Load secrets from the environment file.
    Args:
        env_path (str): Path to the environment file.
    Returns:
        dict: A dictionary with secrets.
    Raises:
        FileNotFoundError: If the environment file is missing.
        ValueError: If any required secrets are missing.
    """
    if not os.path.exists(env_path):
        raise FileNotFoundError(f"Environment file not found at: {env_path}")

    dotenv.load_dotenv(env_path)

    secrets = {
        "CUSTOMER_BOT_TOKEN": os.getenv("CUSTOMER_BOT_TOKEN"),
        "ADMIN_BOT_TOKEN": os.getenv("ADMIN_BOT_TOKEN"),
    }

    if not all(secrets.values()):
        raise ValueError("Some secrets are missing in the environment file.")
    
    return secrets
