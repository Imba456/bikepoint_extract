# bikepoint_extract
bikepoint extract repo to start obtaining data

sudo code plan for extract
-----

- [x] import os
- [x] import datetime
- [x] import requests
- [x] import json
- [x] import time
- [x] import logging

- [x] timestamp for filename
- [x] create a data folder

- [ ] while loop, 3 < max
    - [x] call api
    - [x] check the response
        - [x] if status code 2xx
            - [x] try - save data locally - except
            - [x] break
        - [x] elif status code 3xx or 4xx
            - [x] break & notify
        - [x] else
            - [x] #+=1
            - [x] wait 30 seconds

- [x] save data locally

-----

sudo LOAD code
- [x] import aws related packages - boto3
- [x] import os
- [x] import dotenv
- [x] import logging

- [ ] start logging
- [x] read in keys
- [x] where is json
- [x] create a list
- [x] connect to aws
- [x] setup s3 client

- [x] upload to s3
- [x] for loop
- [x] check the upload
- [x] delete locally
- [ ] end logging