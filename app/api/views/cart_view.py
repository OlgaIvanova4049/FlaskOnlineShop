import http

from flask import Blueprint, request
from jose import jwt

from app.core.settings import settings
from app.orm.repository import product_repository, cart_repository, cart_item_repository
from app.orm.schemas.request.cart.cart import CartSchema
from app.orm.schemas.request.cart.cart_item import CartItemRequestSchema
from app.orm.schemas.response.cart.cart import CartResponseSchema
from app.orm.schemas.response.cart.cart_item import CartItemResponseSchema
from app.orm.schemas.response.product.product_response import ProductSchema

cart_blueprint = Blueprint('cart_blueprint', __name__, url_prefix="/cart")

def cart_decorator(f):
    def wrapped(*args, **kwargs):
        token = request.json["token"]
        cart_uid = jwt.decode(token, key=settings.secret_key)["uid"]
        return f(cart_uid, *args, **kwargs)
    return wrapped

@cart_blueprint.route("", methods=['POST'], endpoint="add_product")
@cart_decorator
def add_product_to_cart(cart_uid):
    cart = cart_repository.find_by_uid(cart_uid)
    if not cart:
        cart = cart_repository.create(CartSchema(uid=cart_uid))
    product = product_repository.find(request.json["product_id"])
    cart_item = cart_item_repository.create(CartItemRequestSchema.parse_obj({"cart_id": cart.id,
                                                                 "product_id": product.id,
                                                                "price": product.price,
                                                                 "quantity": request.json["quantity"]}))
    total_price = cart_repository.total_price(uid=cart.uid)
    cart_repository.update(cart.id, CartSchema.parse_obj({"total_price": total_price}))
    return CartItemResponseSchema.from_orm(cart_item).json(), http.HTTPStatus.CREATED

@cart_blueprint.route('/<int:cart_id>/<int:cart_item_id>', endpoint="show_product")
def show_product(cart_id, cart_item_id):
    product, quantity = cart_item_repository.show_product(cart_id, cart_item_id)
    product_schema = ProductSchema.from_orm(product)
    product = product_schema.copy(update={"quantity": quantity})
    return product.json(), http.HTTPStatus.OK

@cart_blueprint.route("", methods=['DELETE'], endpoint="delete_product")
@cart_decorator
def delete_product(cart_uid):
    cart = cart_repository.find_by_uid(cart_uid)
    cart_item = cart_item_repository.find_by_product(request.json["product_id"])
    print(cart_item)
    cart_item_repository.delete(cart_item.id)
    total_price = cart_repository.total_price(uid=cart.uid)
    cart_repository.update(cart.id, CartSchema.parse_obj({"total_price": total_price}))
    return CartResponseSchema.from_orm(cart).json(), http.HTTPStatus.ACCEPTED