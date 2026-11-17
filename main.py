from datetime import datetime
from modules.extract_function import extract_from_bikepoint
import logging
import os

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

logger.info('logger closed')