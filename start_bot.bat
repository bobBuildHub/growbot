@echo off
color 06
cls
echo =======================================
echo Starting Telegram Bot
echo =======================================

:: Check if Python is installed
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in your PATH. Please install Python and ensure it is added to your PATH.
    pause
    exit /b
)

:: Start Telegram Bot
echo ================================
echo Starting Telegram Bot...
echo ================================
start /B python "C:\Users\drost\Desktop\GROW\growbot\complete_project_v2\bot\bots\customer_bot.py"

:: Wait for the bot to initialize
timeout /t 5 /nobreak

:: Check if Telegram Bot is running
echo Checking Telegram Bot...
curl --silent --head "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getMe" | findstr "OK" > nul
if %errorlevel% neq 0 (
    echo ERROR: Telegram bot failed to start or cannot connect to Telegram API.
    pause
    exit /b
)
echo Telegram Bot started successfully.
pause
