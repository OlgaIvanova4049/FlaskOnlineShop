from typing import Optional, List

from pydantic import BaseModel

class NestedCategory(BaseModel):
    name:str

    class Config:
        orm_mode = True

class CategoryResponseSchema(BaseModel):
    id: int
    name: str
    # nested_categories: Optional[List[NestedCategory]]


    class Config:
        orm_mode = True