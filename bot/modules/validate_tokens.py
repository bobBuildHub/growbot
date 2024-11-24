def validate_token(token):
    """
    Validate a Telegram bot token.
    Args:
        token (str): The bot token to validate.
    Returns:
        bool: True if valid, otherwise False.
    """
    return isinstance(token, str) and len(token.split(":")) == 2
