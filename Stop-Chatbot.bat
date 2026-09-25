@echo off
title Stop Olives Chatbot
cd /d "%~dp0"

echo Stopping Olives Chatbot containers...
if exist docker-compose.demo.yml (
    docker compose -f docker-compose.demo.yml down
) else (
    docker compose down
)
echo Chatbot stopped.
timeout /t 2 >nul
