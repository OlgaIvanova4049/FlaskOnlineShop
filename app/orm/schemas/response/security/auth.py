import random
import string
import uuid
from typing import Optional

from pydantic import BaseModel, Field
from pydantic.schema import timedelta, datetime

from app.core.constants import token_life_time_hours


def uuid_generator():
    return str(uuid.uuid4())


def jti_generator():
    return ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(25)])


class Payload(BaseModel):
    uid: Optional[str] = Field(default_factory=uuid_generator)
    iat: datetime = Field(default=datetime.now())
    exp: datetime = Field(default=datetime.now() + timedelta(hours=token_life_time_hours))
    jti: str = Field(default_factory=jti_generator)


class TokenResponse(BaseModel):
    access_token: str
    type: str = 'Bearer'
