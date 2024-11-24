# utils/token_loader.py
import os
import logging

def load_bot_tokens():
    """
    Loads bot tokens for Admin and Customer bots from environment variables or fallback to a configuration file.
    Returns:
        tuple: (admin_token, customer_token)
    Raises:
        ValueError: If tokens are missing or improperly formatted.
    """
    logging.info("🚀 Loading bot tokens...")

    # Step 1: Attempt to load tokens from environment variables
    admin_token = os.getenv("ADMIN_BOT_TOKEN")
    customer_token = os.getenv("CUSTOMER_BOT_TOKEN")
    logging.debug(f"Environment tokens loaded: Admin - {bool(admin_token)}, Customer - {bool(customer_token)}")

    # Step 2: Fallback to configuration file if tokens are missing
    if not admin_token or not customer_token:
        try:
            logging.info("🔄 Falling back to 'config/secret.env.txt'")
            with open("config/secret.env.txt", "r", encoding="utf-8") as file:
                lines = file.readlines()
                tokens = {
                    line.split('=')[0].strip(): line.split('=')[1].strip()
                    for line in lines if '=' in line
                }
                admin_token = tokens.get("ADMIN_BOT_TOKEN", admin_token)
                customer_token = tokens.get("CUSTOMER_BOT_TOKEN", customer_token)
                logging.debug(f"File tokens loaded: Admin - {bool(admin_token)}, Customer - {bool(customer_token)}")
        except FileNotFoundError:
            raise ValueError("❌ Token file 'secret.env.txt' not found!")
        except Exception as e:
            raise ValueError(f"❌ Error reading token file: {e}")

    # Step 3: Validate tokens
    if not admin_token:
        raise ValueError("❌ Admin Bot token is missing! Ensure it is set.")
    if not customer_token:
        raise ValueError("❌ Customer Bot token is missing! Ensure it is set.")

    logging.info("✅ Bot tokens loaded successfully!")
    return admin_token, customer_token

import os
import logging

def load_bot_tokens():
    logging.info("🚀 Loading bot tokens...")
    # Example token loading logic
    return "admin_token_example", "customer_token_example"
