from pydantic import BaseModel


class CategorySchema(BaseModel):
    id: int
    name: str
    # nested_categories: list['CategorySchema']


    class Config:
        orm_mode = True