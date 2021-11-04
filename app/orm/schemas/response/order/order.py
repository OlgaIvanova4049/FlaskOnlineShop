from typing import Optional

from pydantic import BaseModel


class OrderResponseSchema(BaseModel):
    id: Optional[int]
    user_id: Optional[int]

    class Config:
        orm_mode = True
