import os
from typing import Optional


class TokenLoader:
    """
    TokenLoader is a utility class for loading and validating tokens from multiple sources.
    """

    def __init__(self, env_var: Optional[str] = None, file_path: Optional[str] = None):
        """
        Initialize the TokenLoader.

        :param env_var: Name of the environment variable to fetch the token from.
        :param file_path: Path to the file containing the token.
        """
        self.env_var = env_var
        self.file_path = file_path
        self.token = None  # Stores the loaded token

    def load_from_env(self) -> str:
        """
        Load the token from an environment variable.

        :return: The token value from the environment variable.
        :raises: EnvironmentError if the environment variable is not set.
        """
        if not self.env_var:
            raise ValueError("Environment variable name is not provided.")
        token = os.getenv(self.env_var)
        if not token:
            raise EnvironmentError(f"Environment variable '{self.env_var}' is not set.")
        return token.strip()

    def load_from_file(self) -> str:
        """
        Load the token from a file.

        :return: The token value from the file.
        :raises: FileNotFoundError if the file does not exist.
        :raises: ValueError if the file is empty or cannot be read.
        """
        if not self.file_path:
            raise ValueError("File path is not provided.")
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Token file '{self.file_path}' not found.")
        with open(self.file_path, "r") as file:
            token = file.read().strip()
        if not token:
            raise ValueError(f"Token file '{self.file_path}' is empty.")
        return token

    def validate_token(self, token: str, min_length: int = 10) -> bool:
        """
        Validate the format and length of the token.

        :param token: The token to validate.
        :param min_length: Minimum acceptable token length (default: 10).
        :return: True if the token is valid.
        :raises: ValueError if the token is invalid.
        """
        if len(token) < min_length:
            raise ValueError(f"Token must be at least {min_length} characters long.")
        if " " in token:
            raise ValueError("Token must not contain spaces.")
        return True

    def load_and_validate(self, source: str, min_length: int = 10) -> str:
        """
        Load the token from a specified source and validate it.

        :param source: 'env' to load from environment, 'file' to load from file.
        :param min_length: Minimum acceptable token length (default: 10).
        :return: The validated token.
        :raises: ValueError for invalid sources.
        """
        if source == "env":
            token = self.load_from_env()
        elif source == "file":
            token = self.load_from_file()
        else:
            raise ValueError("Invalid source. Use 'env' or 'file'.")
        self.validate_token(token, min_length)
        self.token = token
        return token


# Example usage for testing TokenLoader
if __name__ == "__main__":
    # Specify your environment variable name or file path
    ENV_VAR_NAME = "MY_TOKEN_ENV"
    FILE_PATH = r"C:\Users\drost\Desktop\GROW\growbot\complete_project_v2\bot\secret.env.txt"

    try:
        print("Loading token from environment variable...")
        loader = TokenLoader(env_var=ENV_VAR_NAME)
        token = loader.load_and_validate(source="env")
        print(f"Token loaded and validated from environment: {token}")
    except Exception as e:
        print(f"Error loading token from environment: {e}")

    try:
        print("\nLoading token from file...")
        loader = TokenLoader(file_path=FILE_PATH)
        token = loader.load_and_validate(source="file")
        print(f"Token loaded and validated from file: {token}")
    except Exception as e:
        print(f"Error loading token from file: {e}")
