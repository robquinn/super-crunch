#!/bin/sh

gcloud functions deploy $CLOUD_FUNCTIONS_FN_NAME_CLOSED \
    --gen2 \
    --runtime=$CLOUD_FUNCTIONS_RUNTIME \
    --region=$CLOUD_FUNCTIONS_REGION \
    --source=$CLOUD_FUNCTIONS_SOURCE \
    --entry-point=$CLOUD_FUNCTIONS_ENTRY_POINT_CLOSED \
    --trigger-topic=$PUBSUB_TOPIC_NAME \
    --memory=$CLOUD_FUNCTIONS_MEMORY

gcloud functions deploy $CLOUD_FUNCTIONS_FN_NAME_PENDING \
    --gen2 \
    --runtime=$CLOUD_FUNCTIONS_RUNTIME \
    --region=$CLOUD_FUNCTIONS_REGION \
    --source=$CLOUD_FUNCTIONS_SOURCE \
    --entry-point=$CLOUD_FUNCTIONS_ENTRY_POINT_PENDING \
    --trigger-topic=$PUBSUB_TOPIC_NAME \
    --memory=$CLOUD_FUNCTIONS_MEMORY

gcloud functions deploy $CLOUD_FUNCTIONS_FN_NAME_OFFICE \
    --gen2 \
    --runtime=$CLOUD_FUNCTIONS_RUNTIME \
    --region=$CLOUD_FUNCTIONS_REGION \
    --source=$CLOUD_FUNCTIONS_SOURCE \
    --entry-point=$CLOUD_FUNCTIONS_ENTRY_POINT_OFFICE \
    --trigger-topic=$PUBSUB_TOPIC_NAME \
    --memory=$CLOUD_FUNCTIONS_MEMORY

gcloud functions deploy $CLOUD_FUNCTIONS_FN_NAME_FORECAST \
    --gen2 \
    --runtime=$CLOUD_FUNCTIONS_RUNTIME \
    --region=$CLOUD_FUNCTIONS_REGION \
    --source=$CLOUD_FUNCTIONS_SOURCE \
    --entry-point=$CLOUD_FUNCTIONS_ENTRY_POINT_FORECAST \
    --trigger-topic=$PUBSUB_TOPIC_NAME \
    --memory=$CLOUD_FUNCTIONS_MEMORY
