import pytest

from marshmallow import ValidationError

from price_searcher_app.products import schemas
from tests import factories


def test_product_load_schema():
    # arrange
    raw_product = factories.RawProductFactory()

    # act
    loaded = schemas.ProductSchema().load(raw_product)

    # assert
    assert loaded == {
        'id': raw_product['id'],
        'name': raw_product['name'],
        'brand': raw_product['brand'],
        'retailer': raw_product['retailer'],
        'price': raw_product['price'],
        'in_stock': raw_product['in_stock'] in ('y', 'yes', 'true', True)
    }


def test_product_load_schema_accepts_empty_string_for_fields():
    # arrange
    raw_product = factories.RawProductFactory(
        name='',
        brand='',
        retailer='',
        price=''
    )

    # act
    loaded = schemas.ProductSchema().load(raw_product)

    # assert
    assert loaded == {
        'id': raw_product['id'],
        'name': None,
        'brand': None,
        'retailer': None,
        'price': None,
        'in_stock': raw_product['in_stock'] in ('y', 'yes', 'true', True)
    }


def test_product_load_schema_sets_none_for_missing():
    # arrange
    raw_product = {'id': 'onlySetField'}

    # act
    loaded = schemas.ProductSchema().load(raw_product)

    # assert
    assert loaded == {
        'id': raw_product['id'],
        'name': None,
        'brand': None,
        'retailer': None,
        'price': None,
        'in_stock': None
    }


def test_products_response_schema():
    # arrange
    product_response = {
        'page': 1,
        'page_size': 10,
        'data': [factories.ProductFactory()],
        'total_records': 1
    }

    # act
    dumped = schemas.ProductsResponseSchema().dump(product_response)

    # assert
    assert dumped == product_response


def test_products_request_schema():
    # arrange
    page = 5
    page_size = 10
    args_dict = {
        'page': page,
        'page_size': page_size
    }

    # act
    loaded = schemas.ProductsRequestSchema().load(args_dict)

    # assert
    assert loaded['page'] == 5
    assert loaded['page_size'] == page_size


@pytest.mark.parametrize('field_for_negative', ('page', 'page_size'))
def test_products_request_schema_raises_for_invalid(field_for_negative):
    # arrange
    args_dict = {
        'page': 5,
        'page_size': 10
    }
    args_dict[field_for_negative] = -1

    # act & assert
    with pytest.raises(ValidationError):
        schemas.ProductsRequestSchema().load(args_dict)
