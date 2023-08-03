import os

import pytest
from google.cloud import bigquery

from super_crunch.constants import CLOSED, FORECAST, OFFICE, PENDING
from super_crunch.utils.upload import upload_transactions

dataset_ref = bigquery.DatasetReference(
    project=os.environ.get("GOOGLE_CLOUD_PROJECT_ID"),
    dataset_id=os.environ.get("BIGQUERY_TRANSACTIONS_DATASET_ID"),
)


@pytest.mark.parametrize(
    "endpoint,table_ref,type",
    [
        (
            os.environ.get("API_ENDPOINT_CLOSED"),
            dataset_ref.table(str(os.environ.get("BIGQUERY_CLOSED_TABLE_ID"))),
            CLOSED,
        ),
        (
            os.environ.get("API_ENDPOINT_PENDING"),
            dataset_ref.table(str(os.environ.get("BIGQUERY_PENDING_TABLE_ID"))),
            PENDING,
        ),
        (
            os.environ.get("API_ENDPOINT_OFFICE"),
            dataset_ref.table(str(os.environ.get("BIGQUERY_OFFICE_TABLE_ID"))),
            OFFICE,
        ),
        (
            os.environ.get("API_ENDPOINT_FORECAST"),
            dataset_ref.table(str(os.environ.get("BIGQUERY_FORECAST_TABLE_ID"))),
            FORECAST,
        ),
    ],
)
def test_upload(endpoint, table_ref, type, caplog):
    upload_transactions(
        endpoint=endpoint,
        table_ref=table_ref,
        type=type,
    )
    assert (
        f"Records Uploaded Into {table_ref.dataset_id}:{table_ref.table_id}."
        in caplog.text
    )
