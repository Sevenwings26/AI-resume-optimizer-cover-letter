from flask import Flask 
from .extensions import *
from app.web.routes import web_bp
from app.api.routes import api_ns
from config import SQLALCHEMY_TRACK_MODIFICATIONS, SQLALCHEMY_DATABASE_URI

from app.models import User

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  # Ensure it returns a user object or None

def create_app():
    app = Flask(__name__)

    # load_user(user_id)

    # set up configuration 
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    jwt.init_app(app)
    oauth.init_app(app)

    # Register web blueprint
    app.register_blueprint(web_bp, url_prefix="/")

    # Initialize and register API
    api.init_app(app)
    api.add_namespace(api_ns)  # Correct way for Flask-RESTX
    # app.register_blueprint(api_ns, url_prefix="/")

    return app
