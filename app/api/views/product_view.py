import http
import json

from flask import Blueprint, request, jsonify

from app.orm.models.product.product_model import ProductModel
from app.orm.repository import product_repository
from app.orm.schemas.query.product.product_query import ProductQueryParam
from app.orm.schemas.response.product.product_response import ProductSchema, ProductResponseSchema, Paginator

product_blueprint = Blueprint('product_blueprint', __name__, url_prefix="/products")


@product_blueprint.route('')
def find_all():
    query_param: ProductQueryParam = ProductQueryParam.as_obj(request.args.to_dict(flat=True))
    products: list[ProductModel] = product_repository.filtered_sorted_product_list(query_param)
    paginator = query_param.paginator.copy(update={"total": product_repository.count()})
    return ProductResponseSchema(items=[ProductSchema.from_orm(product).dict() for product in products], paginator=paginator).dict(), http.HTTPStatus.OK
