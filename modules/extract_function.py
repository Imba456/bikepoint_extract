import os
from datetime import datetime #library, allows us not having to write datetime.datetime
import requests
import json
import time
import logging

logger = logging.getLogger(__name__)

def extract_from_bikepoint(api_endpoint: str ,data_dir: str, timestamp: str, max_attempts: int, delay: int):
    """function to extract json files from an URL and save to a destionation

    Args:
        api_endpoint (str): API endpoint url
        data_dir (str): local directory name
        timestamp (str): string formatted timestamp for filename
        max_attempts (int): number+1 for how many times it can retry an API call if it errors
        delay (int): how long in seconds to wait before attempting another API call upon error
    """
    #make datadir and filename
    os.makedirs(data_dir,exist_ok=True)
    filename = f'{data_dir}/{timestamp}.json'

    attempts = 0
    # max_attempts = 2

    while attempts <= max_attempts:

        response = requests.get(api_endpoint)
        status_code = response.status_code

        if 200<=status_code<300:
            try:
                data = response.json()

                with open(filename,'w') as file:
                    json.dump(data, file) #currently no safeguarding around having no response, so files can be empty if there is no response

                print(f'file {filename} saved successfully 👍')
                logger.info(f'file {filename} saved successfully 👍')
                #flag the function that data was saved
                return True
            
            except Exception as e:
                print(f"an error occurred when saving the JSON: {e}")
                logger.error(f"an error occurred when saving the JSON: {e}")

            break

        elif 300<=status_code<500:
            print(f'API call failed, status code {status_code} 🤬')
            logger.error(f'API call failed, status code {status_code} 🤬')
            break
        else:
            if attempts==max_attempts:
                print(f'max attempts reached')
                logger.warning(f'max attempts reached')
            else:
                print(f'Attempt {attempts} failed status code {status_code}, waiting 30 seconds before the next attempt')
                logger.error(f'Attempt {attempts} failed status code {status_code}, waiting 30 seconds before the next attempt')
            attempts+=1
            time.sleep(delay)

    logger.info('logger closed')

    #return statement
    return False