from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class TokenRequestSchema(BaseModel):
    id: Optional[int]
    access_token: str
    refresh_token: Optional[str]
    user_id: Optional[int]
    scope: Optional[tuple]
    expired_at: datetime = Field(alias='exp')
