from app.orm.models.order.order_item_model import OrderItemModel
from app.orm.repository.base import BaseRepository
from app.orm.schemas.request.cart.cart_item import CartItemRequestSchema


class OrderItemRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.model = OrderItemModel

    def create_order_items(self, schemas: CartItemRequestSchema, order_id):
        objects = []
        for schema in schemas:
            schema.cart_id = order_id
            objects.append(
                self.model(**schema.dict(exclude={"id"}, by_alias=True))
            )
        self.bulk_save(objects)
