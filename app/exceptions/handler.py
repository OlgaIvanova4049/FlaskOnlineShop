import http
import json

from pydantic import ValidationError
from werkzeug.exceptions import HTTPException


def register_exceptions(app):

    @app.errorhandler(HTTPException)
    def handle_exception(e):
        response = e.get_response()
        response.data = json.dumps({
            "code": e.code,
            "name": e.name,
            "description": e.description,
        })
        response.content_type = "application/json"
        return response

    @app.errorhandler(ValidationError)
    def handle_validation_exception(e):
        data = {
            "code": 400,
            "name": "Validation error",
            "description": str(e)}
        return data, http.HTTPStatus.BAD_REQUEST
