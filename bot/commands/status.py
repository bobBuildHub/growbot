def command(update, context):
    """Handles the /status command."""
    update.message.reply_text("Fetching system status...")
    # Simulate fetching data
    status_message = "Temperature: 25°C\nHumidity: 60%\nAll systems operational."
    update.message.reply_text(status_message)
