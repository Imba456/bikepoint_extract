# bikepoint_extract
bikepoint extract repo to start obtaining data

sudo code plan
-----

import os ✔️
import datetime ✔️
import requests ✔️
import json ✔️
import time ✔️
import logging ✔️

timestamp for filename ✔️
create a data folder ✔️

while loop, 3 < max
call api ✔️
check the response ✔️
    if status code 2xx
        try - save data locally - except ✔️
        break
    elif status code 3xx or 4xx
        break & notify
    else 
        #+=1
        wait 30 seconds

save data locally ✔️

-----