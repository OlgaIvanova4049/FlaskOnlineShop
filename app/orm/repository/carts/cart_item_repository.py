from app.orm.models.cart.cart_item_model import CartItemModel
from app.orm.repository.base import BaseRepository, session_scope


class CartItemRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.model = CartItemModel

    def product_in_cart(self, cart_id, product_id):
        with session_scope() as session:
            return session.query(self.model).filter_by(product_id=product_id, cart_id=cart_id).first()

    def update_quantity(self, id, quantity):
        with session_scope() as session:
            cart_item = session.query(self.model).filter_by(id=id)
            new_quantity = cart_item.first().quantity + quantity
            cart_item.update({"quantity": new_quantity})
            session.commit()
            return cart_item
