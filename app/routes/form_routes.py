from flask import Blueprint, request, jsonify, render_template, g
from app.utils.util import get_context

form_bp = Blueprint('form_bp', __name__)

@form_bp.route('/')
def home():
    return render_template('form.html')

@form_bp.route('/submit_diagnostic', methods=['POST'])
def submit_diagnostic():
    g.make = request.form.get('make')
    g.model = request.form.get('model')
    g.year = request.form.get('year')
    g.car_issue = request.form.get('carIssue')

    chat_gpt_response = get_context()

    return jsonify({
        'chat_gpt_response': chat_gpt_response,
        'diagnostic_info': {
            'make': g.make,
            'model': g.model,
            'year': g.year,
            'car_issue': g.car_issue
        }
    })
