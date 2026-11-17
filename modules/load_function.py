from dotenv import load_dotenv
import os
import json
import boto3
import logging

#define logger filename for python file name
logger = logging.getLogger(__name__)

def load_into_s3bucket(aws_access_key: str,aws_secret:str,s3_bucket:str,data_dir:str):
    """function to upload files to s3 bucket

    Args:
        aws_access_key (str): load these in main from environment
        aws_secret (str): load these in main from environment
        s3_bucket (str): load these in main from environment
        data_dir (str): directory where data sits, will only check at folder level
    """

    logger.info('logger initialised')

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
            logger.info(f'{file} uploaded successfully')
            os.remove(to_upload)
            # logger.info('logger closed')
        except Exception as e:
            print(f'something went wrong with the upload of {file}, Error: {e}')
            logger.error(f'something went wrong with the upload of {file}, Error: {e}')

    logger.info('logger closed')


