import json
from werkzeug.exceptions import HTTPException

from app.exceptions.exceptions import UserNotFoundException


def register_exceptions(app):
    @app.errorhandler(UserNotFoundException)
    def handle_exception(e):
        response = e.get_response()
        response.data = json.dumps({
            "code": e.code,
            "name": e.name,
            "description": e.description,
        })
        response.content_type = "application/json"
        return response

    app.register_error_handler(400, handle_exception)