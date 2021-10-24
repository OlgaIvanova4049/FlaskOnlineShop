import json
from typing import Optional

from pydantic import BaseModel


class UserSchema(BaseModel):
    email: Optional[str]
    password: Optional[str]




