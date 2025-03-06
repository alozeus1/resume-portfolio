import json
import boto3
import base64
import os

s3 = boto3.client('s3')
BUCKET_NAME = os.getenv("S3_BUCKET_NAME", "your-s3-bucket-name")

def lambda_handler(event, context):
    try:
        file_content = base64.b64decode(event["body"])
        file_name = event["headers"]["filename"]
        
        s3.put_object(Bucket=BUCKET_NAME, Key=file_name, Body=file_content)
        
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "File uploaded successfully!"})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }