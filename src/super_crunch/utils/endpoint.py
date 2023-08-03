from io import StringIO

import requests

from .. import logger


def get_endpoint(endpoint: str) -> StringIO:
    logger.info(f"Trying API Endpoint: {endpoint}")
    try:
        response = requests.get(endpoint, timeout=None, verify=False)
        logger.info("Successful Retrieval at API Endpoint")
        response_text = StringIO(response.text)
        return response_text
    except requests.exceptions.ReadTimeout as err:
        logger.error(f"Error at API Endpoint: {err}")
        raise err
