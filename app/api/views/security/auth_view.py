from flask import Blueprint, request

from app.exceptions.exceptions import UserNotFoundException
from app.orm.repository import cart_repository, token_repository
from app.orm.repository import user_repository
from app.orm.schemas.request.cart.cart import CartSchema
from app.orm.schemas.request.user.token import TokenRequestSchema
from app.orm.schemas.request.user.user import UserSchemaRequest
from app.orm.schemas.response.security.auth import Payload, TokenResponse
from app.services.security.auth_service import encode_auth_token

auth_blueprint = Blueprint('auth_blueprint', __name__, url_prefix="/login")


@auth_blueprint.post('/anon')
def get_token():
    token = encode_auth_token(Payload())
    return TokenResponse(access_token=token).json()


@auth_blueprint.post('')
def login():
    user = user_repository.find_by_email(UserSchemaRequest.parse_obj(request.json).email)
    if not user:
        raise UserNotFoundException
    cart = user.cart
    if not cart:
        cart = cart_repository.create(CartSchema(user_id=user.id))
    payload = Payload(uid=str(cart.uid))
    token = encode_auth_token(payload)
    token_repository.create(TokenRequestSchema(access_token=payload.jti,
                                               user_id=user.id,
                                               exp=payload.exp))
    return TokenResponse(access_token=token).json()
