import os

import pytest
from google.cloud import bigquery

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
            dataset_ref.table(os.environ.get("BIGQUERY_CLOSED_TABLE_ID")),
            "closed",
        ),
        (
            os.environ.get("API_ENDPOINT_PENDING"),
            dataset_ref.table(os.environ.get("BIGQUERY_PENDING_TABLE_ID")),
            "pending",
        ),
    ],
)
def test_upload(endpoint, table_ref, type, caplog):
    upload_transactions(
        endpoint=endpoint,
        table_ref=table_ref,
        type=type,
    )
    assert f"Records uploaded in {table_ref.table_id}." in caplog.text
