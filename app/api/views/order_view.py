import http

from celery import group
from flask import Blueprint, jsonify

from app.api.views.cart_view import cart_decorator, scope_decorator
from app.core.settings import settings
from app.exceptions.exceptions import AccessDeniedException, OrderNotFoundException
from app.orm.repository import cart_repository, order_repository, order_item_repository, user_repository
from app.orm.schemas.request.cart.cart import CartSchemaWithItems
from app.orm.schemas.response.cart.cart import CartResponseSchema
from app.orm.schemas.response.order.order import OrderResponseSchemaWithItems
from app.worker.tasks.email import send_admin_email, send_user_email

order_blueprint = Blueprint('order_blueprint', __name__, url_prefix="/order")


@order_blueprint.route("", methods=['POST'], endpoint="create_order")
@cart_decorator
def create_order(cart_uid):
    cart = cart_repository.find_by_uid(cart_uid)
    cart_schema = CartSchemaWithItems.from_orm(cart)
    order = order_repository.create_order(cart_schema)
    order_item_repository.create_order_items(cart_schema.cart_items, order.id)
    cart_repository.delete(cart.id)
    user_email = user_repository.find(order.user_id).email
    group([send_admin_email.s(order.id, settings.admin_email), send_user_email.s(order.id, user_email)])()
    return CartResponseSchema.from_orm(order).json(), http.HTTPStatus.CREATED


@order_blueprint.route('')
@scope_decorator
def find_all(scope):
    if "get all orders" not in scope:
        raise AccessDeniedException
    orders = order_repository.find_all()
    return jsonify([OrderResponseSchemaWithItems.from_orm(order).dict() for order in orders]), http.HTTPStatus.OK


@order_blueprint.route('/<int:id>')
@scope_decorator
def show_order(scope, id: int):
    if "get order" not in scope:
        raise AccessDeniedException
    order = order_repository.find(id)
    if not order:
        raise OrderNotFoundException
    return jsonify(OrderResponseSchemaWithItems.from_orm(order).dict()), http.HTTPStatus.OK



@order_blueprint.route('/<int:id>', methods=['DELETE'])
@scope_decorator
def delete_order(scope, id: int):
    if "delete order" not in scope:
        raise AccessDeniedException
    order = order_repository.find(id)
    if not order:
        raise OrderNotFoundException
    order_repository.delete(id)
    return {}, http.HTTPStatus.NO_CONTENT
