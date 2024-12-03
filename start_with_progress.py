@echo off
color 0a
cls

echo ========================================
echo Starting Flask Web Server and Telegram Bot
echo ========================================

:: Print some space for clarity
echo.

:: Set the Python environment (optional, if using virtualenv)
:: call "C:\path\to\your\virtualenv\Scripts\activate"

echo Checking for Python installation...
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in your PATH. Please install Python.
    pause
    exit /b
)

echo Python is installed. Continuing...
echo.

:: Starting Flask Web Server
echo ===============================
echo Starting Flask Web Server...
echo ===============================

:: Run Flask web server (in background)
start /B pythonw app.py
echo Flask web server is starting... Please wait a moment.
timeout /t 5 /nobreak

:: Check if Flask server is running on port 5000
echo Checking if Flask web server is running...
curl --silent --head http://localhost:5000 | findstr "200 OK" > nul
if %errorlevel% neq 0 (
    echo ERROR: Flask web server failed to start or is not reachable. Please check the logs.
    pause
    exit /b
)

echo Flask Web Server started successfully on http://localhost:5000.
echo.

:: Starting Telegram Bot
echo ==========================
echo Starting Telegram Bot...
echo ==========================

:: Run Telegram bot (in background)
start /B pythonw bot.py
echo Telegram bot is starting... Please wait a moment.
timeout /t 5 /nobreak

:: Check if Telegram bot is running by testing for connection (e.g., check if bot token is valid)
echo Checking if Telegram bot is running...
curl --silent --head "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getMe" | findstr "OK" > nul
if %errorlevel% neq 0 (
    echo ERROR: Telegram bot failed to start or cannot connect to Telegram API. Please check the bot token and logs.
    pause
    exit /b
)

echo Telegram Bot started successfully.
echo.

:: Final Success Message
echo ========================================
echo Both Flask Web Server and Telegram Bot are now running.
echo ========================================
echo Flask Web Server is accessible at: http://localhost:5000
echo Telegram Bot is connected and working with Telegram API.
echo ========================================
echo.

:: Give the user time to read the success messages
pause
