from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required

from decorators import is_super_admin
from requests.restaurant_request import RestaurantRequest
from services.restaurant_service import RestaurantService

restaurant_bp = Blueprint('restaurant_bp', __name__)


@restaurant_bp.post('')
@jwt_required()
@is_super_admin
def store(service: RestaurantService):
    data = RestaurantRequest(**request.get_json())
    resource = service.store(data.dict())
    return jsonify(resource), 201


@restaurant_bp.get('')
@jwt_required()
def index(service: RestaurantService):
    resources = service.find_all(query=request.args)
    return jsonify(resources)


@restaurant_bp.get('/<string:id>')
@jwt_required()
def find(id, service: RestaurantService):
    resource = service.find(id)
    return jsonify(resource)
