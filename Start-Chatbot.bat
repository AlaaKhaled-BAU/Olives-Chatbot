@echo off
title Olives Chatbot Launcher
cd /d "%~dp0"

echo =========================================================
echo              Starting Olives Chatbot...
echo =========================================================

:: 1. Check if Docker is running
docker info >nul 2>&1
if %errorlevel% neq 0 (
    echo [INFO] Docker not running. Starting chatbot natively with Python...
    python desktop_app.py
    if %errorlevel% neq 0 pause
    exit /b 0
)

:: 2. Check and load images if needed
docker image inspect olives-chatbot:latest >nul 2>&1
if %errorlevel% neq 0 (
    echo [INFO] Loading chatbot images (first-time only, please wait)...
    if exist docker\out\olives-chatbot.tar (
        docker load -i docker\out\olives-chatbot.tar
    ) else if exist olives-chatbot.tar (
        docker load -i olives-chatbot.tar
    )
    if exist docker\out\olives-mssql-demo.tar (
        docker load -i docker\out\olives-mssql-demo.tar
    ) else if exist olives-mssql-demo.tar (
        docker load -i olives-mssql-demo.tar
    )
)

:: 3. Start demo containers
if exist docker-compose.demo.yml (
    docker compose -f docker-compose.demo.yml up -d
) else (
    docker compose up -d
)

:: 4. Launch browser
echo [INFO] Waiting for service to initialize...
timeout /t 3 /nobreak >nul
start http://localhost:8100

echo.
echo =========================================================
echo Chatbot is active at: http://localhost:8100
echo To stop the bot, double-click Stop-Chatbot.bat
echo =========================================================
pause
