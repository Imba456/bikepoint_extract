from dotenv import load_dotenv
import os
import json
import boto3
import logging

load_dotenv()

#to be done

#check environment variables
aws_access_key = os.getenv('aws_access_key')
aws_secret = os.getenv('aws_secret')
s3_bucket = os.getenv('s3_bucket')

#initial check with hardcoded test files before switching to dynamic listing
# test_file = '2026-11-11 15-31-08.json'
# file_location = 'data/2026-11-11 15-31-08.json'
data_dir = 'data'
file_list = os.listdir(data_dir)

#setup s3 client
s3_client = boto3.client(
    's3'
    ,aws_access_key_id = aws_access_key
    ,aws_secret_access_key = aws_secret
)

for file in file_list:
    #upload to s3
    to_upload = f'{data_dir}/{file}'
    try:
        s3_client.upload_file(
            to_upload #the file from file_location
            ,s3_bucket #the bucket
            ,file #the filename to use
        )
        print(f'{file} uploaded successfully')
        os.remove(to_upload)
    except Exception as e:
        print(f'something went wrong with the upload of {file}, Error: {e}')
