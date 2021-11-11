from typing import Optional

from pydantic import BaseModel, Field


class CartItemRequestSchema(BaseModel):
    id: Optional[int]
    cart_id: Optional[int] = Field(..., alias="order_id")
    product_id: Optional[int]
    price: Optional[int]
    quantity: Optional[int]

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
