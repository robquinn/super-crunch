#!/bin/sh

# API Endpoint to Fetch
echo ${API_ENDPOINT}

# Google Cloud Platform
echo ${GOOGLE_CLOUD_PROJECT_ID}

# BigQuery
echo ${BIGQUERY_DATASET_ID}
echo ${BIQUERY_TABLE_ID}

# Functions
echo ${CLOUD_FUNCTIONS_FN_NAME}
echo ${CLOUD_FUNCTIONS_RUNTIME}
echo ${CLOUD_FUNCTIONS_REGION}
echo ${CLOUD_FUNCTIONS_SOURCE}
echo ${CLOUD_FUNCTIONS_ENTRY_POINT}
echo ${CLOUD_FUNCTIONS_MEMORY}

# Functions Framework
echo ${FUNCTIONS_FRAMEWORK_TARGET}
echo ${FUNCTIONS_FRAMEWORK_SIGNATURE_TYPE}
echo ${FUNCTIONS_FRAMEWORK_PORT}

# PubSub
echo ${PUBSUB_TOPIC_NAME}

# PubSub Emulators
echo ${PUBSUB_EMULATOR_PROJECT_ID}

# Cron Scheduler
echo ${SCHEDULER_JOB_NAME}
echo ${SCHEDULER_LOCATION}
echo ${SCHEDULER_SCHEDULE}
echo ${SCHEDULER_MESSAGE_BODY}
echo ${SCHEDULER_TIME_ZONE}
