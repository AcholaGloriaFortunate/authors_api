from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from authors_app.extension import db,migrate,bcrypt
from flask_bcrypt import Bcrypt
from authors_app.models.user import User
from authors_app.models.company import Company
from authors_app.models.book import Book
from authors_app.controllers.auth_controller import auth


# Application factory function
def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize extensions within the application factory
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    # Import and register models and blueprints
    
    app.register_blueprint(auth)

    return app

# Testing whether application works
app = create_app()

@app.route('/')
def home():
    return "Hello, world!"

    app.register_blueprint(auth, url_prefix='/api/v1/auth')
    app.register_blueprint(auth, url_prefix='/api/v1/books')
    app.register_blueprint(auth, url_prefix='/api/v1/companies')



if __name__ == "__main__":
    app.run()
    app.run(debug=True)






















# from flask import Flask

# from flask_sqlalchemy import SQLAlchemy

# from flask_migrate import Migrate

# from authors_app.extension import db

# from authors_app.extension import migrate,bcrypt

# from authors_app.models.user import User

# from authors_app.controllers.auth_controller import auth
# #from flask_script import Manager
# #from flask_migrate import MigrateCommand


# #application factory function
# def create_app():

#     #app instance
#     app = Flask(__name__)
#     app.config.from_object('config.Config')
#     #db = SQLAlchemy(app)
#     #migrate = Migrate(app, db)
#     #manager = Manager(app)
#     #manager.add_command('db', MigrateCommand)

# #for any third party library it must be initialised within the application factory function
#     db.init_app(app)
#     migrate.init_app(app,db)
#     bcrypt.init_app(app)

#  # importing and registering the models
#     from authors_app.models.user import User
#     from authors_app.models.company import Company
#     from authors_app.models.book import   Book 
#     from authors_app.extension import db
    
#     # Registering blueprints
#     app.register_blueprint(auth)
    
#     return app

# #testing whether application works
# app = create_app()

# @app.route('/')
# def home():
#         return "hello world"

# #return app










# from flask import Flask

# from flask_sqlalchemy import SQLAlchemy

# from flask_migrate import Migrate

# from authors_app.extension import db

# from authors_app.extension import migrate,bcrypt

# from authors_app.models.user import User

# # from authors_app.controllers.auth.auth_controller import auth

# from authors_app.controllers.users.auth_controller import auth
# #from flask_script import Manager
# #from flask_migrate import MigrateCommand
# #from authors_app.controller.auth import auth

# #application factory function
# def create_app():

#     #app instance
#     app = Flask(__name__)
#     app.config.from_object('config.Config')
#     #db = SQLAlchemy(app)
#     #migrate = Migrate(app, db)
#     #manager = Manager(app)
#     #manager.add_command('db', MigrateCommand)

# #for any third party library it must be initialised within the application factory function
#     db.init_app(app)
#     migrate.init_app(app,db)
#     bcrypt.init_app(app)

#  # importing and registering the models
#     from authors_app.models.user import User
#     from authors_app.models.company import Company
#     from authors_app.models.book import Book 
    



# #testing whether application works
# @app.route('/')
# def home():
#         return "hello world"

# #registering blueprint
# app.register_blueprint(auth)
# #return app

    
        
    



