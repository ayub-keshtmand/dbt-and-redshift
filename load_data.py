import os
import boto3
from botocore.exceptions import ClientError
from logs.setup_logging import setup_logging


logger = setup_logging(__name__)
REGION = "eu-west-2"
BUCKET = REGION + "-dbt-and-redshift"
FILENAME = "data.csv"
FILEPATH = os.path.join(".", "data", FILENAME)


def create_s3_client():
    s3_client = boto3.client("s3", region_name=REGION)
    logger.info("Created S3 client")
    return s3_client
    

def create_bucket(s3_client):
    try:
        logger.info(f"Creating S3 bucket: {BUCKET}")
        location = {'LocationConstraint': REGION}
        s3_client.create_bucket(Bucket=BUCKET, ACL="public-read-write", CreateBucketConfiguration=location)
        logger.info(f"Created S3 bucket: {BUCKET}")
    except ClientError as e:
        logger.error(e)


def upload_file(s3_client):
    try:
        s3_client.upload_file(Filename=FILEPATH, Bucket=BUCKET, Key=FILENAME)
        logger.info(f"Uploaded {FILEPATH} to {BUCKET}")
    except ClientError as e:
        logger.error(e)


def load_data():
    s3_client = create_s3_client()
    create_bucket(s3_client)
    upload_file(s3_client)
