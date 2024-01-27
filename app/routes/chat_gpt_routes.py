"""Module to define routes for interacting with the ChatGPT service.

This module sets up a Flask Blueprint for routing related to ChatGPT operations.
It includes routes to handle API requests to interact with the ChatGPT service.
"""

from typing import Optional, Dict, Any, Tuple

from flask import Blueprint, request, jsonify, Response
from app.services import chat_gpt_service

chatgpt_bp = Blueprint("chatgpt_routes", __name__)


@chatgpt_bp.route("/api/chat_gpt/prompt/", methods=["POST"])
def prompt_chat_gpt() -> Tuple[Response, int]:
    """
    Handle POST requests to prompt the ChatGPT service.

    This route function extracts message content and model information
    from the incoming JSON request, prompts the ChatGPT service, and
    returns the generated response as JSON.

    The function expects a JSON payload with 'message_content' and
    optionally 'model' keys.

    Returns:
        Response: A Flask JSON response containing the ChatGPT response.
    """
    data: Optional[Dict[str, Any]] = request.json
    if data is None:
        return jsonify({"error": "Invalid or missing JSON payload"}), 400

    message_content: Optional[str] = data.get("message_content")
    model: str = data.get("model", "gpt-3.5-turbo")

    if message_content is None:
        return jsonify({"error": "Missing field: message_content"}), 400

    response = chat_gpt_service.prompt_chat_gpt(message_content, model)
    return jsonify(response), 200
