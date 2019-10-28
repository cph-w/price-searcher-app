from price_searcher_app.utils import log_time
from price_searcher_app.products import load, store

HOSTED_JSON_URL = 'https://s3-eu-west-1.amazonaws.com/pricesearcher-code-tests/python-software-developer/products.json'  # noqa: E501
LOCAL_CSV_GZIP_PATH = 'files/products.csv.gz'


@log_time
def load_products_from_remote_json() -> None:
    raw_products = load.get_remote_file_json(HOSTED_JSON_URL)
    products = load.load_raw_products(raw_products)
    store.store_products(products)


@log_time
def load_products_from_local_csv_gzip() -> None:
    file_ = load.open_local_gzip(LOCAL_CSV_GZIP_PATH)
    raw_products = load.csv_to_dicts(file_)
    products = load.load_raw_products(raw_products)
    store.store_products(products)


def load_data_sources():
    load_products_from_remote_json()
    load_products_from_local_csv_gzip()
    store.sort_stored_products()
