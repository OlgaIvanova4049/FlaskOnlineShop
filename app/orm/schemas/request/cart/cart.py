from typing import Optional

from pydantic import BaseModel


class CartSchema(BaseModel):
    id: Optional[int]
    user_id: int
