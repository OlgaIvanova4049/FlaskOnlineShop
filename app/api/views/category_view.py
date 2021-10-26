import http

from flask import Blueprint, jsonify

from app.orm.models.product.category_model import CategoryModel
from app.orm.models.product.product_model import ProductModel
from app.orm.repository import product_repository
from app.orm.repository import category_repository
from app.orm.schemas.response.product.category_response import CategorySchema
from app.orm.schemas.response.product.product_response import ProductSchema, ProductResponseSchema

category_blueprint = Blueprint('category_blueprint', __name__, url_prefix="/categories")

@category_blueprint.route('/<int:id>/products')
def find_all_products(id: int):
    products: list[ProductModel] = product_repository.products_in_category(id)
    return jsonify([ProductSchema.from_orm(product).dict() for product in products]), http.HTTPStatus.OK


@category_blueprint.route('')
def find_all():
    categories: list[CategoryModel] = category_repository.find_all()
    return jsonify([CategorySchema.from_orm(category).dict() for category in categories]), http.HTTPStatus.OK

# TODO: добавить пагинацию