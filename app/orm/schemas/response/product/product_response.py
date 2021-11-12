from typing import List, Optional

from pydantic import BaseModel


class ProductInCart(BaseModel):
    name: Optional[str]
    description: Optional[str]
    category_id: Optional[int]

    class Config:
        orm_mode = True


class ProductSchema(ProductInCart):
    id: Optional[int]
    quantity: Optional[int]
    price: Optional[int]


class Paginator(BaseModel):
    limit: Optional[int] = 50
    offset: Optional[int] = 0


class ProductResponseSchema(BaseModel):
    items: List[ProductSchema]
    paginator: Paginator

    class Config:
        orm_mode = True
