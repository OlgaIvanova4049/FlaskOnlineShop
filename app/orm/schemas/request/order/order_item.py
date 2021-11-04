from typing import Optional

from pydantic import BaseModel, Field


class OrderItemRequestSchema(BaseModel):
    id: Optional[str]
    order_id: int = Field(alias='id')
    product_id: int
    price: int
    quantity: int
