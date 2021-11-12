from jose import jwt

from app.core.settings import settings
from app.orm.schemas.response.security.auth import Payload


def encode_auth_token(payload: Payload):
    return jwt.encode(
        claims=payload.dict(),
        key=settings.secret_key,
        algorithm=settings.algorithm,
    )
