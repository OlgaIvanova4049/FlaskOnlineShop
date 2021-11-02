from typing import Optional

from pydantic import BaseModel


class CartItemResponseSchema(BaseModel):
    id: Optional[int]
    cart_id: int
    product_id: int
    price: int
    quantity: int

    class Config:
        orm_mode = True