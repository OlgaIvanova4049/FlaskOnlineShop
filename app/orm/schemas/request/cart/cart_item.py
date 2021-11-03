from typing import Optional

from pydantic import BaseModel


class CartItemRequestSchema(BaseModel):
    id: Optional[int]
    cart_id:  Optional[int]
    product_id:  Optional[int]
    price:  Optional[int]
    quantity:  Optional[int]

    class Config:
        orm_mode = True