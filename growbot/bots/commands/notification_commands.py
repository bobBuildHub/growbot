"""
notification_commands.py: Commands to toggle notifications.
"""

from telegram import Update
from telegram.ext import ContextTypes
from modules.notifications import toggle_notifications

async def toggle_notifications_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Toggle notification settings for a user.
    """
    user_id = update.message.from_user.id
    status = toggle_notifications(user_id)
    message = "✅ Notifications enabled." if status else "❌ Notifications disabled."
    await update.message.reply_text(message)
