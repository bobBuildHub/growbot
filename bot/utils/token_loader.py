import sys
import os
import logging
from telegram.ext import ApplicationBuilder, CommandHandler

# Add parent directory to the system path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.token_loader import load_bot_token
from commands.start import command as start_command
from commands.status import command as status_command
from commands.help import command as help_command

# Logging Configuration
logging.basicConfig(
    filename=os.path.join("logs", "customer_bot.log"),
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    """Main function to start the Customer Bot."""
    try:
        logging.info("Starting Customer Bot...")

        # Load bot token
        token = load_bot_token("customer")
        if not token:
            raise ValueError("Customer bot token is missing or invalid!")

        # Initialize the bot
        app = ApplicationBuilder().token(token).build()

        # Register commands
        app.add_handler(CommandHandler("start", start_command))
        app.add_handler(CommandHandler("status", status_command))
        app.add_handler(CommandHandler("help", help_command))

        # Start polling
        logging.info("Customer Bot is running...")
        app.run_polling()
    except Exception as e:
        logging.error(f"Error starting Customer Bot: {e}")
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
import os
import json

def load_bot_token(bot_type):
    """
    Loads the bot token from a JSON configuration file.
    Args:
        bot_type (str): 'customer' or 'admin'.
    Returns:
        str: Bot token.
    """
    config_path = os.path.join(os.path.dirname(__file__), "..", "config", "bot_config.json")

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    with open(config_path, "r", encoding="utf-8") as file:
        config = json.load(file)

    token_key = f"{bot_type}_bot_token"
    if token_key not in config or not config[token_key]:
        raise ValueError(f"Bot token for '{bot_type}' not found or invalid in configuration.")

    return config[token_key]
