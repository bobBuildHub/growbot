"""
hardware_commands.py: Commands to control ESP32 hardware.
"""

from telegram import Update
from telegram.ext import ContextTypes
from modules.esp32 import ESP32

esp32 = ESP32()

async def get_hardware_status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Fetch ESP32 hardware status.
    """
    status = esp32.check_status()
    if status.get("status") == "online":
        message = f"🔧 **ESP32 Status:**\nIP: {esp32.ip}\nStatus: Online"
    else:
        message = "⚠️ ESP32 is offline or unreachable."
    await update.message.reply_text(message, parse_mode="Markdown")

async def control_hardware(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Send a command to control ESP32.
    """
    command = " ".join(context.args)
    if not command:
        await update.message.reply_text("⚠️ Please specify a command to send to ESP32.")
        return

    result = esp32.send_command(command)
    if result.get("status") == "success":
        await update.message.reply_text(f"✅ Command executed: {command}")
    else:
        await update.message.reply_text(f"⚠️ Failed to execute command: {command}")
