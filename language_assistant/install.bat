@echo off
echo ==================================
echo Django Project Installation Script
echo ==================================

:: Check if virtual environment exists
if exist "venv" (
    echo Virtual environment found.
) else (
    echo Creating virtual environment...
    python -m venv venv
    if %errorlevel% neq 0 (
        echo Failed to create virtual environment.
        echo Please make sure Python is installed and in your PATH.
        pause
        exit /b 1
    )
    echo Virtual environment created successfully.
)

:: Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate
if %errorlevel% neq 0 (
    echo Failed to activate virtual environment.
    pause
    exit /b 1
)
echo Virtual environment activated.

:: Install requirements
if exist "requirements.txt" (
    echo Installing requirements from requirements.txt...
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo Failed to install requirements.
        pause
        exit /b 1
    )
    echo Requirements installed successfully.
) else (
    echo Warning: requirements.txt not found!
    echo Continuing without installing packages...
)

:: Change to directory language_assistant
echo Changing to directory language_assistant...
if exist "language_assistant" (
    cd language_assistant
    echo Changed to directory language_assistant.
) else (
    echo Warning: Directory language_assistant not found!
    echo Please ensure your project structure is correct.
    pause
    exit /b 1
)

:: Run migrations
echo Running migrations...
python manage.py migrate

if %errorlevel% neq 0 (
    echo Failed to run migrations.
    pause
    exit /b 1
)
echo Migrations completed successfully.

:: Open browser
echo Opening browser...
start http://localhost:8000/

:: Run the server
echo Starting Django development server...
python manage.py runserver
if %errorlevel% neq 0 (
    echo Failed to start the server.
    pause
    exit /b 1
)

:: This code should not be reached as runserver keeps running
echo Server has stopped.
pause