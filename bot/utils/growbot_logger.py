import logging
from colorama import Fore, Style, init

init(autoreset=True)  # Initialize Colorama for colored output

class Logger:
    """
    Centralized logger for GrowBot, providing pretty, combined output to console and file.
    """

    def __init__(self, log_file="growbot.log"):
        """
        Initialize the logger with file and console handlers.
        """
        self.logger = logging.getLogger("GrowBot")
        self.logger.setLevel(logging.INFO)

        # Formatter for readable logs
        formatter = logging.Formatter(
            fmt="%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )

        # File Handler: Logs to a file
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.INFO)

        # Console Handler: Pretty output to the console
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        console_handler.setLevel(logging.INFO)

        # Add handlers to logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def info(self, message):
        """Log an info message."""
        self.logger.info(Fore.GREEN + message)

    def warning(self, message):
        """Log a warning message."""
        self.logger.warning(Fore.YELLOW + message)

    def error(self, message):
        """Log an error message."""
        self.logger.error(Fore.RED + message)

    def critical(self, message):
        """Log a critical error."""
        self.logger.critical(Fore.MAGENTA + message)

# Example usage
if __name__ == "__main__":
    log = Logger()
    log.info("This is an informational message.")
    log.warning("This is a warning message.")
    log.error("This is an error message.")
    log.critical("This is a critical message.")
