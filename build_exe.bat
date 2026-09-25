@echo off
title Build Olives Chatbot Standalone EXE
cd /d "%~dp0"

echo =========================================================
echo       Building Olives Chatbot Standalone .EXE
echo =========================================================

:: 1. Check Python installation
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not found in PATH!
    echo Please install Python 3.11, 3.12, or 3.13 and add it to PATH.
    pause
    exit /b 1
)

:: 2. Install requirements & pyinstaller
echo [1/3] Installing/verifying build requirements...
pip install -r requirements.txt pyinstaller

:: 3. Run PyInstaller
echo [2/3] Bundling everything into dist\OlivesChatbot.exe...
pyinstaller --clean olives_chatbot.spec

if %errorlevel% neq 0 (
    echo [ERROR] Build failed! Check the output above.
    pause
    exit /b %errorlevel%
)

:: 4. Done
echo [3/3] Build succeeded!
echo.
echo =========================================================
echo Output file: dist\OlivesChatbot.exe
echo You can give OlivesChatbot.exe directly to your boss.
echo =========================================================
pause
