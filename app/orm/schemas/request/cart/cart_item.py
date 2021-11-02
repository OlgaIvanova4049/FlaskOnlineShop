from typing import Optional

from pydantic import BaseModel


class CartItemRequestSchema(BaseModel):
    id: Optional[int]
    cart_id: int
    product_id: int
    price: int
    quantity: int