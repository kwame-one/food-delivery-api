from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from requests.order_request import OrderRequest
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


@order_bp.get('/<string:id>')
@jwt_required()
def find(id, service: OrderService):
    resources = service.find(id)
    return jsonify(resources)
