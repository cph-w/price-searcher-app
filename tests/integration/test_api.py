import json

from price_searcher_app.products import store
from tests import factories


def test_get_product_by_id(flask_app):
    # arrange
    product_id = 'product_1'
    product = factories.ProductFactory(id=product_id)
    store.product_records = [product]

    # act
    received_product = flask_app.test_client().get(
        f'/api/products/{product_id}'
    )

    # assert
    assert product == json.loads(received_product.data)


def test_get_product_by_id_only_gets_desired(flask_app):
    # arrange
    products = [factories.ProductFactory() for _ in range(10)]
    store.product_records = products

    # act
    received_product = flask_app.test_client().get(
        f'/api/products/{products[6]["id"]}'
    )

    # assert
    assert products[6] == json.loads(received_product.data)
