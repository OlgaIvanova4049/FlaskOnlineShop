from app.orm.models.cart.cart_model import CartModel
from app.orm.models.product.product_model import ProductModel
from app.orm.repository import cart_item_repository, product_repository
from app.orm.repository.base import BaseRepository, session_scope
from app.orm.schemas.request.cart.cart import CartSchema
from app.orm.schemas.request.cart.cart_item import CartItemRequestSchema
from app.orm.schemas.request.product.product import ProductCartSchema


class CartRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.model = CartModel

    def find_by_uid(self, uid):
        with session_scope() as session:
            return session.query(self.model).filter_by(uid=uid).first()

    def update_price(self, total_price, uid):
        with session_scope() as session:
            cart = session.query(self.model).filter_by(uid=uid).update({"total_price": total_price})
            session.commit()
            return cart

    def add_product_to_cart(self, cart_schema: CartSchema, product_schema: ProductCartSchema):
        cart = self.find_by_uid(cart_schema.uid)
        if not cart:
            cart = self.create(cart_schema)

        with session_scope() as session:
            product = session.query(ProductModel).get(id)
            cart_item = session.query(self.model).filter_by(product_id=product_schema.id, cart_id=cart.id).first()
            if cart_item:
                cart_item.quantity += product_schema.quantity
            else:
                cart_item_repository.create(
                    CartItemRequestSchema(
                        cart_id=cart.id,
                        product_id=product.id,
                        price=product.price,
                        quantity=product_schema.quantity
                    )
                )
            product.quantity -= product_schema.quantity

        return cart
