from pydantic import BaseModel


class CategorySchema(BaseModel):
    id: int
    name: str
    parent_category: int