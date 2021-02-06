from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from flask_jwt_extended import JWTManager

db = SQLAlchemy()


def create_app():
    from .views.pages import pages_blueprint

    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    CORS(app)
    jwt = JWTManager(app)

    app.config.from_object('config.Config')

    db.init_app(app)
    
    app.register_blueprint(pages_blueprint)

    with app.app_context():
        db.create_all()  # Create sql tables for our data models

        return app
