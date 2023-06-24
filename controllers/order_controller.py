from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from decorators import is_restaurant_admin
from requests.order_request import OrderRequest
from requests.order_status_request import OrderStatusRequest
from services.order_service import OrderService

order_bp = Blueprint('order_bp', __name__)


@order_bp.post('')
@jwt_required()
def store(service: OrderService):
    data = OrderRequest(**request.get_json()).dict()
    data['user_id'] = get_jwt_identity()
    resource = service.store(data)
    return jsonify(resource), 201


@order_bp.get('')
@jwt_required()
def index(service: OrderService):
    resources = service.find_orders(user_id=get_jwt_identity(), query=request.args)
    return jsonify(resources)


@order_bp.put('/<string:id>/status')
@jwt_required()
@is_restaurant_admin
def update(id, service: OrderService):
    data = OrderStatusRequest(**request.get_json()).dict()
    data['user_id'] = get_jwt_identity()
    resource = service.update_order_status(id, data)
    return jsonify(resource)


@order_bp.get('/<string:id>')
@jwt_required()
def find(id, service: OrderService):
    resources = service.find_order(id, get_jwt_identity())
    return jsonify(resources)
