from flask import Flask, g
from flask_cors import CORS
import os

app = Flask(__name__)
app.config['OPENAI_API_KEY'] = os.environ.get('OPENAI_API_KEY')
CORS(app)
from app.routes import chat_gpt_routes, form_routes

app.register_blueprint(chat_gpt_routes.chatgpt_bp)
app.register_blueprint(form_routes.form_bp)

