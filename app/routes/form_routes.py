"""Module to define routes for car diagnostic form handling.

This module sets up a Flask Blueprint for handling routes related to a car
diagnostic tool. It includes routes for rendering the form and processing
form submissions.
"""
from flask import Blueprint, request, jsonify, render_template, g
from app.utils.util import get_context

form_bp = Blueprint('form_bp', __name__)


@form_bp.route('/')
def home():
  """Render the home page with the car diagnostic form.

    Returns:
      A rendered template of 'form.html' for the home page.
      """
  return render_template('form.html')


@form_bp.route('/submit_diagnostic', methods=['POST'])
def submit_diagnostic():
  """Handle the submission of car diagnostic form.

    This function retrieves car details from the submitted form, stores them
    in Flask's global `g` object, and uses these details to get a diagnostic
    response from a ChatGPT service. It then returns this information in a
    JSON response.

    The form is expected to provide 'make', 'model', 'year', and 'car_issue'
    fields.

    Returns:
      A Flask JSON response containing the ChatGPT response and the submitted
      car diagnostic information.
  """
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
