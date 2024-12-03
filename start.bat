@echo off
cls
echo =======================================
echo Starting Flask Web Server and Telegram Bot
echo =======================================
echo.

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python.
    pause
    exit /b
)

echo Python is installed. Continuing...
echo =======================================
echo Checking if Flask is installed...
python -m pip show flask >nul 2>&1
if %errorlevel% neq 0 (
    echo Flask is not installed. Installing now...
    python -m pip install flask
)

echo Flask is already installed.
echo ===================================
echo Starting Flask Web Server...
echo ===================================

:: Ensure you're in the correct directory
cd /d "%~dp0"  :: Changes to the directory of the .bat file

:: Set Flask environment variable
set FLASK_APP=web.app

:: Check if Flask app can be imported
python -c "from web.app import app; print('Flask App Loaded Successfully!')"

:: Start Flask Web Server
start /B python -m flask run

:: Check if Flask Web Server is running
timeout /t 5 /nobreak >nul
echo Waiting for Flask to initialize...

:: Here you can add a check for the server to ensure it's running
curl http://127.0.0.1:5000 >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Flask web server failed to start or is not reachable.
    pause
    exit /b
)

echo Flask Web Server started successfully.
echo ========================================
echo Flask Web Server is running at http://localhost:5000
echo ========================================
pause
