import os
from datetime import datetime #library, allows us not having to write datetime.datetime
import requests
import json

timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

#print(timestamp)

data_dir = 'data'
os.makedirs(data_dir,exist_ok=True)
filename = f'{data_dir}/{timestamp}.json' 

api_endpoint = 'https://api.tfl.gov.uk/BikePoint/'

#print(filename)

response = requests.get(api_endpoint)

data = response.json()

#print(data) #mindful that this prints in the terminal

with open(filename,'w') as file:
    json.dump(data, file) #currently no safeguarding around having no response, so files can be empty if there is no response