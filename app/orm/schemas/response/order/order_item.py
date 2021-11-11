from typing import Optional

from pydantic import BaseModel


class OrderItemResponseSchema(BaseModel):
    product_id: Optional[int]
    price: Optional[int]
    quantity: Optional[int]

    class Config:
        orm_mode = True
