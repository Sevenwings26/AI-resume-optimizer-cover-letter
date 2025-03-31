from flask import Blueprint, render_template

web_bp = Blueprint("web", __name__)

@web_bp.route('/')
def index():
    # return "Welcome to the Resume Optimizer!"
    return render_template('index.html')
