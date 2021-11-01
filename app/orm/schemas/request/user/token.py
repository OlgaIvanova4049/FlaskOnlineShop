from datetime import datetime
from typing import Optional, Tuple

from pydantic import BaseModel, fields, validator
from pydantic.validators import timedelta
from app.core.constants import token_life_time_hours


class TokenRequestSchema(BaseModel):
    id: Optional[int]
    access_token: str
    refresh_token: Optional[str]
    user_id: Optional[int]
    scope:Optional[tuple]
    expired_at: datetime = datetime.now() + timedelta(hours=token_life_time_hours)
