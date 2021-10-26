from pydantic import BaseModel


class CategoryRequestSchema(BaseModel):
    id: int
    name: str
    parent_category: int