from typing import Optional

from pydantic import BaseModel


class CategoryRequestSchema(BaseModel):
    id: Optional[int]
    name: Optional[str]
    parent_category: Optional[int]
