import os
from typing import Literal

from google.cloud import bigquery
from google.cloud.bigquery.table import TableReference

from .. import logger
from .endpoint import get_endpoint
from .transactions import Transactions


def upload_transactions(
    endpoint: str, table_ref: TableReference, type: Literal["closed", "pending"]
) -> None:
    api_response = get_endpoint(endpoint=endpoint)
    transactions = Transactions(api_response=api_response, type=type)
    transactions.change_column_names()
    transactions.cast_columns()
    transactions.transform_columns()

    job_config = bigquery.LoadJobConfig()
    job_config.write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE

    logger.info("Attempting Connection to...")
    logger.info(f"Project: {table_ref.project}")
    logger.info(f"Dataset ID: {table_ref.dataset_id}")
    logger.info(f"Table ID: {table_ref.table_id}")

    client = bigquery.Client(project=os.environ.get("GOOGLE_CLOUD_PROJECT_ID"))

    job = client.load_table_from_dataframe(
        dataframe=transactions.get_dataframe(),
        destination=table_ref,
        location="US",
        job_config=job_config,
    )
    job.result()  # Waits for table load to complete.
    logger.info(
        "Loaded {} rows into {}:{}.".format(
            job.output_rows, table_ref.dataset_id, table_ref.table_id
        )
    )
    logger.info(f"{len(transactions)} Records uploaded in {table_ref.table_id}.")
