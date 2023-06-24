from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required

from decorators import is_super_admin
from requests.restaurant_registration_request import RestaurantRegistrationRequest, UpdateRestaurantRegistrationRequest
from services.restaurant_registration_service import RestaurantRegistrationService

restaurant_registration_bp = Blueprint('restaurant_registration_bp', __name__)


@restaurant_registration_bp.post('')
def store(service: RestaurantRegistrationService):
    data = RestaurantRegistrationRequest(**request.get_json())
    service.store(data.dict())
    return jsonify({'message': 'You details have been submitted. You will be notified upon approval'}), 201


@restaurant_registration_bp.get('')
@jwt_required()
@is_super_admin
def index(service: RestaurantRegistrationService):
    print(request.args)
    resources = service.find_all(query=request.args)
    return jsonify(resources)


@restaurant_registration_bp.put('/<string:id>')
@jwt_required()
@is_super_admin
def update(id, service: RestaurantRegistrationService):
    data = UpdateRestaurantRegistrationRequest(**request.get_json())
    resource = service.update(id, data.dict())
    return jsonify(resource)
