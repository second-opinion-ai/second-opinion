from flask import Blueprint, request, jsonify, render_template, g
from app.utils.util import get_context

form_bp = Blueprint('form_bp', __name__)


@form_bp.route('/')
def home():
    return render_template('form.html')


@form_bp.route('/submit_diagnostic', methods=['POST'])
def submit_diagnostic():
    make = request.form.get('make')
    model = request.form.get('model')
    year = request.form.get('year')
    car_issue = request.form.get('carIssue')

    chat_gpt_response = get_context(make, model, year, car_issue)

    return jsonify({
        'chat_gpt_response': chat_gpt_response,
        'diagnostic_info': {
            'make': make,
            'model': model,
            'year': year,
            'car_issue': car_issue
        }
    })
