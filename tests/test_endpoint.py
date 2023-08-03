import os
import re

import pytest

from super_crunch.utils.endpoint import get_endpoint


@pytest.mark.parametrize(
    "endpoint",
    [
        (os.environ.get("API_ENDPOINT_CLOSED")),
        (os.environ.get("API_ENDPOINT_PENDING")),
        (os.environ.get("API_ENDPOINT_OFFICE")),
        (os.environ.get("API_ENDPOINT_FORECAST")),
    ],
)
def test_pending_endpoint(endpoint):
    api_response = get_endpoint(endpoint=endpoint)
    response_value = api_response.getvalue()
    assert len(response_value) > 0
    assert len(re.findall(",", response_value)) > 0
