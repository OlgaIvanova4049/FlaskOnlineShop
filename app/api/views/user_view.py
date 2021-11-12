import http

from flask import Blueprint, jsonify, request

from app.api.views.cart_view import scope_decorator
from app.exceptions.exceptions import (
    AccessDeniedException,
    UserExistsException,
    UserNotFoundException,
)
from app.orm.models.user.user_model import UserModel
from app.orm.repository import cart_repository, user_repository
from app.orm.schemas.request.cart.cart import CartSchema
from app.orm.schemas.request.user.user import UserSchemaRequest
from app.orm.schemas.response.user.user import UserSchemaResponse

user_blueprint = Blueprint("user_blueprint", __name__, url_prefix="/users")


@user_blueprint.route("")
@scope_decorator
def find_all(scope):
    if "get all users" not in scope:
        raise AccessDeniedException
    users: list[UserModel] = user_repository.find_all()
    return (
        jsonify([UserSchemaResponse.from_orm(user).dict() for user in users]),
        http.HTTPStatus.OK,
    )


@user_blueprint.route("/<int:id>")
@scope_decorator
def single_user(scope, id: int):
    if "get user" not in scope:
        raise AccessDeniedException
    user = user_repository.find(id)
    if not user:
        raise UserNotFoundException
    return UserSchemaResponse.from_orm(user).json(), http.HTTPStatus.OK


@user_blueprint.route("", methods=["POST"])
@scope_decorator
def new_user(scope):
    if "create user" not in scope:
        raise AccessDeniedException
    user = user_repository.find_by_email(request.json["email"])
    if user:
        raise UserExistsException
    user = user_repository.create(UserSchemaRequest.parse_obj(request.json))
    cart_repository.create(CartSchema.parse_obj({"user_id": user.id}))
    return UserSchemaResponse.from_orm(user).json(), http.HTTPStatus.CREATED


@user_blueprint.route("/<int:id>", methods=["PUT"])
@scope_decorator
def update_user(scope, id: int):
    if "update user" not in scope:
        raise AccessDeniedException
    user = user_repository.find(id)
    if not user:
        raise UserNotFoundException
    user = user_repository.update(
        id, UserSchemaRequest.parse_obj(request.json)
    )
    return UserSchemaResponse.from_orm(user).json(), http.HTTPStatus.ACCEPTED


@user_blueprint.route("/<int:id>", methods=["DELETE"])
@scope_decorator
def delete_user(scope, id: int):
    if "delete user" not in scope:
        raise AccessDeniedException
    user = user_repository.find(id)
    if not user:
        raise UserNotFoundException
    user_repository.delete(id)
    return (
        jsonify({"message": "User was successfully deleted"}),
        http.HTTPStatus.NO_CONTENT,
    )
