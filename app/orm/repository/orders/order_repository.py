from app.orm.models.order.order_model import OrderModel
from app.orm.repository.base import BaseRepository, session_scope


class OrderRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.model = OrderModel

    def create_order(self, cart_schema):
        with session_scope() as session:
            order = OrderModel(
                user_id=cart_schema.user_id,
                total_price=cart_schema.total_price,
            )
            session.add(order)
            session.commit()
            return order
