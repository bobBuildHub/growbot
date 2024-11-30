import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Initialize logging
logging.basicConfig(
    filename="logs/growbot.log",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)


class GrowBot:
    """
    A Telegram bot with buttons for UI/UX and appropriate action confirmations.
    """

    def __init__(self, token):
        self.token = token

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """
        Handle the /start command.
        """
        user = update.effective_user
        keyboard = [
            [
                InlineKeyboardButton("Start GrowBot", callback_data="start"),
                InlineKeyboardButton("Stop GrowBot", callback_data="stop"),
            ],
            [
                InlineKeyboardButton("Status", callback_data="status"),
                InlineKeyboardButton("Help", callback_data="help"),
            ],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text(
            f"Hi {user.first_name}, I am GrowBot! Use the buttons below to manage the bot:",
            reply_markup=reply_markup,
        )
        logger.info(f"User {user.id} started the bot.")

    async def button_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """
        Handle button interactions.
        """
        query = update.callback_query
        await query.answer()  # Acknowledge the button press

        if query.data == "start":
            logger.info("Start GrowBot action triggered.")
            await query.edit_message_text("✅ GrowBot has been started successfully!")
        elif query.data == "stop":
            logger.info("Stop GrowBot action triggered.")
            await query.edit_message_text("❌ GrowBot has been stopped.")
        elif query.data == "status":
            logger.info("Status action triggered.")
            await query.edit_message_text("ℹ️ GrowBot is currently running.")
        elif query.data == "help":
            logger.info("Help action triggered.")
            await query.edit_message_text(
                "ℹ️ *GrowBot Help Menu*\n"
                "1. Start GrowBot: Launch the GrowBot service.\n"
                "2. Stop GrowBot: Shut down the GrowBot service.\n"
                "3. Status: Check if GrowBot is running.\n"
                "4. Contact support for advanced issues.",
                parse_mode="Markdown",
            )
        else:
            logger.warning(f"Unknown action: {query.data}")
            await query.edit_message_text("⚠️ Unknown action. Please try again.")

    def run(self):
        """
        Start the Telegram bot application.
        """
        application = ApplicationBuilder().token(self.token).build()

        # Handlers
        application.add_handler(CommandHandler("start", self.start))
        application.add_handler(CallbackQueryHandler(self.button_handler))

        # Run the bot
        logger.info("GrowBot is starting...")
        application.run_polling()


if __name__ == "__main__":
    # Telegram bot token
    BOT_TOKEN = "7586067879:AAFtBcPcu8_eQYVmUqmpDltASX7TLZObwkI"

    # Create necessary directories
    import os
    os.makedirs("logs", exist_ok=True)

    try:
        growbot = GrowBot(BOT_TOKEN)
        growbot.run()
    except Exception as e:
        logger.critical(f"Critical error: {e}")
        print(f"Critical error: {e}")
