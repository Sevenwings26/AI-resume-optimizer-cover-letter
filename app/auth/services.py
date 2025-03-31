# Auth handling 
from app.models import User
from app.extensions import db, login_manager, jwt
from werkzeug.security import generate_password_hash, check_password_hash

def register_user(email, password, name):
    """Register a new user with the given email, password, and name."""
    hashed_password = generate_password_hash(password, method='sha256')
    new_user = User(email=email, password=hashed_password, name=name)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def login_user(email, password):
    """Authenticate a user with the given email and password."""
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        return user
    return None

