from app.orm.models.cart.cart_model import CartModel
from app.orm.repository.base import BaseRepository, session_scope


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



