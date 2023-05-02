import os

import pandas as pd
import pytest

from super_crunch.utils.endpoint import get_endpoint
from super_crunch.utils.transactions import Transactions


@pytest.mark.parametrize(
    "endpoint,type",
    [
        (os.environ.get("API_ENDPOINT_CLOSED"), "closed"),
        (os.environ.get("API_ENDPOINT_PENDING"), "pending"),
    ],
)
def test_transactions(endpoint, type):
    api_response = get_endpoint(endpoint=endpoint)
    transactions = Transactions(api_response=api_response, type=type)
    transactions.change_column_names()
    transactions.cast_columns()
    transactions.transform_columns()
    df = transactions.get_dataframe()
    assert isinstance(df, pd.DataFrame)
    assert len(df.columns) == 55
