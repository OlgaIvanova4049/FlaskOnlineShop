from flask import Blueprint
from app.worker.tasks.example import send_request

import_blueprint = Blueprint('import_blueprint', __name__, url_prefix="/import")


@import_blueprint.route('/<id>')
def import_add(id):
    send_request(id)
    return 'OK'
