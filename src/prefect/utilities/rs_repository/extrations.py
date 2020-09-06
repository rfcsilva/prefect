from prefect.utilities.storage import my_ip
from prefect.utilities.rs_repository.search import BandDoesNotExist


def band_path(product_json, band_nr) -> str:
    try:
        band = next(filter(lambda band_info: band_info['band'] == band_nr, product_json["data"]["imagery"]))
        return band['url']
    except StopIteration:
        raise BandDoesNotExist() from None


def is_local(product_json, band_nr) -> bool:
    return band_path(product_json, band_nr).startswith(my_ip())


class ProductDoesNotHaveCoordinates(Exception):
    def __init__(self):
        self.message = "Product does not have coordinates associated"
