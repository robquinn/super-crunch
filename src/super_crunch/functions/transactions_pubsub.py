import os

from google.cloud import bigquery

from .. import logger
from ..utils.upload import upload_transactions


def transactions_pubsub(event, context):
    logger.info(f"Retrieved Event Id: {context.event_id}")
    dataset_ref = bigquery.DatasetReference(
        project=os.environ.get("GOOGLE_CLOUD_PROJECT_ID"),
        dataset_id=os.environ.get("BIGQUERY_TRANSACTIONS_DATASET_ID"),
    )
    closed_api_endpoint = os.environ.get("API_ENDPOINT_CLOSED")
    closed_table_ref = dataset_ref.table(os.environ.get("BIGQUERY_CLOSED_TABLE_ID"))
    pending_api_endpoint = os.environ.get("API_ENDPOINT_PENDING")
    pending_table_ref = dataset_ref.table(os.environ.get("BIGQUERY_PENDING_TABLE_ID"))

    upload_transactions(
        endpoint=closed_api_endpoint,
        table_ref=closed_table_ref,
        type="closed",
    )
    upload_transactions(
        endpoint=pending_api_endpoint,
        table_ref=pending_table_ref,
        type="pending",
    )
