from flask import Flask
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
from app.routes import chat_gpt_routes, form_routes

app.register_blueprint(chat_gpt_routes.chatgpt_bp)
app.register_blueprint(form_routes.form_bp)
