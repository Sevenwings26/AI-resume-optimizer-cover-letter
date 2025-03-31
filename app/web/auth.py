from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User, db
from werkzeug.security import check_password_hash
from models import web_bp 


# web_bp = Blueprint('web', __name__)

@web_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        name = request.form.get('name')

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already exists!', 'danger')
            return redirect(url_for('web.signup'))

        new_user = User(email=email, name=name)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        flash('Account created successfully!', 'success')
        return redirect(url_for('web.login'))
    
    return render_template('signup.html')

@web_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('web.dashboard'))
        else:
            flash('Invalid credentials!', 'danger')

    return render_template('login.html')

@web_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out!', 'info')
    return redirect(url_for('web.login'))

from flask import redirect, url_for, session
from app.models import User
from app.extensions import db, oauth
import os
from config import GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET


google = oauth.register(
    name='google',
    client_id=GOOGLE_CLIENT_ID,
    client_secret=GOOGLE_CLIENT_SECRET,
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    client_kwargs={'scope': 'openid email profile'},
    api_base_url='https://www.googleapis.com/oauth2/v1/',
)

@web_bp.route('/login/google')
def login_google():
    return google.authorize_redirect(url_for('web.google_callback', _external=True))

@web_bp.route('/auth/google/callback')
def google_callback():
    token = google.authorize_access_token()
    user_info = google.get('userinfo').json()

    user = User.query.filter_by(email=user_info['email']).first()
    if not user:
        user = User(email=user_info['email'], name=user_info['name'], google_id=user_info['id'])
        db.session.add(user)
        db.session.commit()

    login_user(user)
    return redirect(url_for('web.dashboard'))


