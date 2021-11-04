import http

from flask import Blueprint, jsonify, request

from app.orm.models.user.user_model import UserModel
from app.orm.repository import user_repository, cart_repository
from app.orm.schemas.request.cart.cart import CartSchema
from app.orm.schemas.request.user.user import UserSchemaRequest
from app.orm.schemas.response.user.user import UserSchemaResponse

user_blueprint = Blueprint('user_blueprint', __name__, url_prefix="/users")


@user_blueprint.route('')
def find_all():
    users: list[UserModel] = user_repository.find_all()
    return jsonify([UserSchemaResponse.from_orm(user).dict() for user in users]), http.HTTPStatus.OK


@user_blueprint.route('/<int:id>')
def single_user(id: int):
    user = user_repository.find(id)
    return UserSchemaResponse.from_orm(user).json(), http.HTTPStatus.OK


@user_blueprint.route('', methods=['POST'])
def new_user():
    user = user_repository.create(UserSchemaRequest.parse_obj(request.json))
    cart_repository.create(CartSchema.parse_obj({'user_id': user.id}))
    return UserSchemaResponse.from_orm(user).json(), http.HTTPStatus.CREATED


@user_blueprint.route('/<int:id>', methods=['PUT'])
def update_user(id: int):
    user = user_repository.update(id, UserSchemaRequest.parse_obj(request.json))
    return UserSchemaResponse.from_orm(user).json(), http.HTTPStatus.ACCEPTED


@user_blueprint.route('/<int:id>', methods=['DELETE'])
def delete_user(id: int):
    user_repository.delete(id)
    return jsonify({"message": "User was successfully deleted"}), http.HTTPStatus.NO_CONTENT
