from typing import Optional

from pydantic import BaseModel

from app.orm.schemas.request.cart.cart_item import CartItemRequestSchema


class CartSchema(BaseModel):
    id: Optional[int]
    user_id: int = None
    total_price: Optional[int]

    class Config:
        orm_mode = True


class CartSchemaWithItems(CartSchema):
    cart_items: Optional[list[CartItemRequestSchema]]


class CartUIDSchema(CartSchema):
    uid: Optional[str]
