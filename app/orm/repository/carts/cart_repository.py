from app.orm.models.cart.cart_model import CartModel
from app.orm.repository.base import BaseRepository, session_scope


class CartRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.model = CartModel

    def find_by_uid(self, uid):
        with session_scope() as session:
            return session.query(self.model).filter_by(uid=uid).first()

    def total_price(self, uid):
            cart = self.find_by_uid(uid)
            cart_items = cart.cart_item
            return sum(cart_item.price * cart_item.quantity for cart_item in cart_items)
