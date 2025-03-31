from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask_restx import Namespace, Resource
from app.models import User, db

# Create API namespace
api_ns = Namespace("api", description="RESTful API operations")

# Signup Resource
@api_ns.route('/signup')
class SignupResource(Resource):
    def post(self):
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        name = data.get('name')

        if User.query.filter_by(email=email).first():
            return {"message": "Email already exists"}, 400

        new_user = User(email=email, name=name)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        return {"message": "User created successfully"}, 201

# Login Resource
@api_ns.route('/login')
class LoginResource(Resource):
    def post(self):
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            access_token = create_access_token(identity=user.id)
            return {"access_token": access_token}, 200
        return {"message": "Invalid credentials"}, 401

# Protected Resource
@api_ns.route('/protected')
class ProtectedResource(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        return {"email": user.email, "name": user.name}, 200

# API Status Resource
@api_ns.route("/status")
class StatusResource(Resource):
    def get(self):
        return {"status": "API is running!"}
