import random
import string
import uuid
from typing import Optional

from pydantic import BaseModel, Field
from datetime import datetime, timedelta

from app.core.constants import token_life_time_hours


def uuid_generator():
    return str(uuid.uuid4())


def jti_generator():
    return ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(25)])

def expired_generator():
    return datetime.now() + timedelta(hours=token_life_time_hours)


class Payload(BaseModel):
    uid: Optional[str] = Field(default_factory=uuid_generator)
    iat: datetime = Field(default_factory=datetime.now)
    exp: datetime = Field(default_factory=expired_generator)
    jti: str = Field(default_factory=jti_generator)


class TokenResponse(BaseModel):
    access_token: str
    type: str = 'Bearer'
