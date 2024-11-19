# growbot/bots/commands/log_commands.py
"""
Log commands for admin bot.
"""

import os

def view_logs(update, context):
    """
    Send recent logs to the admin.
    """
    log_file = "logs/system.log"
    if os.path.exists(log_file):
        with open(log_file, "r") as file:
            logs = file.readlines()[-10:]  # Get last 10 lines
            update.message.reply_text("".join(logs))
    else:
        update.message.reply_text("No logs found.")
