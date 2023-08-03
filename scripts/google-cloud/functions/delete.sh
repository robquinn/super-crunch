#!/bin/sh

gcloud functions delete $CLOUD_FUNCTIONS_FN_NAME_CLOSED
gcloud functions delete $CLOUD_FUNCTIONS_FN_NAME_PENDING
gcloud functions delete $CLOUD_FUNCTIONS_FN_NAME_OFFICE
gcloud functions delete $CLOUD_FUNCTIONS_FN_NAME_FORECAST
