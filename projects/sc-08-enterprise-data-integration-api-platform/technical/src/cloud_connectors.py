import boto3
from azure.storage.blob import BlobServiceClient

def s3_client():
    return boto3.client("s3")

def azure_blob(connection_string: str):
    return BlobServiceClient.from_connection_string(connection_string)
