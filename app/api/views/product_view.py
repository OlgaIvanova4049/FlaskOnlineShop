import http
import json

from flask import Blueprint, request, jsonify

from app.orm.models.product.product_model import ProductModel
from app.orm.repository import product_repository, user_repository
from app.orm.schemas.query.product.product_query import ProductQueryParam
from app.orm.schemas.response.product.product_response import ProductSchema

product_blueprint = Blueprint('product_blueprint', __name__, url_prefix="/goods")


@product_blueprint.route('')
def hello():
    query_param = ProductQueryParam.as_obj(request.args.to_dict(flat=True))
    products: list[ProductModel] = product_repository.filtered_sorted_product_list(query_param)
    return jsonify([ProductSchema.from_orm(product).dict() for product in products]), http.HTTPStatus.OK