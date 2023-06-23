from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required

from decorators import is_super_admin
from requests.menu_category_request import MenuCategoryRequest
from services.menu_category_service import MenuCategoryService

menu_category_bp = Blueprint('menu_category_bp', __name__)


@menu_category_bp.get('')
def index(service: MenuCategoryService):
    resources = service.find_all(query=request.args)
    return jsonify(resources)


@menu_category_bp.post('')
# @jwt_required()
# @is_super_admin
def store(service: MenuCategoryService):
    data = MenuCategoryRequest(**request.get_json())
    resource = service.store(data.dict())
    return jsonify(resource), 201


@menu_category_bp.put('/<string:id>')
@jwt_required()
@is_super_admin
def update(id, service: MenuCategoryService):
    data = MenuCategoryRequest(**request.get_json())
    resource = service.update(id, data.dict())
    return jsonify(resource)


@menu_category_bp.delete('/<string:id>')
@jwt_required()
@is_super_admin
def destroy(id, service: MenuCategoryService):
    service.delete(id)
    return jsonify({}), 204
