#!/bin/bash

# Navigate to the project root directory
cd "$(dirname "$0")"

# Set up the environment variables
export FLASK_APP=run.py
export FLASK_ENV=development  # Optional: Enables debug mode
export FLASK_RUN_PORT=5000

# Run the Flask app
flask --app run.py --debug run