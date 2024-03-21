#app extensions
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
#from flask_jwt_extended import JWTManager

#create an instance
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
#jwt = JWTManager()