#!/bin/sh

gcloud functions deploy $CLOUD_FUNCTIONS_FN_NAME \
    --gen2 \
    --runtime=$CLOUD_FUNCTIONS_RUNTIME \
    --region=$CLOUD_FUNCTIONS_REGION \
    --source=$CLOUD_FUNCTIONS_SOURCE \
    --entry-point=$CLOUD_FUNCTIONS_ENTRY_POINT \
    --trigger-topic=$PUBSUB_TOPIC_NAME \
    --memory=$CLOUD_FUNCTIONS_MEMORY
