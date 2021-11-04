from app.orm.models.order.order_item_model import OrderItemModel
from app.orm.repository.base import BaseRepository, session_scope


class OrderItemRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.model = OrderItemModel

    def create_order_items(self, cart_item, order_id):
        with session_scope() as session:
            order_item = OrderItemModel(
                order_id=order_id,
                product_id=cart_item.product_id,
                price=cart_item.price,
                quantity=cart_item.quantity)
            session.add(order_item)
            session.commit()
            return order_item
