import http

from flask import Blueprint, jsonify

product_blueprint = Blueprint('product_blueprint', __name__, url_prefix="/goods")

@product_blueprint.route('')
def hello():
    return jsonify({"message":"Hello!"}), http.HTTPStatus.OK