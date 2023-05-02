#!/bin/sh

gcloud scheduler jobs create pubsub $SCHEDULER_JOB_NAME \
    --location=$SCHEDULER_LOCATION \
    --schedule=$SCHEDULER_SCHEDULE \
    --topic=$PUBSUB_TOPIC_NAME \
    --message-body=$SCHEDULER_MESSAGE_BODY \
    --time-zone=$SCHEDULER_TIME_ZONE
