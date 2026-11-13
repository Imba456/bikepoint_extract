# bikepoint_extract
bikepoint extract repo to start obtaining data

sudo code plan
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
