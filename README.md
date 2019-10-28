# Price Searcher Test App

Test application for qeurying product data from local gzip csv and remote s3 json.

## Installing the environment

Run `pipenv install` to install all requirements. I used python3.7 so I recommend using this version of python, but it may work with other python versions.

## Running the app

If you have make, run `make run`. See the [Makefile](Makefile) for more details of how running the environment is customisable.

## Running the tests

If you have make, run `make test`. Else run `pipenv run pytest tests/`.

## Endpoints

#### /api/products

Get products paginated. The products are stored in order of cheapest to most expensive, so this will return the cheapest products first.

```
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
```


#### /api/products/{id}

Get a single product by it's ID

```
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
```
