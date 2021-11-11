from typing import List, Optional

from pydantic import BaseModel, validator

from app.orm.schemas.response.product.category_response import CategoryResponseSchema


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
    # total: Optional[int] = 0
    # has_next: Optional[bool] = False
    # has_previous: Optional[bool] = False
    #
    #
    # @validator("has_next", always=True)
    # def has_next_result(cls, v, values, field):
    #     return values['limit'] + values['offset'] < values['total']
    #
    # @validator("has_previous", always=True)
    # def has_previous_result(cls, v, values, field):
    #     return values['offset'] !=0


class ProductResponseSchema(BaseModel):
    items: List[ProductSchema]
    paginator: Paginator

    class Config:
        orm_mode = True
