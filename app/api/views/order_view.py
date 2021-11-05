import http

from flask import Blueprint, jsonify

from app.api.views.cart_view import cart_decorator
from app.orm.repository import cart_repository, order_repository, order_item_repository
from app.orm.schemas.request.cart.cart import CartSchemaWithItems
from app.orm.schemas.response.cart.cart import CartResponseSchema
from app.orm.schemas.response.order.order import OrderResponseSchemaWithItems

order_blueprint = Blueprint('order_blueprint', __name__, url_prefix="/order")


@order_blueprint.route("", methods=['POST'], endpoint="create_order")
@cart_decorator
def create_order(cart_uid):
    cart = cart_repository.find_by_uid(cart_uid)
    cart_schema = CartSchemaWithItems.from_orm(cart)
    order = order_repository.create_order(cart_schema)
    cart_items = cart_schema.cart_items
    [order_item_repository.create_order_items(cart_item, order.id) for cart_item in cart_items]
    cart_repository.delete(cart.id)
    return CartResponseSchema.from_orm(order).json(), http.HTTPStatus.CREATED


@order_blueprint.route('')
def find_all():
    orders = order_repository.find_all()
    return jsonify([OrderResponseSchemaWithItems.from_orm(order).dict() for order in orders]), http.HTTPStatus.OK


@order_blueprint.route('/<int:id>')
def show_order(id: int):
    order = order_repository.find(id)
    return jsonify(OrderResponseSchemaWithItems.from_orm(order).dict()), http.HTTPStatus.OK


@order_blueprint.route('/<int:id>', methods=['DELETE'])
def delete_order(id: int):
    order_repository.delete(id)
    return {}, http.HTTPStatus.NO_CONTENT
