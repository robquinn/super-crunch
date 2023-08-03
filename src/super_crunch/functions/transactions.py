import os

from google.cloud import bigquery

from .. import logger
from ..constants import CLOSED, FORECAST, OFFICE, PENDING
from ..utils.upload import upload_transactions


def transactions_closed(event, context):
    logger.info(f"Retrieved Event Id: {context.event_id}")

    dataset_ref = bigquery.DatasetReference(
        project=os.environ.get("GOOGLE_CLOUD_PROJECT_ID"),
        dataset_id=os.environ.get("BIGQUERY_TRANSACTIONS_DATASET_ID"),
    )

    closed_api_endpoint = str(os.environ.get("API_ENDPOINT_CLOSED"))
    closed_table_ref = dataset_ref.table(
        str(os.environ.get("BIGQUERY_CLOSED_TABLE_ID"))
    )

    upload_transactions(
        endpoint=closed_api_endpoint,
        table_ref=closed_table_ref,
        type=CLOSED,
    )


def transactions_pending(event, context):
    logger.info(f"Retrieved Event Id: {context.event_id}")

    dataset_ref = bigquery.DatasetReference(
        project=os.environ.get("GOOGLE_CLOUD_PROJECT_ID"),
        dataset_id=os.environ.get("BIGQUERY_TRANSACTIONS_DATASET_ID"),
    )

    pending_api_endpoint = str(os.environ.get("API_ENDPOINT_PENDING"))
    pending_table_ref = dataset_ref.table(
        str(os.environ.get("BIGQUERY_PENDING_TABLE_ID"))
    )

    upload_transactions(
        endpoint=pending_api_endpoint,
        table_ref=pending_table_ref,
        type=PENDING,
    )


def transactions_office(event, context):
    logger.info(f"Retrieved Event Id: {context.event_id}")

    dataset_ref = bigquery.DatasetReference(
        project=os.environ.get("GOOGLE_CLOUD_PROJECT_ID"),
        dataset_id=os.environ.get("BIGQUERY_TRANSACTIONS_DATASET_ID"),
    )

    office_api_endpoint = str(os.environ.get("API_ENDPOINT_OFFICE"))
    office_table_ref = dataset_ref.table(
        str(os.environ.get("BIGQUERY_OFFICE_TABLE_ID"))
    )

    upload_transactions(
        endpoint=office_api_endpoint,
        table_ref=office_table_ref,
        type=OFFICE,
    )


def transactions_forecast(event, context):
    logger.info(f"Retrieved Event Id: {context.event_id}")

    dataset_ref = bigquery.DatasetReference(
        project=os.environ.get("GOOGLE_CLOUD_PROJECT_ID"),
        dataset_id=os.environ.get("BIGQUERY_TRANSACTIONS_DATASET_ID"),
    )

    forecast_api_endpoint = str(os.environ.get("API_ENDPOINT_FORECAST"))
    forecast_table_ref = dataset_ref.table(
        str(os.environ.get("BIGQUERY_FORECAST_TABLE_ID"))
    )

    upload_transactions(
        endpoint=forecast_api_endpoint,
        table_ref=forecast_table_ref,
        type=FORECAST,
    )
