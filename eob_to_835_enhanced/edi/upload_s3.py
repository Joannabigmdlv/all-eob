
import boto3
import os

def upload_edi_to_s3(file_path, file_name):
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
    )
    bucket = os.getenv("S3_BUCKET_NAME")
    s3.upload_file(file_path, bucket, file_name)
    return f"s3://{bucket}/{file_name}"
