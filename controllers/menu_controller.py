from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required

from decorators import is_restaurant_admin
from requests.menu_request import MenuRequest
from services.menu_service import MenuService

menu_bp = Blueprint('menu_bp', __name__)


@menu_bp.post('')
@jwt_required()
@is_restaurant_admin
def store(service: MenuService):
    data = MenuRequest(**request.get_json()).dict()
    data['user_id'] = get_jwt_identity()
    resource = service.store(data)
    return jsonify(resource), 201


@menu_bp.put('/<string:id>')
@jwt_required()
@is_restaurant_admin
def update(id, service: MenuService):
    data = MenuRequest(**request.get_json()).dict()
    data['user_id'] = get_jwt_identity()
    resource = service.update(id, data)
    return jsonify(resource)


@menu_bp.get('')
@jwt_required()
def index(service: MenuService):
    resources = service.find_all_menus(user_id=get_jwt_identity(), query=request.args)
    return jsonify(resources)


@menu_bp.get('/<string:id>')
@jwt_required()
@is_restaurant_admin
def destroy(id, service: MenuService):
    service.delete_menu(id, get_jwt_identity())
    return jsonify({}), 204
