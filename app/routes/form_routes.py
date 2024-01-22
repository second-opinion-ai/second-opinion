from flask import Blueprint, render_template

form_bp = Blueprint('form_bp', __name__)

@form_bp.route('/')
def home():
    return render_template('form.html')
