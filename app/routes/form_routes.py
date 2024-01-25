"""Module to define routes for car diagnostic form handling.

This module sets up a Flask Blueprint for handling routes related to a car
diagnostic tool. It includes routes for rendering the form and processing
form submissions.
"""
from flask import Blueprint, request, jsonify
from app.utils.util import get_context

form_bp = Blueprint('form_bp', __name__)

@form_bp.route('/submit_diagnostic', methods=['POST'])
def submit_diagnostic():
  """
  Handle the submission of the car diagnostic form.

  This function directly retrieves car details ('make', 'model', 'year', and
  'car_issue') from the submitted form data. It then uses these details to get
  a diagnostic response from the ChatGPT service. The diagnostic response,
  along with the submitted car details, are then returned in a JSON format.

  The form is expected to provide 'make', 'model', 'year', and 'car_issue'
  fields.

  Returns:
    dict: A Flask JSON response containing the ChatGPT response and the
    submitted car diagnostic information.
  """
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
