from flask_restx import Api 
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_jwt_extended import JWTManager
from authlib.integrations.flask_client import OAuth


# database 
db = SQLAlchemy()
# login manager  
login_manager = LoginManager()
# token 
jwt = JWTManager()
# oauth
oauth = OAuth()

# rest api 
api = Api(
    title="Resume Optimizer API",
    version="1.0",
    description="API for the Resume Optimizer application and Cover letter generator",
    doc="/api/docs/", # Swagger UI documentation endpoint
)

