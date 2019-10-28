from flask import Flask

from price_searcher_app import setup
from price_searcher_app.blueprints.products_api import products_api


def create_app() -> Flask:
    app = Flask(__name__, static_url_path='/')
    app.register_blueprint(products_api)
    setup.load_data_sources()
    return app
