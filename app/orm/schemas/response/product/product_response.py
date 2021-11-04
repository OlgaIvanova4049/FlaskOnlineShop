from typing import List, Optional

from pydantic import BaseModel

from app.orm.schemas.response.product.category_response import CategoryResponseSchema


class ProductInCart(BaseModel):
    name: Optional[str]
    description: Optional[str]
    category: Optional[CategoryResponseSchema]

    class Config:
        orm_mode = True


class ProductSchema(ProductInCart):
    id: Optional[int]
    quantity: Optional[int]
    price: Optional[int]


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
