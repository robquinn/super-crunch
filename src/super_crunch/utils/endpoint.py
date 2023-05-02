from io import StringIO

import requests

from .. import logger


def get_endpoint(endpoint: str) -> StringIO:
    logger.info(f"Trying API Endpoint: {endpoint}")
    try:
        response = requests.get(endpoint, timeout=None)
    except requests.exceptions.ReadTimeout as err:
        return logger.error(f"Error at API Endpoint: {err}")
    logger.info("Successful retrieval at API Endpoint")
    response_text = StringIO(response.text)
    return response_text
