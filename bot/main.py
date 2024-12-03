import subprocess
import time
import sys

def start_flask_server():
    """Start the Flask Web Server."""
    print("Starting Flask Web Server...")
    flask_process = subprocess.Popen(['start', '/B', 'python', '-m', 'flask', 'run', '--host=0.0.0.0', '--port=5000'], shell=True)
    time.sleep(10)  # Wait for Flask to initialize
    return flask_process

def start_telegram_bot():
    """Start the Telegram Bot."""
    print("Starting Telegram Bot...")
    bot_process = subprocess.Popen(['start', '/B', 'python', 'C:\\Users\\drost\\Desktop\\GROW\\growbot\\complete_project_v2\\bot\\bots\\customer_bot.py'], shell=True)
    time.sleep(5)  # Wait for bot to initialize
    return bot_process

def check_flask_server():
    """Check if the Flask server is running by sending a request."""
    import requests
    try:
        response = requests.get('http://localhost:5000')
        if response.status_code == 200:
            print("Flask Web Server started successfully.")
        else:
            print("ERROR: Flask Web Server is not reachable.")
            sys.exit(1)
    except Exception as e:
        print(f"ERROR: Unable to reach Flask Web Server. {str(e)}")
        sys.exit(1)

def check_telegram_bot():
    """Check if the Telegram bot is running."""
    import requests
    bot_token = "7586067879:AAFtBcPcu8_eQYVmUqmpDltASX7TLZObwkI"
    try:
        response = requests.get(f"https://api.telegram.org/bot{bot_token}/getMe")
        if response.status_code == 200:
            print("Telegram Bot started successfully.")
        else:
            print("ERROR: Telegram Bot is not reachable.")
            sys.exit(1)
    except Exception as e:
        print(f"ERROR: Unable to connect to Telegram Bot. {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    # Start Flask server and Telegram bot
    flask_process = start_flask_server()
    bot_process = start_telegram_bot()

    # Check Flask server and bot
    check_flask_server()
    check_telegram_bot()

    print("Both Flask Web Server and Telegram Bot are running!")
    flask_process.wait()
    bot_process.wait()
