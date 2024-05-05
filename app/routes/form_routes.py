"""
Module to define routes for car diagnostic form handling.

This module sets up a Flask Blueprint for handling routes related to a car
diagnostic tool. It includes routes for rendering the form and processing
form submissions.
"""

from flask import Blueprint, request, jsonify, render_template, Response
from app.utils.util import get_context
from typing import Tuple

form_bp = Blueprint("form_bp", __name__)


@form_bp.route("/")
def home() -> Response:
  return render_template("form.html")


@form_bp.route("/submit_diagnostic", methods=["POST"])
def submit_diagnostic() -> Tuple[Response, int]:
  """
  Handle the submission of the car diagnostic form.

  Returns:
    Response: A Flask JSON response containing the ChatGPT response Tuple[Response, int] and the
    submitted car diagnostic information.
  """
  make = request.form.get("make", "")
  model = request.form.get("model", "")
  year = request.form.get("year", "")
  car_issue = request.form.get("carIssue", "")

  if not all([make, model, year, car_issue]):
    return jsonify({"error": "Missing form data"}), 400

  llm_response = get_context(make, model, year, car_issue)

  print("llm_response", llm_response)

  return (
    jsonify(
      {
        "llm_response": llm_response,
        "diagnostic_info": {
          "make": make,
          "model": model,
          "year": year,
          "car_issue": car_issue,
        },
      }
    ),
    200,
  )
