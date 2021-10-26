from app.orm.models.cart.cart_model import CartModel
from app.orm.repository.base import BaseRepository


class CartRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.model = CartModel
