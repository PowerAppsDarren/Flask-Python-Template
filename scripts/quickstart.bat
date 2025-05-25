@echo off
echo Flask Python Template - Quick Start
echo ==================================
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    echo Virtual environment created.
    echo.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
echo.

REM Copy .env if it doesn't exist
if not exist ".env" (
    if exist ".env.example" (
        copy .env.example .env
        echo Environment file created from .env.example
    )
)

REM Launch VS Code if available
where /q code
if %ERRORLEVEL% EQU 0 (
    echo Launching VS Code...
    code .
    echo.
    echo VS Code launched. Press Ctrl+Shift+P and select "Python: Select Interpreter"
    echo Then choose the interpreter from venv\Scripts\python.exe
) else (
    echo VS Code not found in PATH
)

echo.
echo Setup complete! To run the app:
echo   1. Run: venv\Scripts\activate
echo   2. Run: python run.py
echo.
pause
