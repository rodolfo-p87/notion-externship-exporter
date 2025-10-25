@echo off
REM Notion to GPT Exporter - Easy Launch Script
REM Double-click this file to run the export tool

echo ========================================
echo  NOTION TO GPT EXPORTER
echo ========================================
echo.

REM Check if virtual environment exists
if not exist "venv\Scripts\activate.bat" (
    echo Virtual environment not found. Running first-time setup...
    echo.
    echo Creating virtual environment...
    python -m venv venv

    echo Activating virtual environment...
    call venv\Scripts\activate.bat

    echo Installing dependencies...
    pip install -r requirements.txt
    echo.
    echo Setup complete!
    echo.
) else (
    echo Activating virtual environment...
    call venv\Scripts\activate.bat
)

REM Check if .env file exists
if not exist ".env" (
    echo.
    echo ========================================
    echo  WARNING: Configuration Missing
    echo ========================================
    echo.
    echo You need to create a .env file with your Notion API key.
    echo.
    echo Steps:
    echo   1. Copy .env.example to .env
    echo   2. Edit .env and add your NOTION_API_KEY
    echo   3. Run this script again
    echo.
    pause
    exit /b 1
)

echo.
echo Starting export tool...
echo.

REM Run the export tool
python src\main.py

echo.
echo ========================================
echo Press any key to close this window...
pause >nul
