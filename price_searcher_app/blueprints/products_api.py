from typing import Tuple

from flask import Blueprint, Response

from price_searcher_app.products import api

products_api = Blueprint('products', __name__, url_prefix='/api/products')


@products_api.route('', methods=['GET'])
def products() -> Tuple[Response, int]:
    """ Get products paginated. The products are stored in order of
    cheapest to most expensive, so this will return the cheapest products
    first.

    Example requests:
        GET
            /api/products (will use default pagination, page=1, page_size=10)
            /api/products?page=5
            /api/products?page_size=15
            /api/products?page=2&page_size=20

    Example response (http 200):
        {
            "data": [
                {
                    "brand": "abbey",
                    "id": "8182756",
                    "in_stock": false,
                    "name": "mesencephalon",
                    "price": 0.1,
                    "retailer":"zymology"
                }
            ],
            "page": 1,
            "page_size": 1,
            "total_records": 500357
        }

    Example Error Response (http 500):
        {
            "error": "Internal Server Error"
        }
    """
    return api.get_products()


@products_api.route('/<product_id>', methods=['GET'])
def product(product_id: str) -> Tuple[Response, int]:
    """ Get a single product by it's ID

    Example request:
        /api/products/5860865

    Example response (http 200):
        {
            "brand": "balsamroot",
            "id": "5860865",
            "in_stock": false,
            "name": "deflorescence",
            "price": 320.0,
            "retailer": "redecline"
        }

    Example response (http 404):
        {
            "error": "product an_id_thats_not_real not found"
        }

    Example response (http 500):
        {
            "error": "Internal Server Error retrieving product with id: 12"
        }
    """
    return api.get_product_by_id(product_id)
