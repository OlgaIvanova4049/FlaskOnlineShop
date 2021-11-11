import http

from flask import Blueprint, jsonify, request

from app.api.views.cart_view import scope_decorator
from app.exceptions.exceptions import AccessDeniedException
from app.orm.models.product.product_model import ProductModel
from app.orm.repository import category_repository
from app.orm.repository import product_repository
from app.orm.schemas.query.product.product_query import ProductQueryParam
from app.orm.schemas.request.product.category import CategoryRequestSchema
from app.orm.schemas.response.product.category_response import CategoryChildrenResponseSchema, CategoryResponseSchema
from app.orm.schemas.response.product.product_response import ProductSchema, ProductResponseSchema

category_blueprint = Blueprint('category_blueprint', __name__, url_prefix="/categories")


@category_blueprint.route('/<int:id>/products')
def find_all_products(id: int):
    query_param: ProductQueryParam = ProductQueryParam.as_obj(request.args.to_dict(flat=True))
    products: list[ProductModel] = product_repository.products_in_category(id)
    paginator = query_param.paginator.copy(update={"total": product_repository.count()})
    return ProductResponseSchema(items=[ProductSchema.from_orm(product).dict() for product in products],
                                 paginator=paginator).dict(), http.HTTPStatus.OK


@category_blueprint.route('')
def find_all():
    categories = category_repository.find_all()
    return jsonify(
        [CategoryChildrenResponseSchema.from_orm(category).dict() for category in categories]), http.HTTPStatus.OK



@category_blueprint.route('', methods=['POST'])
@scope_decorator
def new_category(scope):
    if "create category" not in scope:
        raise AccessDeniedException
    category = category_repository.create(CategoryRequestSchema.parse_obj(request.json))
    return CategoryResponseSchema.from_orm(category).json(), http.HTTPStatus.CREATED


@category_blueprint.route('/<int:id>', methods=['PUT'])
@scope_decorator
def update_category(scope, id: int):
    if "update category" not in scope:
        raise AccessDeniedException
    category = category_repository.update(id, CategoryRequestSchema.parse_obj(request.json))
    return CategoryChildrenResponseSchema.from_orm(category).json(), http.HTTPStatus.ACCEPTED


@category_blueprint.route('/<int:id>', methods=['DELETE'])
@scope_decorator
def delete_category(scope, id: int):
    if "delete category" not in scope:
        raise AccessDeniedException
    category_repository.delete(id)
    return jsonify({"message": "Category was successfully deleted"}), http.HTTPStatus.NO_CONTENT
