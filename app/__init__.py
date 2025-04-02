# app/__init__.py

from flask import Flask
from app.routes import api_blueprint
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Register Blueprints
    app.register_blueprint(api_blueprint)
    
    return app