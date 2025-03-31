from app.extensions import db 
from flask_login import UserMixin
from datetime import datetime

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200))
    name = db.Column(db.String(150))
    google_id = db.Column(db.String(100), unique=True)
    is_active = db.Column(db.Boolean, default=True)  # For Flask-Login
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.email}>'
    