from typing import List, Optional

from pydantic import BaseModel, validator


class ProductSchema(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        orm_mode = True


class Paginator(BaseModel):
    limit: Optional[int]=50
    offset: Optional[int]=0
    has_next: Optional[bool]=False
    has_previous: Optional[bool]=False
    total: Optional[int]=0


    # @validator("has_previous", pre=True, always=True)
    # def has_previous_result(cls, v, values, *kwargs):
    #     return values['offset'] !=0
    #
    # @validator("has_next", pre=True, always=True)
    # def has_next_result(cls, v, values, *kwargs):
    #     return values['limit'] + values['offset'] < values['total']



class ProductResponseSchema(BaseModel):
    items: List[ProductSchema]
    paginator: Paginator
    class Config:
        orm_mode = True