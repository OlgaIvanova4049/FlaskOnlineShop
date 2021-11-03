from typing import Optional

from pydantic import BaseModel, Field


class ProductRequestSchema(BaseModel):
    id: Optional[int]
    name: Optional[str]
    description: Optional[str]
    category_id: Optional[int]
    quantity: Optional[int]
    price: Optional[int]

class ProductAddSchema(BaseModel):
    id: int = Field(alias='product_id')
    quantity: int
#TODO: добавить валидацию