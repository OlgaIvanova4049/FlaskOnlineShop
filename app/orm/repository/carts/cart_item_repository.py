from app.orm.models.cart.cart_item_model import CartItemModel
from app.orm.repository.base import BaseRepository


class CartItemRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.model = CartItemModel

