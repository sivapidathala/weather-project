import json
from datetime import datetime
import boto3
from botocore.exceptions import NoCredentialsError, ClientError

from .config import (
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    AWS_REGION,
    S3_BUCKET_NAME
)

def get_s3_client():
    """Create S3 client with credentials."""
    return boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION
    )

def upload_to_s3(data):
    """Upload weather data JSON file to S3."""
    s3 = get_s3_client()

    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    file_name = f"weather_data_{timestamp}.json"

    try:
        s3.put_object(
            Bucket=S3_BUCKET_NAME,
            Key=file_name,
            Body=json.dumps(data),
            ContentType="application/json"
        )
        print(f"Uploaded to S3: {file_name}")
        return file_name

    except (NoCredentialsError, ClientError) as e:
        print("S3 Upload Failed:", e)
        return None
