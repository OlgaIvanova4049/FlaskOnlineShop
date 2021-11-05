from typing import Optional

from pydantic import BaseModel, Field


class OrderItemRequestSchema(BaseModel):
    id: Optional[str]
    product_id: int
    price: int
    quantity: int
