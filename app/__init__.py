"""Initialization module for the Flask application.

This module sets up the Flask application instance and its configuration.
It includes the necessary imports and configurations for the application
to function correctly. The module initializes the Flask app, sets up CORS
(Cross-Origin Resource Sharing) policies, and registers various blueprints
that define the routes and logic of the application.

The application is configured to interact with the OpenAI API, with the
API key being loaded from the environment variables. It includes blueprints
for handling ChatGPT interactions and form submissions related to car
diagnostics.

Attributes:
    app (Flask): The Flask application instance.
"""

from flask import Flask
from flask_cors import CORS
import os

app = Flask(__name__)
app.config["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY")
CORS(app)

# Importing and registering blueprints after Flask app creation
# to avoid circular imports.
from app.routes import chat_gpt_routes, form_routes

app.register_blueprint(chat_gpt_routes.chatgpt_bp)
app.register_blueprint(form_routes.form_bp)
