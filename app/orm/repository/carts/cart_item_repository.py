from app.orm.models.cart.cart_item_model import CartItemModel
from app.orm.repository.base import BaseRepository, session_scope


class CartItemRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.model = CartItemModel

    def show_product(self, cart_id, cart_item_id):
        with session_scope() as session:
            cart_item = session.query(self.model).get(cart_item_id)
            product = cart_item.product
            quantity = cart_item.quantity
            return product, quantity