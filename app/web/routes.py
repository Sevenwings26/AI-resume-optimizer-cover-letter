from flask import Blueprint, request, render_template, redirect, url_for, flash

web_bp = Blueprint('web', __name__)

@web_bp.route("/")
def index():
    return render_template("index.html")


