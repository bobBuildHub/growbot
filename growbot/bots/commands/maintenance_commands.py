"""
notification_commands.py: Handles notification toggling.
"""

from telegram import Update
from telegram.ext import ContextTypes
from modules.notifications import Notifications

notifications = Notifications()

async def toggle_notifications(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Toggle user notifications on/off.
    """
    try:
        chat_id = update.message.chat_id
        status = notifications.toggle(chat_id)
        message = "🔔 Notifications enabled." if status else "🔕 Notifications disabled."
        await update.message.reply_text(message)
    except Exception as e:
        await update.message.reply_text("⚠️ Error toggling notifications.")
