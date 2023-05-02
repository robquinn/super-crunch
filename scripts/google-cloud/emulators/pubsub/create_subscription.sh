#!/bin/sh

python dev/subscriber.py $PUBSUB_EMULATOR_PROJECT_ID create-push $PUBSUB_EMULATOR_TOPIC_ID $PUBSUB_EMULATOR_SUBSCRIPTION_ID http://localhost:8080
