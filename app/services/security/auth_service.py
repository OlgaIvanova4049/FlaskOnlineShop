import uuid
from typing import Optional

from jose import jwt, JWTError
from app.core.settings import settings
from app.orm.schemas.response.security.auth import Payload


def set_payload(uid: Optional[str] = None) -> Payload:
    return Payload(uid=uid)


def encode_auth_token(payload: Payload):
    token = jwt.encode(claims=payload.dict(), key=settings.secret_key, algorithm=settings.algorithm)
    return token
