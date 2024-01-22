from flask import Blueprint, request, render_template, g
from app.services.chat_gpt_service import prompt_chat_gpt
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

    g.make = request.form.get('make')
    g.model = request.form.get('model')
    g.year = request.form.get('year')
    g.car_issue = request.form.get('carIssue')

    # message_content = f"Car Make: {make}, Model: {model}, Year: {year}, Issue: {car_issue}"

    # response = prompt_chat_gpt(message_content)

    chat_gpt_response = get_context()

    return render_template('diagnostic_submitted.html', chat_gpt_response=chat_gpt_response, diagnostic_info={
        'make': make,
        'model': model,
        'year': year,
        'car_issue': car_issue
    })
