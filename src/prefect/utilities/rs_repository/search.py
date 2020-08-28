import requests

from prefect import config


def product_info(product_id):
    r = requests.get(f"{config.api}/products/{product_id}")
    if r.status_code == 404:
        raise ProductDoesNotExist()
    else:
        return r.json()


def query(product_query, page=0, page_size=100):
    params = {"page": page, "pageSize": page_size}
    r = requests.post(f"{config.api}/products/query", params=params, json=product_query)
    return r.json()['content']


class ProductDoesNotExist(Exception):
    def __init__(self):
        self.message = "Product does not exist"


class BandDoesNotExist(Exception):
    def __init__(self):
        self.message = "Band does not exist"
