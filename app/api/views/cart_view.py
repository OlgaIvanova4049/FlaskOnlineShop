import functools
import http

from flask import Blueprint, request, jsonify
from jose import jwt

from app.core.settings import settings
from app.orm.repository import cart_repository
from app.orm.schemas.request.cart.cart import CartUIDSchema
from app.orm.schemas.request.product.product import ProductCartSchema
from app.orm.schemas.response.cart.cart import CartResponseSchema
from app.orm.schemas.response.cart.cart_item import CartItemResponseSchema

cart_blueprint = Blueprint('cart_blueprint', __name__, url_prefix="/cart")


def cart_decorator(f):
    """Get cart_uid from JWT"""

    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        auth_token = auth_header.removeprefix("Bearer ") if auth_header else ""
        cart_uid = jwt.decode(auth_token, key=settings.secret_key)["uid"]
        return f(cart_uid, *args, **kwargs)

    return wrapped


@cart_blueprint.route("/add", methods=['POST'], endpoint="add_product")
@cart_decorator
def add_product_to_cart(cart_uid):
    cart_schema = CartUIDSchema(uid=cart_uid)
    product_schema = ProductCartSchema.parse_obj(request.json)
    cart = cart_repository.add_product_to_cart(cart_schema, product_schema)
    cart_repository.set_total_price(cart.uid)
    return CartResponseSchema.from_orm(cart).json(), http.HTTPStatus.CREATED


@cart_blueprint.route('/<int:id>', endpoint="show_products")
def show_products(id: int):
    cart = cart_repository.find(id)
    cart_items = cart.cart_items
    return jsonify(
        [CartItemResponseSchema.from_orm(cart_item).dict() for cart_item
         in cart_items]), http.HTTPStatus.OK
#TODO: корзину достать из токена


@cart_blueprint.route("/delete", methods=['DELETE'], endpoint="delete_product")
@cart_decorator
def delete_product(cart_uid):
    cart_schema = CartUIDSchema(uid=cart_uid)
    product_schema = ProductCartSchema.parse_obj(request.json)
    cart = cart_repository.remove_product_from_cart(cart_schema, product_schema)
    cart_repository.set_total_price(cart.uid)
    return CartResponseSchema.from_orm(cart).json(), http.HTTPStatus.ACCEPTED


@cart_blueprint.route("/update", methods=['PUT'])
@cart_decorator
def update_product_quantity(cart_uid):
    cart_schema = CartUIDSchema(uid=cart_uid)
    product_schema = ProductCartSchema.parse_obj(request.json)
    cart = cart_repository.change_quantity(cart_schema, product_schema)
    cart_repository.set_total_price(cart.uid)
    return CartResponseSchema.from_orm(cart).json(), http.HTTPStatus.ACCEPTED
