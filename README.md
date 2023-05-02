# Google Cloud PubSub Function and CronJob

## Table of Contents

- [About](#about)
- [Requirements](#requirements)
- [Install](#install)
- [Commands](#commands)
    - [Publish Cloud Function](#publish-cloud-function)
    - [Delete Cloud Function](#delete-cloud-function)
    - [Create the PubSub](#create-the-pubsub)
    - [Delete the PubSub](#delete-the-pubSub)
    - [Create the CronJob](#create-the-cronjob)
    - [Edit the CrobJob](#edit-the-cronjob)
    - [Delete the CronJob](#delete-the-cronJob)
- [Unit Testing](#unit-testing)
    - [Run All Tests](#run-all-tests)
    - [Test Endpoint](#test-endpoint)
    - [Test Transactions](#test-transactions)
    - [Test Upload](#test-upload)
- [Integration Testing](#integration-testing)

## About

This is a [Google Cloud Function](https://cloud.google.com/functions) written in python. The function is triggered by a [PubSub](https://cloud.google.com/pubsub), which in turn is triggered by a [cron job](https://en.wikipedia.org/wiki/Cron). The function retrieves data from an API endpoint that outputs a `.csv` file, then proceeds to ETL (extract, transform, and load) that data into a [BigQuery](https://cloud.google.com/bigquery) Table.

All the commands necessary to setup, configure, and deploy the function are written into the `scripts` folder and accessible by `make` commands.

## Requirements

In order to run this project, you'll need

- [make](https://www.gnu.org/software/make/)
- [python 3.11](https://www.python.org/downloads/)
- `.env` file based upon the `.env.example` file, with the values filled out
- [Google Cloud CLI (gcloud)](https://cloud.google.com/cli)
- [functions-framework for python](https://github.com/GoogleCloudPlatform/functions-framework-python)

## Install

To install ALL the necessary python packages for development:

```bash
pip install -r requirements-dev.txt
```
To install just the production python packages:

```bash
pip install -r requirements.txt
```

## Commands

### Publish Cloud Function

To publish the cloud function:

```bash
make gcp_functions_publish
```

### Delete Cloud Function

To delete the cloud function:

```bash
make gcp_functions_delete
```

### Create the PubSub

To create the PubSub that triggers the cloud function:

```bash
make gcp_pubsub_create
```
### Delete the PubSub

To delete the PubSub that triggers the cloud function:

```bash
make gcp_pubsub_delete
```

### Create the CronJob

To create the cronjob for the PubSub:

```bash
make gcp_cronjob_create
```

### Edit the CronJob

To edit the cronjob for the PubSub, edit the file:
```bash
scripts/google-cloud/cronjob/edit.sh
```
Then run the command:

```bash
make gcp_cronjob_edit
```

### Delete the CronJob

To delete the cronjob for the PubSub

```bash
make gcp_cronjob_delete
```
## Unit Testing

### Run All Tests
To run all tests
```bash
make test
```
### Test Endpoint

To test the retrieval of the api endpoint csv data:
```bash
make test_endpoint
```
### Test Transactions
To test setting up of the Pandas Dataframe and data transformations:
```bash
make test_transactions
```
### Test Upload
To test the uploading of the transaction data to the BigQuery table:
```bash
make test_upload
```
## Integration Testing

To run integrations tests, you will need 3 separate shells.

In the first shell, start the function framework:
```bash
make ff_start
```
Next, in your second shell, start the pubsub emulators:
```bash
make gcp_em_pubsub_start
```
In your third shell, run the following command:
```bash
make gcp_em_pubsub_env_init
```
The output of the command should look something like:
```bash
 export PUBSUB_EMULATOR_HOST=localhost:8085
```
Copy that output, paste it into your shell, and hit enter.

That step is important, as the next set of commands will not work without it.

Also ensure for these next steps that your `.env` file has all the variables filled out.

Then, run the following command to create a PubSub topic:
```bash
make gcp_em_pubsub_create_topic
```
Next, run the following command to create a subscription for the PubSub topic:
```bash
make gcp_em_pubsub_create_sub
```
Lastly, run the following command to publish the topic:
```bash
make gcp_em_pubsub_publish_topic
```
If you return to your first shell, you should see the output of your integration tests
