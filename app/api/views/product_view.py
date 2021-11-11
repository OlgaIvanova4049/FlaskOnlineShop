import http

from flask import Blueprint, request

from app.api.views.cart_view import scope_decorator
from app.exceptions.exceptions import AccessDeniedException, ProductNotFoundException, ProductExistsException
from app.orm.models.product.product_model import ProductModel
from app.orm.repository import product_repository
from app.orm.schemas.query.product.product_query import ProductQueryParam
from app.orm.schemas.request.product.product import ProductRequestSchema
from app.orm.schemas.response.product.product_response import ProductSchema, ProductResponseSchema

product_blueprint = Blueprint('product_blueprint', __name__, url_prefix="/products")


@product_blueprint.route('')
def find_all():
    query_param: ProductQueryParam = ProductQueryParam.as_obj(request.args.to_dict(flat=True))
    products: list[ProductModel] = product_repository.filtered_sorted_product_list(query_param)
    return ProductResponseSchema(items=[ProductSchema.from_orm(product).dict() for product in products],
                                 paginator=query_param.paginator).dict(), http.HTTPStatus.OK


@product_blueprint.route('/<int:id>')
def single_product(id: int):
    product = product_repository.find(id)
    if not product:
        raise ProductNotFoundException
    return ProductSchema.from_orm(product).json(), http.HTTPStatus.OK


@product_blueprint.route('', methods=['POST'])
@scope_decorator
def new_product(scope):
    if "create product" not in scope:
        raise AccessDeniedException
    product = product_repository.find_by_name(request.json['name'])
    if product:
        raise ProductExistsException
    product = product_repository.create(ProductRequestSchema.parse_obj(request.json))
    return ProductSchema.from_orm(product).json(), http.HTTPStatus.CREATED


@product_blueprint.route('/<int:id>', methods=['PUT'])
@scope_decorator
def update_product(scope, id: int):
    if "update product" not in scope:
        raise AccessDeniedException
    product = product_repository.update(id, ProductRequestSchema.parse_obj(request.json))
    if not product:
        raise ProductNotFoundException
    return ProductSchema.from_orm(product).json(), http.HTTPStatus.ACCEPTED


@product_blueprint.route('/<int:id>', methods=['DELETE'])
@scope_decorator
def delete_product(scope, id: int):
    if "delete product" not in scope:
        raise AccessDeniedException
    product = product_repository.find(id)
    if not product:
        raise ProductNotFoundException
    product_repository.delete(id)
    return {}, http.HTTPStatus.NO_CONTENT
