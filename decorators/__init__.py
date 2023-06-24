from functools import wraps

from flask import jsonify, request
from flask_jwt_extended import decode_token

from repositories.user_repository import UserRepository


def is_super_admin(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        token = get_token()

        if token is None:
            return jsonify({'message': 'access denied'}), 403

        payload = decode_token(token)

        user_repo = UserRepository()
        user = user_repo.find(payload.get('sub'))
        print(user)
        if user.role.name != 'Super Admin':
            return jsonify({'message': 'access denied'}), 403
        return func(*args, **kwargs)

    return decorated_function


def is_restaurant_admin(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        token = get_token()

        if token is None:
            return jsonify({'message': 'access denied'}), 403

        payload = decode_token(token)

        user_repo = UserRepository()
        user = user_repo.find(payload.get('sub'))
        if user.role.name != 'Restaurant Admin':
            return jsonify({'message': 'access denied'}), 403
        return func(*args, **kwargs)

    return decorated_function


def get_token():
    header = request.headers.get('Authorization')
    token = header.split(' ')[1]
    return token
