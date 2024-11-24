def command(update, context):
    """Handles the /help command."""
    update.message.reply_text("Available commands:\n/start - Start the bot\n/status - Get system status\n/help - List available commands.")
