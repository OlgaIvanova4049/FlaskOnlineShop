from typing import Optional

from pydantic import BaseModel


class ProductRequestSchema(BaseModel):
    id: Optional[int]
    name: Optional[str]
    description: Optional[str]
    category_id: Optional[int]
    quantity: Optional[int]
    price: Optional[int]
