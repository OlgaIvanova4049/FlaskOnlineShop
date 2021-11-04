from typing import Optional

from pydantic import BaseModel

from app.orm.schemas.response.product.product_response import ProductInCart


class CartItemResponseSchema(BaseModel):
    product_id:Optional[int]
    price: Optional[int]
    quantity: Optional[int]
    product: Optional[ProductInCart]

    class Config:
        orm_mode = True