import json

from app.exceptions.exceptions import NotFoundException


def register_exceptions(app):
    @app.errorhandler(NotFoundException)
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