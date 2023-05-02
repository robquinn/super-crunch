#!/bin/sh

gcloud beta emulators pubsub start \
    --project=$PUBSUB_EMULATOR_PROJECT_ID \
    --host-port=localhost:8085
