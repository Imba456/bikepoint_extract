from dotenv import load_dotenv
import os
import json
import boto3
import logging

load_dotenv()

#check environment variables
aws_access_key = os.getenv('aws_access_key')
aws_secret = os.getenv('aws_secret')
s3_bucket = os.getenv('s3_bucket')

#initial check with hardcoded test files
test_file = '2026-11-11 15-31-08.json'
file_location = 'data/2026-11-11 15-31-08.json'

#setup s3 client
s3_client = boto3.client(
    's3'
    ,aws_access_key_id = aws_access_key
    ,aws_secret_access_key = aws_secret
)
#upload to s3
s3_client.upload_file(
    file_location #local location
    ,s3_bucket #the bucket
    ,test_file #name of the file
)
