
import logging
from telegram.ext import ApplicationBuilder, CommandHandler

logging.basicConfig(level=logging.INFO)
TOKEN = os.getenv("CUSTOMER_BOT_TOKEN", "customer-token-placeholder")

async def start(update, context):
    await update.message.reply_text("Customer Bot is running!")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

if __name__ == "__main__":
    app.run_polling()
