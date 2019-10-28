import random

from price_searcher_app.products import store
from tests import factories


def test_get_product_by_id():
    # arrange
    fake_products = [factories.ProductFactory() for _ in range(10)]
    store.product_records = fake_products

    # act
    product = store.get_product_by_id(fake_products[5]['id'])

    # assert
    assert product == fake_products[5]


def test_get_product_by_id_returns_none_if_no_match():
    # arrange
    fake_products = [factories.ProductFactory() for _ in range(10)]
    store.product_records = fake_products

    # act
    product = store.get_product_by_id('I do not exist')

    # assert
    assert product is None


def test_get_products():
    # arrange
    fake_products = [factories.ProductFactory() for _ in range(10)]
    store.product_records = fake_products

    # act
    products, total_records = store.get_products(page=1, page_size=10)

    # assert
    assert len(products) == 10
    assert total_records == 10

    assert fake_products == products


def test_get_products_pagination():
    # arrange
    fake_products = [factories.ProductFactory() for _ in range(30)]
    store.product_records = fake_products

    # act
    received_products = []
    page_size = 5
    for page in range(1, 7):
        products, total_records = store.get_products(page, page_size)
        received_products.extend(products)

    # assert
    assert len(received_products) == 30
    assert total_records == 30

    assert fake_products == received_products


def test_get_products_pagination_does_not_error_if_page_out_of_range():
    # arrange
    fake_products = [factories.ProductFactory() for _ in range(5)]
    store.product_records = fake_products

    # act
    products, total_records = store.get_products(page=2, page_size=10)

    # assert
    assert total_records == 5
    assert products == []


def test_get_products_pagination_does_not_error_if_page_bigger_than_dataset():
    # arrange
    fake_products = [factories.ProductFactory() for _ in range(5)]
    store.product_records = fake_products

    # act
    products, total_records = store.get_products(page=1, page_size=10)

    # assert
    assert total_records == 5
    assert products == fake_products


def test_sort_stored_products():
    # arrange
    fake_products = [
        factories.ProductFactory(price=float(i))
        for i in range(10)
    ]
    fake_products[-1]['price'] = None
    store.product_records = fake_products.copy()
    random.shuffle(store.product_records)

    # act
    store.sort_stored_products()

    # assert
    assert store.product_records == fake_products
