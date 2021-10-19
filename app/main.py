from flask import Flask

from app.core.extensions import db


def create_app():
    app = Flask(__name__)
    register_extensions(app)
    register_views(app)
    return app

def register_extensions(app):
    db.init_app(app)

def register_views(app):
    from app.api.views.product_view import product_blueprint
    app.register_blueprint(product_blueprint)
