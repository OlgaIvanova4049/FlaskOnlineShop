from typing import Optional, ForwardRef

from pydantic import BaseModel
CategoryResponseSchema = ForwardRef('CategoryResponseSchema')

# class CategoryResponseSchema(BaseModel):
#     id: Optional[int]
#     name: Optional[str]
#     parent_object: Optional[CategoryResponseSchema]
#     all_parents: Optional[list]
#
#     class Config:
#         orm_mode = True



class CategoryResponseSchema(BaseModel):
    id: Optional[int]
    name: Optional[str]
    children: list[CategoryResponseSchema]

    class Config:
        orm_mode = True
#
CategoryResponseSchema.update_forward_refs()