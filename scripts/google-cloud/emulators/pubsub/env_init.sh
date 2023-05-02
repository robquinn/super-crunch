#!/bin/sh

echo "export $(gcloud beta emulators pubsub env-init --format 'config' | sed "s/ //g")"

# export PUBSUB_EMULATOR_HOST=localhost:8085
