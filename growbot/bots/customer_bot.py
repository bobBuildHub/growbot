from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext
from rich.console import Console

console = Console()

def start_handler(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! Customer Bot is working.")
    console.print("[green]Customer Bot responded to a message.[/green]")

def start_customer_bot(token):
    if not token:
        console.print("[bold red]Customer bot token is missing![/bold red]")
        return

    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start_handler))  # Add a basic command

    console.print(":robot: [cyan]Customer Bot is online and polling...[/cyan]")
    app.run_polling()
