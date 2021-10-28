from typing import Optional

from pydantic import BaseModel


class CategoryResponseSchema(BaseModel):
    id: Optional[int]
    name: Optional[str]
    nested_categories: Optional[list]
    all_parents: Optional[list]

    class Config:
        orm_mode = True