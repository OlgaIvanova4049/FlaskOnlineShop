from typing import Optional

from pydantic import BaseModel


class CartResponseSchema(BaseModel):
    id: Optional[int]
    user_id: Optional[int]

    class Config:
        orm_mode = True