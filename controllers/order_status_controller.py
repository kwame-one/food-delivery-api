from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required

from decorators import is_super_admin
from requests.menu_category_request import MenuCategoryRequest
from services.menu_category_service import MenuCategoryService
from services.order_status_service import OrderStatusService

order_status_bp = Blueprint('order_status_bp', __name__)


@order_status_bp.get('')
@jwt_required()
def index(service: OrderStatusService):
    resources = service.find_all(query=request.args)
    return jsonify(resources)

