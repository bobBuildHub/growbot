# admin_bot.py
import logging
from telegram.ext import ApplicationBuilder, CommandHandler

async def start(update, context):
    logging.info(f"Admin Bot /start command used by {update.effective_user.username}")
    await update.message.reply_text("Welcome to the Admin Bot! Type /help for available commands.")

async def help_command(update, context):
    logging.info(f"Admin Bot /help command used by {update.effective_user.username}")
    await update.message.reply_text("Available commands:\n/start\n/help")

def create_admin_bot(token):
    """
    Creates and starts the Admin Bot.
    Args:
        token (str): The bot token for Admin Bot.
    """
    logging.info("🚀 Initializing Admin Bot...")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.run_polling()
