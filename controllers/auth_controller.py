from flask import Blueprint, request, jsonify

from requests.login_request import LoginRequest
from requests.register_request import RegisterRequest
from services.auth_service import AuthService

auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.post('/register')
def register(service: AuthService):
    data = RegisterRequest(**request.get_json())
    response = service.register(data)
    return jsonify(response)


@auth_bp.post('/login')
def login(service: AuthService):
    data = LoginRequest(**request.get_json())
    response = service.login(data)
    if response is None:
        return jsonify({'message': 'invalid credentials'}), 401
    return jsonify(response)
