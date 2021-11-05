from typing import Optional

from pydantic import BaseModel

from app.orm.schemas.response.order.order_item import OrderItemResponseSchema


class OrderResponseSchema(BaseModel):
    id: Optional[int]
    user_id: Optional[int]
    total_price: Optional[int]

    class Config:
        orm_mode = True


class OrderResponseSchemaWithItems(OrderResponseSchema):
    order_items: Optional[list[OrderItemResponseSchema]]
