#!/bin/bash
# Start script for Render deployment

echo "Starting DRM Uploader Bot on Render..."

# Install additional system dependencies if needed
echo "Installing system dependencies..."

# Start Flask app in background
echo "Starting Flask web server on port 5000..."
gunicorn --bind 0.0.0.0:5000 --workers 1 --timeout 120 app:app &

# Wait a moment for Flask to start
sleep 5

# Start the main bot
echo "Starting Telegram bot..."
python3 main.py
