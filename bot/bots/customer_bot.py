# customer_bot.py
import logging
from telegram.ext import ApplicationBuilder, CommandHandler

async def status(update, context):
    logging.info(f"Customer Bot /status command used by {update.effective_user.username}")
    await update.message.reply_text("Status: All systems are operational.")

async def preferences(update, context):
    logging.info(f"Customer Bot /preferences command used by {update.effective_user.username}")
    await update.message.reply_text("Here are your preferences.")

def create_customer_bot(token):
    """
    Creates and starts the Customer Bot.
    Args:
        token (str): The bot token for Customer Bot.
    """
    logging.info("🚀 Initializing Customer Bot...")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("preferences", preferences))
    app.run_polling()
