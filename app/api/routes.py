# # from flask import Blueprint, jsonify
# from flask_restx import Namespace

# api_bp = Namespace('api', description='File parsing operations')

# # api_bp = Blueprint('api', __name__)

# @api_bp.route("/status")
# def status():
#     return ({"Status":"API is running"})


# app/api/routes.py
from flask_restx import Namespace, Resource

api_ns = Namespace("example", description="Example endpoints")

@api_ns.route("/status")
class StatusResource(Resource):
    def get(self):
        return {"status": "API is running!"}


