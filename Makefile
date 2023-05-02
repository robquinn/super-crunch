#!make

SH=sh

# Directories
S=scripts
S_FF=${S}/functions-framework
S_GCP=${S}/google-cloud
S_GCP_CRONJOB=${S_GCP}/cronjob
S_GCP_EM=${S_GCP}/emulators
S_GCP_EM_PUBSUB=${S_GCP_EM}/pubsub
S_GCP_PUBSUB=${S_GCP}/pubsub
S_GCP_FUNCTIONS=${S_GCP}/functions
S_ENV=${S}/env
S_TEST=${S}/tests
TESTS=tests

# Load Environment Variables
include .env
export $(shell sed 's/=.*//' .env)

.PHONY: all

ff_start: # Start Functions Framework for Testing
	$(SH) ${PWD}/${S_FF}/start.sh
gcp_cronjob_create: # Create Job in Google Cloud Platform "Scheduler"
	$(SH) ${PWD}/${S_GCP_CRONJOB}/create.sh
gcp_cronjob_edit: # Edit Scheduler Job in Google Cloud Platform
	$(SH) ${PWD}/${S_GCP_CRONJOB}/edit.sh
gcp_cronjob_delete: # Delete Scheduler Job in Google Cloud Platform
	$(SH) ${PWD}/${S_GCP_CRONJOB}/delete.sh
gcp_em_pubsub_start: # Start the PubSub Emulator
	$(SH) ${PWD}/${S_GCP_EM_PUBSUB}/start.sh
gcp_em_pubsub_create_topic: # Create a PubSub Topic in the PubSub Emulator
	$(SH) ${PWD}/${S_GCP_EM_PUBSUB}/create_topic.sh
gcp_em_pubsub_create_sub: # Create a PubSub Scription in the PubSub Emulator
	$(SH) ${PWD}/${S_GCP_EM_PUBSUB}/create_subscription.sh
gcp_em_pubsub_publish_topic: # Publish a PubSub Topic in the PubSub Emulator
	$(SH) ${PWD}/${S_GCP_EM_PUBSUB}/publish_topic.sh
gcp_em_pubsub_env_init: # Print the Commands Required to Export PubSub Emulator's Env Variables
	$(SH) ${PWD}/${S_GCP_EM_PUBSUB}/env_init.sh
gcp_pubsub_create: # Create the PubSub in Google Cloud Platform
	$(SH) ${PWD}/${S_GCP_PUBSUB}/create.sh
gcp_pubsub_delete: # Delte the PubSub in Google Cloud Platform
	$(SH) ${PWD}/${S_GCP_PUBSUB}/delete.sh
gcp_functions_publish: # Publish the Function to Google Cloud Platform
	$(SH) ${PWD}/${S_GCP_FUNCTIONS}/publish.sh
gcp_functions_delete:# Delete the Function in Google Cloud Platform
	$(SH) ${PWD}/${S_GCP_FUNCTIONS}/delete.sh
env_example: # Create the ".env.example" File
	$(SH) ${PWD}/${S_ENV}/example.sh
isort: # isort - fix python files
	isort ${PWD}/**/*.py
test: # Pytest - run all tests
	py.test ${PWD}/${TESTS}/ -W ignore::DeprecationWarning
test_endpoint: # Pytest - test retriving csv data from endpoint
	py.test ${PWD}/${TESTS}/test_endpoint.py
test_transactions: # Pytest - test transforming transaction data
	py.test ${PWD}/${TESTS}/test_transactions.py
test_upload: # Pytest - test uploading transactions
	py.test ${PWD}/${TESTS}/test_upload.py -W ignore::DeprecationWarning
test_env_vars: # Test Environment Variables
	$(SH) ${PWD}/${S_TESTS}/env.sh
