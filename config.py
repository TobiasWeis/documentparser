from os import environ, path

basedir = path.abspath(path.dirname(__file__))


class Config:
    """Set Flask configuration from .env file."""

    # General Config
    SECRET_KEY = environ.get('JWT_SECRET_KEY', 'CHANGEME')
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')
    UPLOAD_FOLDER = "/tmp/"

    # Database
    SQLALCHEMY_DATABASE_URI = "sqlite:///mlsys.db" # environ.get("DATABASE_URI")
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    INTERFACE_SERVER_URI = environ.get('IFSURI', 'http://localhost:5001/task/')
