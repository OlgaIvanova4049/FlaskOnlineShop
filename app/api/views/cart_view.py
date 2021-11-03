import http

from flask import Blueprint, request, jsonify
from jose import jwt

from app.core.settings import settings
from app.orm.repository import product_repository, cart_repository, cart_item_repository
from app.orm.schemas.request.cart.cart import CartSchema
from app.orm.schemas.request.cart.cart_item import CartItemRequestSchema
from app.orm.schemas.request.product.product import ProductAddSchema
from app.orm.schemas.response.cart.cart import CartResponseSchema
from app.orm.schemas.response.cart.cart_item import CartItemResponseSchema


cart_blueprint = Blueprint('cart_blueprint', __name__, url_prefix="/cart")


def cart_decorator(f):
    # TODO: добавить документацию, functools.wraps, исключение
    def wrapped(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header:
            auth_token = auth_header.split(" ")[1]
        cart_uid = jwt.decode(auth_token, key=settings.secret_key)["uid"]
        return f(cart_uid, *args, **kwargs)

    return wrapped


@cart_blueprint.route("/add", methods=['POST'], endpoint="add_product")
@cart_decorator
def add_product_to_cart(cart_uid):
    cart = cart_repository.find_by_uid(cart_uid)
    if not cart:
        cart = cart_repository.create(CartSchema(uid=cart_uid))
    product_schema = ProductAddSchema.parse_obj(request.json)
    product = product_repository.find(product_schema.id)
    product_in_cart = cart_item_repository.product_in_cart(cart.id, product_schema.id)
    if product_in_cart:
        cart_item_repository.update_quantity(product_in_cart.id, product_schema.quantity)
    else:
        cart_item_repository.create(CartItemRequestSchema(cart_id=cart.id,
                                                          product_id=product.id,
                                                          price=product.price,
                                                          quantity=product_schema.quantity))
    cart = cart_repository.find_by_uid(cart_uid)
    product_repository.update_quantity(product_schema.id, product_schema.quantity)
    cart_repository.update_price(cart.count_total_price(), cart_uid)
    # TODO: изменить количество продукта+, сделать метод в модели для подсчеты total price+, композитный индекс+
    return CartResponseSchema.from_orm(cart).json(), http.HTTPStatus.CREATED


@cart_blueprint.route('/<int:id>', endpoint="show_products")
def show_products(id: int):
    cart = cart_repository.find(id)
    cart_items = cart.cart_items
    # return jsonify([ProductInCartSchema.from_orm(cart_item.product).dict() for cart_item in cart_items]), http.HTTPStatus.OK
    return jsonify([CartItemResponseSchema.from_orm(cart_item).dict(exclude={"id", "product_id", "cart_id","price"}) for cart_item in cart_items]), http.HTTPStatus.OK


@cart_blueprint.route("", methods=['DELETE'], endpoint="delete_product")
@cart_decorator
def delete_product(cart_uid):
    cart = cart_repository.find_by_uid(cart_uid)
    cart_item = cart_item_repository.find_by_product(request.json["product_id"])
    cart_item_repository.delete(cart_item.id)
    # TODO: добавить несколько условий в фильтр прежде чем удалить
    total_price = cart_repository.total_price(uid=cart.uid)
    cart_repository.update(cart.id, CartSchema.parse_obj({"total_price": total_price}))
    return CartResponseSchema.from_orm(cart).json(), http.HTTPStatus.ACCEPTED
