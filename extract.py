import os
from datetime import datetime #library, allows us not having to write datetime.datetime
import requests
import json
import time

timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

#print(timestamp)

data_dir = 'data'
os.makedirs(data_dir,exist_ok=True)
filename = f'{data_dir}/{timestamp}.json' 

api_endpoint = 'https://api.tfl.gov.uk/BikePoint/'

attempts = 0
max_attempts = 2

while attempts <= max_attempts:

    response = requests.get(api_endpoint)
    status_code = response.status_code

    if 200<=status_code<300:
        data = response.json()

        with open(filename,'w') as file:
            json.dump(data, file) #currently no safeguarding around having no response, so files can be empty if there is no response

        print(f'file {filename} saved successfully 👍')

        break

    elif 300<=status_code<500:
        print(f'API call failed, status code {status_code} 🤬')
        break
    else:
        if attempts==max_attempts:
            print(f'max attempts reached')
        else:
            print(f'Attempt {attempts} failed status code {status_code}, waiting 30 seconds before the next attempt')
        attempts+=1
        time.sleep(30)