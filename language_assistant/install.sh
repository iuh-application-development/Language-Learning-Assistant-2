#!/bin/bash

echo "=================================="
echo "Django Project Installation Script"
echo "=================================="

# Check if virtual environment exists
if [ -d "venv" ]; then
    echo "Virtual environment found."
else
    echo "Creating virtual environment..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "Failed to create virtual environment."
        echo "Please make sure Python 3 is installed and in your PATH."
        exit 1
    fi
    echo "Virtual environment created successfully."
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo "Failed to activate virtual environment."
    exit 1
fi
echo "Virtual environment activated."

# Install requirements
if [ -f "requirements.txt" ]; then
    echo "Installing requirements from requirements.txt..."
    pip install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "Failed to install requirements."
        exit 1
    fi
    echo "Requirements installed successfully."
else
    echo "Warning: requirements.txt not found!"
    echo "Continuing without installing packages..."
fi

# Change to directory language_assistant
echo "Changing to directory language_assistant..."
if [ -d "language_assistant" ]; then
    cd language_assistant
    echo "Changed to directory language_assistant."
else
    echo "Warning: Directory language_assistant not found!"
    echo "Please ensure your project structure is correct."
    exit 1
fi

# Run migrations
echo "Running migrations..."
python manage.py migrate
if [ $? -ne 0 ]; then
    echo "Failed to run migrations."
    exit 1
fi
echo "Migrations completed successfully."

# Open browser
echo "Opening browser..."
open http://localhost:8000/

# Run the server
echo "Starting Django development server..."
python manage.py runserver
if [ $? -ne 0 ]; then
    echo "Failed to start the server."
    exit 1
fi

# This line typically won't be reached because the server runs continuously
echo "Server has stopped."
