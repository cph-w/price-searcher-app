from typing import Any, Dict, List, Iterable, Optional, Tuple

ProductDict = Dict[str, Any]

# Initialise an empty list to store product records in
product_records: List[ProductDict] = []


def get_product_by_id(product_id: str) -> Optional[ProductDict]:
    product = next(
        (
            prod for prod in product_records
            if prod['id'] == product_id
        ),
        None
    )
    return product


def get_products(page, page_size) -> Tuple[List[ProductDict], int]:
    start = (page - 1) * page_size
    end = start + page_size
    number_of_records = len(product_records)

    if start > number_of_records:
        products = []
    if end > number_of_records:
        end = number_of_records
        products = product_records[start:end]
    else:
        products = product_records[start:end]

    return products, len(product_records)


def store_products(products: Iterable[ProductDict]) -> None:
    product_records.extend(products)


def sort_stored_products() -> None:
    """ Sort stored products by cheapest first,
    None (null) is assumed as high since price is not known.
    """
    product_records.sort(key=_product_price)


def _product_price(product: ProductDict) -> float:
    price = product['price']
    if price is None:
        return 1E10
    return price
