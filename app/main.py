from flask import Flask

from app.core.extensions import db
from app.core.settings import settings
from app.exceptions.handler import register_exceptions


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(settings.get_original_env())
    register_extensions(app)
    register_exceptions(app)
    register_views(app)
    return app

def register_extensions(app):
    db.init_app(app)

def register_views(app):
    from app.api.views.product_view import product_blueprint
    from app.api.views.user_view import user_blueprint
    from app.api.views.category_view import category_blueprint
    from app.api.views.import_view import import_blueprint
    from app.api.views.security.auth_view import auth_blueprint
    app.register_blueprint(category_blueprint)
    app.register_blueprint(product_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(import_blueprint)
    app.register_blueprint(auth_blueprint)

    #TODO: настроить volumes




