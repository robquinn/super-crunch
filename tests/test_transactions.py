import os

import pandas as pd
import pytest

from super_crunch.constants import CLOSED, FORECAST, OFFICE, PENDING
from super_crunch.utils.columns import Columns
from super_crunch.utils.endpoint import get_endpoint
from super_crunch.utils.fields import Fields
from super_crunch.utils.transactions import Transactions


@pytest.mark.parametrize(
    "endpoint,type",
    [
        (os.environ.get("API_ENDPOINT_CLOSED"), CLOSED),
        (os.environ.get("API_ENDPOINT_PENDING"), PENDING),
        (os.environ.get("API_ENDPOINT_OFFICE"), OFFICE),
        (os.environ.get("API_ENDPOINT_FORECAST"), FORECAST),
    ],
)
def test_transactions(endpoint, type):
    api_response = get_endpoint(endpoint=endpoint)

    cols = Columns(type=type)

    fields = Fields(
        {
            "numeric": cols.numeric(),
            "date": cols.date(),
            "json": cols.json(),
            "string": cols.string(),
            "boolean": cols.boolean(),
            "office": cols.office(),
        }
    )
    transactions = Transactions(api_response=api_response, fields=fields, type=type)
    transactions.change_column_names()
    transactions.cast_columns()
    transactions.transform_columns()
    df = transactions.get_dataframe()
    if type == PENDING or type == CLOSED:
        assert isinstance(df, pd.DataFrame)
        assert len(df.columns) == 55
    elif type == OFFICE:
        assert isinstance(df, pd.DataFrame)
        assert len(df.columns) == 17
    elif type == FORECAST:
        assert isinstance(df, pd.DataFrame)
        assert len(df.columns) == 16
