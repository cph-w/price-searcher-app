from typing import Any, Dict, Iterable, List, TextIO

import csv
import gzip
import logging
import requests

from . import schemas

logger = logging.getLogger(__name__)


def open_local_gzip(path: str) -> TextIO:
    return gzip.open(path, 'rt')


def csv_to_dicts(file_: TextIO) -> csv.DictReader:
    raw_dicts = csv.DictReader(
        file_,
        ('id', 'name', 'brand', 'retailer', 'price', 'in_stock'),
        skipinitialspace=True
    )
    next(raw_dicts)  # skip the fieldnames row
    return raw_dicts


def get_remote_file_json(url: str) -> List[Dict[str, Any]]:
    return requests.get(url).json()


def load_raw_products(
        raw_product_dicts: Iterable[List[Dict[str, Any]]]
) -> Iterable[Dict[str, Any]]:
    """ Load raw product dicts into their a standardised and typed
    dictionary equivalent.
    """
    products = schemas.ProductSchema().load(raw_product_dicts, many=True)
    return products
