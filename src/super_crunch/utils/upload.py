import os

from google.cloud import bigquery
from google.cloud.bigquery.table import TableReference

from .. import logger
from ..constants import TRANSACTION_TYPES
from .columns import Columns
from .endpoint import get_endpoint
from .fields import Fields
from .transactions import Transactions


def upload_transactions(
    endpoint: str,
    table_ref: TableReference,
    type: TRANSACTION_TYPES,
) -> None:
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
        f"{job.output_rows} Records Uploaded Into "
        + f"{table_ref.dataset_id}:{table_ref.table_id}."
    )
