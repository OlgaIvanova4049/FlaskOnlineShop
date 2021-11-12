from typing import ForwardRef, Optional

from pydantic import BaseModel


class CategoryResponseSchema(BaseModel):
    id: Optional[int]
    name: Optional[str]

    class Config:
        orm_mode = True


CategoryParentResponseSchema = ForwardRef("CategoryParentResponseSchema")


class CategoryParentResponseSchema(BaseModel):
    id: Optional[int]
    name: Optional[str]
    parent_object: Optional[CategoryParentResponseSchema]
    all_parents: Optional[list]

    class Config:
        orm_mode = True


CategoryChildrenResponseSchema = ForwardRef("CategoryChildrenResponseSchema")


class CategoryChildrenResponseSchema(CategoryResponseSchema):
    children: Optional[list[CategoryChildrenResponseSchema]]


CategoryChildrenResponseSchema.update_forward_refs()
CategoryParentResponseSchema.update_forward_refs()
