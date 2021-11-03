from typing import List, Optional

from pydantic import BaseModel


class ProductInCart(BaseModel):
    id: Optional[int]
    name: Optional[str]
    description: Optional[str]
    price: Optional[int]

    class Config:
        orm_mode = True


class ProductSchema(ProductInCart):
    quantity: Optional[int]


class Paginator(BaseModel):
    limit: Optional[int] = 50
    offset: Optional[int] = 0
    has_next: Optional[bool] = False
    has_previous: Optional[bool] = False
    total: Optional[int] = 0


class ProductResponseSchema(BaseModel):
    items: List[ProductSchema]
    paginator: Paginator

    class Config:
        orm_mode = True
