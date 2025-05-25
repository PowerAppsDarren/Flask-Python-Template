@echo off
echo Flask Python Template - Quick Start
echo ==================================
echo.

REM Check if venv exists
if exist venv (
    echo Virtual environment found.
    echo Activating virtual environment...
    call venv\Scripts\activate.bat
    echo.
    echo Running Flask application...
    python run.py
) else (
    echo No virtual environment found.
    echo Running setup script first...
    echo.
    python scripts\setup.py
    echo.
    echo Setup complete! Please run this script again or use:
    echo   venv\Scripts\activate
    echo   python run.py
)
