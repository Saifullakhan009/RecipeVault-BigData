import boto3
from botocore.exceptions import ClientError

# Initialize S3 client
s3 = boto3.client("s3", endpoint_url="http://localhost:4566")  # Replace with LocalStack's S3 endpoint
bucket_name = "recipe-files"

# Create the S3 bucket
def initialize_s3_bucket():
    try:
        s3.create_bucket(Bucket=bucket_name)
    except ClientError as e:
        if e.response["Error"]["Code"] != "BucketAlreadyOwnedByYou":
            raise

# Upload file to S3
def upload_to_s3(file_path, file_name):
    try:
        s3.upload_file(file_path, bucket_name, file_name)
        return f"s3://{bucket_name}/{file_name}"
    except ClientError as e:
        return f"Error uploading file: {e}"

# Download file from S3
def download_from_s3(file_name, destination_path):
    try:
        s3.download_file(bucket_name, file_name, destination_path)
    except ClientError as e:
        raise FileNotFoundError(f"Error downloading file: {e}")
