# app/routes.py

from flask import Blueprint, jsonify
from app.services.common_service import get_hello_message

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/api/hello', methods=['GET'])
def hello():
    response = get_hello_message()
    return jsonify(response);

@api_blueprint.route('/api/liveness', methods = ['GET'])
def liveness():
    return jsonify({'status': 'ok'})