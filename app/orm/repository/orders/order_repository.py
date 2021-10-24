from app.orm.models.order.order_model import OrderModel
from app.orm.repository.base import BaseRepository


class OrderRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.model = OrderModel
