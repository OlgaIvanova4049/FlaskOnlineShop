from app.exceptions.exceptions import (
    CartItemNotFoundException,
    ProductNotFoundException,
    QuantityNotEnoughException,
)
from app.orm.models.cart.cart_item_model import CartItemModel
from app.orm.models.cart.cart_model import CartModel
from app.orm.models.product.product_model import ProductModel
from app.orm.repository.base import BaseRepository, session_scope
from app.orm.schemas.request.cart.cart import CartSchema
from app.orm.schemas.request.product.product import ProductCartSchema


class CartRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.model = CartModel

    @staticmethod
    def find_product(session, product_id):
        product = session.query(ProductModel).get(product_id)
        if not product:
            raise ProductNotFoundException
        return product

    @staticmethod
    def find_cart_item(session, product_id, cart_id):
        cart_item = (
            session.query(CartItemModel)
            .filter_by(product_id=product_id, cart_id=cart_id)
            .first()
        )
        if not cart_item:
            raise CartItemNotFoundException
        return cart_item

    def find_by_uid(self, uid):
        with session_scope() as session:
            return session.query(self.model).filter_by(uid=uid).first()

    def add_product_to_cart(
        self, cart_schema: CartSchema, product_schema: ProductCartSchema
    ):
        cart = self.find_by_uid(cart_schema.uid)
        if not cart:
            cart = self.create(cart_schema)

        with session_scope() as session:
            product = self.find_product(session, product_schema.id)
            if product.quantity < product_schema.quantity:
                raise QuantityNotEnoughException
            cart_item = (
                session.query(CartItemModel)
                .filter_by(product_id=product_schema.id, cart_id=cart.id)
                .first()
            )
            if cart_item:
                cart_item.quantity += product_schema.quantity
            else:
                cart_item = CartItemModel(
                    cart_id=cart.id,
                    product_id=product.id,
                    price=product.price
                    - (product.total_discount * product.price),
                    quantity=product_schema.quantity,
                )
                session.add(cart_item)
            product.quantity -= product_schema.quantity
            session.commit()
        return cart

    def remove_product_from_cart(
        self, cart_schema: CartSchema, product_schema: ProductCartSchema
    ):
        with session_scope() as session:
            cart = self.find_by_uid(cart_schema.uid)
            product = self.find_product(session, product_schema.id)
            cart_item = self.find_cart_item(
                session, product_schema.id, cart.id
            )
            product.quantity += cart_item.quantity
            session.delete(cart_item)
            session.commit()

        return cart

    def change_quantity(
        self, cart_schema: CartSchema, product_schema: ProductCartSchema
    ):
        with session_scope() as session:
            cart = self.find_by_uid(cart_schema.uid)
            product = self.find_product(session, product_schema.id)
            cart_item = self.find_cart_item(
                session, product_schema.id, cart.id
            )
            old_quantity = cart_item.quantity
            cart_item.quantity = product_schema.quantity
            quantity_delta = old_quantity - product_schema.quantity
            if quantity_delta < 0 and abs(quantity_delta) > product.quantity:
                raise QuantityNotEnoughException
            product.quantity += quantity_delta
            session.commit()

        return cart

    def set_total_price(self, cart_uid):
        with session_scope() as session:
            cart = session.query(self.model).filter_by(uid=cart_uid).first()
            cart.total_price = cart.count_total_price()
            session.commit()
