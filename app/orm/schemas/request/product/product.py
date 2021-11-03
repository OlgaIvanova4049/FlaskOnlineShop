from typing import Optional

from pydantic import BaseModel, Field, validator


class ProductRequestSchema(BaseModel):
    id: Optional[int]
    name: Optional[str]
    description: Optional[str]
    category_id: Optional[int]
    quantity: Optional[int]
    price: Optional[int]

class ProductCartSchema(BaseModel):
    id: int = Field(alias='product_id')
    quantity: Optional[int]

    @validator('quantity')
    def must_be_positive(cls, v):
        if v < 1:
            raise ValueError('must be positive')
        return v