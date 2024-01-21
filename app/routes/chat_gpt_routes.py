from flask import Blueprint, request, jsonify
from app import app
from app.services import chat_gpt_service

chatgpt_bp = Blueprint('chatgpt_routes', __name__)

@chatgpt_bp.route('/api/chat_gpt/prompt/', methods=['POST'])
def prompt_chat_gpt():
    data = request.json
    message_content = data.get('message_content')
    model = data.get('model', 'gpt-3.5-turbo')

    response = chat_gpt_service.prompt_chat_gpt(message_content, model)
    return jsonify(response)
