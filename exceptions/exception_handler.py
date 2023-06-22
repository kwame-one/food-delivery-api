from flask import jsonify
from pydantic import ValidationError


def bad_request_handler(e: ValidationError):
    errors = {error['loc'][0]: error['msg'] for error in e.errors()}
    return jsonify(errors), 400


def resource_not_found_handler(e):
    return jsonify({'message': e.description}), 404


def email_exists_handler(e):
    return jsonify({'message': 'Email has already taken'}), 400
