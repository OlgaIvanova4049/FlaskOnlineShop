from flask import Blueprint, request
from jose import jwt

from app.core.settings import settings
from app.orm.repository import product_repository, cart_repository, cart_item_repository
from app.orm.schemas.request.cart.cart import CartSchema
from app.orm.schemas.request.cart.cart_item import CartItemRequestSchema

cart_blueprint = Blueprint('cart_blueprint', __name__, url_prefix="/cart")

def cart_decorator(f):
    def wrapped(*args, **kwargs):
        token = request.json["token"]
        cart_uid = jwt.decode(token, key=settings.secret_key)["uid"]
        return f(cart_uid)
    return wrapped

@cart_blueprint.route("", methods=['POST'])
@cart_decorator
def add_product_to_cart(cart_uid):
    cart = cart_repository.find_by_uid(cart_uid)
    if not cart:
        cart = cart_repository.create(CartSchema())
    product = product_repository.find(request.json["product_id"])
    cart_item_repository.create(CartItemRequestSchema.parse_obj({"cart_id":cart.id,
                                                                 "product_id":product.id,
                                                                "price":product.price,
                                                                 "quantity":request.json["quantity"]}))
    total_price = cart_repository.total_price(uid=cart.uid)
    cart_repository.update(cart.id, CartSchema.parse_obj({"total_price":total_price}))
    return {}