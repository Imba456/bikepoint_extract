from datetime import datetime
from modules.extract_function import extract_from_bikepoint
from modules.load_function import load_into_s3bucket
import logging
import os
from dotenv import load_dotenv

timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

log_dir = 'logs'
os.makedirs(log_dir,exist_ok=True)
log_filename = f'{log_dir}/{timestamp}.log'

logging.basicConfig(
    filename = log_filename
    ,format = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
    ,level = logging.INFO
)

logger = logging.getLogger()
logger.info('logger initialised')

data_dir = 'data'
api_endpoint = 'https://api.tfl.gov.uk/BikePoint/'

extract_result = extract_from_bikepoint(api_endpoint,data_dir,timestamp,max_attempts=2,delay=30) #you can add the argument by writing the name so the order can be different

print(extract_result)

if extract_result:
    load_dotenv()

    #check environment variables
    aws_access_key = os.getenv('aws_access_key')
    aws_secret = os.getenv('aws_secret')
    s3_bucket = os.getenv('s3_bucket')

    load_results = load_into_s3bucket(aws_access_key, aws_secret,s3_bucket,data_dir)

    print(load_results)
else:
    logger.warning(f'extract saved no data, nothing to upload')


logger.info('logger closed')