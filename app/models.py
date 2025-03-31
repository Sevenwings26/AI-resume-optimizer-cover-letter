from app.extensions import db
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(200))  # Store hashed password
    name = db.Column(db.String(150))
    google_id = db.Column(db.String(100), unique=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # def set_password(self, password):
    #     """Hash and set password"""
    #     self.password_hash = generate_password_hash(password)

    # def check_password(self, password):
    #     """Check hashed password"""
    #     return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.email}>'
