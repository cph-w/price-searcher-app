from typing import Tuple

import logging

from flask import Response, jsonify, request

from . import store, schemas


def get_product_by_id(product_id) -> Tuple[Response, int]:
    """ Return a product as requested by ID """
    try:
        product = store.get_product_by_id(product_id)
        if not product:
            return jsonify({'error': f'product {product_id} not found'}), 404
        response_data = schemas.ProductSchema().dump(product)
        return jsonify(response_data), 200
    except Exception as e:
        logging.error(e)
        return jsonify(
            {
                'error': f'Internal Server Error retrieving '
                         f'product with id: {product_id}'
            }
        ), 500


def get_products() -> Tuple[Response, int]:
    try:
        pagination = schemas.ProductsRequestSchema().load(request.args)
        products, total_records = store.get_products(**pagination)
        response_data = schemas.ProductsResponseSchema().dump(
            {
                'data': products,
                'page': pagination['page'],
                'page_size': pagination['page_size'],
                'total_records': total_records
            }
        )
        return response_data
    except Exception as e:
        logging.error(e)
        return jsonify(
            {
                'error': 'Internal Server Error'
            }
        ), 500
