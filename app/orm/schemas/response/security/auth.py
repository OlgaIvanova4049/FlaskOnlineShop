import uuid
from typing import Optional

from pydantic import BaseModel, Field

def uuid_generator():
    return str(uuid.uuid4())

class Payload(BaseModel):
    uid: Optional[str] = Field(default_factory=uuid_generator)

class TokenResponse(BaseModel):
    access_token: str
    type: str='Bearer'