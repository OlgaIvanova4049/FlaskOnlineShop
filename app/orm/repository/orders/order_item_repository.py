from app.orm.models.order.order_item_model import OrderItemModel
from app.orm.repository.base import BaseRepository


class OrderItemRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.model = OrderItemModel
