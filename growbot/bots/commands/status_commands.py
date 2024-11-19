"""
status_commands.py: Provides commands to fetch system status.
"""

from telegram import Update
from telegram.ext import ContextTypes
from utils.db_utils import DatabaseUtils

async def get_status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Fetch system status and respond to the user.
    """
    try:
        db = DatabaseUtils()
        statuses = db.fetch_all("status")
        if statuses:
            message = "🟢 **System Status:**\n\n"
            for status in statuses:
                message += f"🔹 {status['key']}: {status['value']}\n"
        else:
            message = "⚠️ No system status data available."
        await update.message.reply_text(message, parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text("⚠️ Error fetching system status.")
