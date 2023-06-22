from flask import request, jsonify, Blueprint

from requests.restaurant_request import RestaurantRequest
from services.restaurant_service import RestaurantService

restaurant_bp = Blueprint('restaurant_bp', __name__)


@restaurant_bp.post('/')
def store(service: RestaurantService):
    data = RestaurantRequest(**request.get_json())
    resource = service.store(data.dict())
    return jsonify(resource), 201


@restaurant_bp.get('/')
def index(service: RestaurantService):
    resources = service.find_all(query=request.args)
    return jsonify(resources)
