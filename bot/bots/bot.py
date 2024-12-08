import os
import requests
from flask import Flask, request, jsonify
from utils import connect_to_mongo

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
BASE_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/"

def send_message(chat_id, text):
    """Send a message via Telegram."""
    url = BASE_URL + "sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

@app.route('/telegram-webhook', methods=['POST'])
def telegram_webhook():
    """Handle Telegram bot updates."""
    data = request.json
    message = data.get("message", {})
    chat_id = message.get("chat", {}).get("id")
    text = message.get("text")

    if text == "/start":
        send_message(chat_id, "Welcome to the bot!")
    else:
        send_message(chat_id, f"You said: {text}")

    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
