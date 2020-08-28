from prefect import config
from prefect.utilities import my_ip
from prefect.utilities.rs_repository.search import BandDoesNotExist


def band_path(product_json, band_nr) -> str:
    try:
        band = next(filter(lambda band_info: band_info['band'] == band_nr, product_json["data"]["imagery"]))
        return band['url']
    except StopIteration:
        raise BandDoesNotExist() from None


def is_local(product_json, band_nr) -> bool:
    return band_path(product_json, band_nr).startswith(my_ip)


def select_worker(product_json, band_nr) -> dict:
    owner_ip = f"tcp://{band_path(product_json=product_json, band_nr=band_nr).split('/', 1)[0]}:{config.dask.worker_port}"
    return {'workers': owner_ip}


class ProductDoesNotHaveCoordinates(Exception):
    def __init__(self):
        self.message = "Product does not have coordinates associated"
