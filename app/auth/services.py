# # Auth email and password
# from app.models import User
# from app.extensions import db, login_manager, jwt
# from werkzeug.security import generate_password_hash, check_password_hash

# from flask import url_for, session
# # from .models import User
# from app.extensions import db, oauth
# from config import GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET
# # auth/services.py
# from flask_jwt_extended import create_access_token


# def register_user(email, password, name):
#     """Register a new user with the given email, password, and name."""
#     hashed_password = generate_password_hash(password, method='sha256')
#     new_user = User(email=email, password=hashed_password, name=name)
#     db.session.add(new_user)
#     db.session.commit()
#     return new_user

# def login_user(email, password):
#     """Authenticate a user with the given email and password."""
#     user = User.query.filter_by(email=email).first()
#     if user and check_password_hash(user.password, password):
#         return user
#     return None



# def configure_google_oauth(app):
#     oauth.register(
#         name="google",
#         client_id=app.GOOGLE_CLIENT_ID,
#         client_secret=app.GOOGLE_CLIENT_SECRET,
#         access_token_url="https://accounts.google.com/o/oauth2/token",
#         authorize_url="https://accounts.google.com/o/oauth2/auth",
#         api_base_url="https://www.googleapis.com/oauth2/v1/",
#         client_kwargs={"scope": "openid email profile"},
#     )


# def handle_google_auth(return_jwt=False):
#     google = oauth.create_client("google")
#     token = google.authorize_access_token()
#     user_info = google.get("userinfo").json()
    
#     user = User.query.filter_by(google_id=user_info["id"]).first()
#     if not user:
#         user = User(
#             email=user_info["email"],
#             name=user_info["name"],
#             google_id=user_info["id"],
#         )
#         db.session.add(user)
#         db.session.commit()
    
#     if return_jwt:  # For API
#         return create_access_token(identity=user.id)
#     return user  # For web


# def handle_google_auth():
#     google = oauth.create_client("google")
#     token = google.authorize_access_token()
#     user_info = google.get("userinfo").json()
    
#     user = User.query.filter_by(google_id=user_info["id"]).first()
#     if not user:
#         user = User(
#             email=user_info["email"],
#             name=user_info["name"],
#             google_id=user_info["id"],
#         )
#         db.session.add(user)
#         db.session.commit()
#     return user

