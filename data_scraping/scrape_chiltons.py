"""Initial experiment to see if we can scrape Chilton's
"""

import json
import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
# url = 'https://app.chiltonlibrary.com/home?id_token=eyJraWQiOiIyMTU3NDU1ODE1NjA3NzI5NjY4Mjc4Mzc4MzYwNDg3MjE2NzU5ODMiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJDaGlsdG9uTGlicmFyeS5jb20iLCJhdWQiOiJHYWxlIiwic3ViIjoiZ2FpbnN0b2Z0ZWNoIiwiaWF0IjoxNzA4MzA4MzQ1LCJleHAiOjE3MDgzMTE5NDUsInZlciI6IjIiLCJsb2NhdGlvbl9pZCI6ImdhaW5zdG9mdGVjaCIsImxvY2F0aW9uX3RpdGxlIjoiR2VvcmdpYSBJbnN0aXR1dGUgT2YgVGVjaG5vbG9neSIsImluc3RpdHV0aW9uX2lkIjoiZ2Vvcmdpb3QiLCJpbnN0aXR1dGlvbl90aXRsZSI6IiIsImNvdW50cnkiOiJVUyIsInJlZ2lvbiI6IkdBIiwiYXV0aF90eXBlIjoic2hpYmJvbGV0aCIsImNsaWVudF9pcCI6Ijk5LjI2LjE0MC4yMTciLCJ1YSI6IjQxOTQ5OTM1NyIsImxhbmdfaWQiOiIxIiwibGF1bmNoX2RvbWFpbiI6ImdhbGUuY29tIiwiYXV0aF9zZXJ2ZXIiOiJodHRwczovL2luZm90cmFjLmdhbGUuY29tL2dhbGVuZXQvZ2FpbnN0b2Z0ZWNoIiwibWVudV9zZXJ2ZXIiOiJodHRwczovL2xpbmsuZ2FsZS5jb20vYXBwcy9tZW51P3VzZXJHcm91cE5hbWU9Z2FpbnN0b2Z0ZWNoIiwic2Vzc2lvbl9pZCI6IjE3MDgzMDgzNDU1NDZnYWluc3RvZnRlY2giLCJ1aV9wcmVmZXJlbmNlIjoiZ2FsZW5ldCIsInByb2R1Y3RfaWQiOiJDSExMIiwiZXhwaXJhdGlvbiI6IjIwMjQwMjIwMDIwNTQ1IEdNVCIsImxpY2Vuc2VfdG9rZW4iOm51bGwsImxpY2Vuc2VfbGltaXQiOi0xLCJicmFuZGluZ19zY3JpcHQiOiIgIiwiYnJhbmRpbmdfdGV4dCI6IiAiLCJzY29wZSI6InJlYWQifQ.sMw7vzL0p0kZWTKPjtgrutsIg31mTzVuB6fQl6BCRCl9kVGEs5Mo1fafi_ma7N7JB-R44Uh8WfzrsHgyWfP8DZyLIM8ERzeafVwo-OGP0AY1LY_mNkAPfy6qdXxj96suJNsaDyT-UL6txxBKAxu8lUiTv0SiNizbhzDiGVp5edX6LAC434aRNDihU8qgK0Mkp1lEOO-CZBUPTTY1q32rNzy6gx7rJR7J1yUNTvOYd1YGO2D721Lwy1hPqG_gFtvjSLUdLBPUzQgBXMoqTDpDT9ppHOZqYbqtnOiUW7jUYA9K_VUrVv0_13AkBzHPAnibJGR2lRgwd8ZcWXAyhct2GA'
url = 'https://appapi.chiltonlibrary.com/chilton-vehicle-service/make/2024'

TOKEN = 'eyJraWQiOiIyMTU3NDU1ODE1NjA3NzI5NjY4Mjc4Mzc4MzYwNDg3MjE2NzU5ODMiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJDaGlsdG9uTGlicmFyeS5jb20iLCJhdWQiOiJHYWxlIiwic3ViIjoic3BsX21haW4iLCJpYXQiOjE3MTAxMzM4MzIsImV4cCI6MTcxMDEzNzQzMiwidmVyIjoiMiIsImxvY2F0aW9uX2lkIjoic3BsX21haW4iLCJsb2NhdGlvbl90aXRsZSI6IlNlYXR0bGUgUHVibGljIExpYnJhcnkiLCJpbnN0aXR1dGlvbl9pZCI6InNwbCIsImluc3RpdHV0aW9uX3RpdGxlIjoiIiwiY291bnRyeSI6IlVTIiwicmVnaW9uIjoiV0EiLCJhdXRoX3R5cGUiOiJpcCIsImNsaWVudF9pcCI6IjY2LjIxMi42NS4yMTUiLCJ1YSI6IjUwOTkwODY1IiwibGFuZ19pZCI6IjEiLCJsYXVuY2hfZG9tYWluIjoiZ2FsZS5jb20iLCJhdXRoX3NlcnZlciI6Imh0dHBzOi8vaW5mb3RyYWMuZ2FsZS5jb20vZ2FsZW5ldC9zcGxfbWFpbiIsIm1lbnVfc2VydmVyIjoiaHR0cHM6Ly9saW5rLmdhbGUuY29tL2FwcHMvbWVudT91c2VyR3JvdXBOYW1lPXNwbF9tYWluIiwic2Vzc2lvbl9pZCI6IjE3MTAxMzM4MzI5MzlzcGxfbWFpbiIsInVpX3ByZWZlcmVuY2UiOiJnYWxlbmV0IiwicHJvZHVjdF9pZCI6IkNITEwiLCJleHBpcmF0aW9uIjoiMjAyNDAzMTIwNTEwMzIgR01UIiwibGljZW5zZV90b2tlbiI6bnVsbCwibGljZW5zZV9saW1pdCI6LTEsImJyYW5kaW5nX3NjcmlwdCI6Imh0dHBzOi8vYXNzZXRzLmNlbmdhZ2UuY29tL2dhbGUvYnJhbmRpbmcvY29uc29ydGlhL3dzbC5qcyIsImJyYW5kaW5nX3RleHQiOiIgIiwic2NvcGUiOiJyZWFkIn0.YQuB9oDkubtCXRtlYQnKe0V2kXfZpxJNXyI2UYVXzmvuQbImVgRuhMoQP2Ga2i96bgmxjCI-Plka1Dh5qIgWfvZ_177aK-nL8slnNIuDuWyHDumU5m0G7FGphCxKq4YJVBveSUs25uNwFr_d3yIyJECpU21kvr2CJ2DdcuQfHR6cOhChNkaaF6ME3wn39pc1D_nnTm1DTm1Y6Jl1x6XhYFjInZq45ZS5Wijh_zHXzSVGzHSQ_68Okv8SlZnG_meX18ZFYNZvlbPmyql4SUSD808i0zAlfiNpB3I56c0YfGviILNFlg7WoKq2pFSNFevMNLt-B63o0AgfnhdV6aYt_g'

HEADERS = {
    # "Referer": "https://google.com",
    # "Accept-Language": "en-US,en;q=0.9",
    # "User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"
    "Authorization": f"Bearer {TOKEN}"

}

BASE_URL = 'https://appapi.chiltonlibrary.com'

url = f'{BASE_URL}/chilton-vehicle-service/make/2017'
def get_makes():
    # Send a GET request to the website
    response = requests.get(url, headers=HEADERS)
    makes = [x['make'] for x in response.json()['makes']]
    assert 'Nissan' in makes
    return makes

print(get_makes())

url = f'{BASE_URL}/chilton-vehicle-service/model/2017/Nissan'
def get_models():
    # Send a GET request to the website
    response = requests.get(url, headers=HEADERS)
    models = [x['model'] for x in response.json()['models']]
    assert 'Rogue' in models
    return models


print(get_models())


url = f'{BASE_URL}/chilton-vehicle-service/basevehicle'

def get_car_base():
    request_payload = {
        'make': 'Nissan',
        'model': 'Rogue',
        'year': 2017
    }
    # Send a POST request to the website
    response = requests.post(url, json=request_payload, headers=HEADERS)
    return response.json()


base_vehicle_id = get_car_base()['baseVehicleId']

print (base_vehicle_id)


url = f'{BASE_URL}/chilton-repair-service/toc/{base_vehicle_id}'

def get_request_basic():
    # Send a GET request to the website
    response = requests.get(url, headers=HEADERS)
    return response.json()

toc = get_request_basic()

# with open (f"./json_dump/{base_vehicle_id}.json", "w") as fo:
#      json.dump(toc, fo, ensure_ascii = False) 




# examples of scraping repair content under "Body Exterior, Doors, Roof & Vehicle Security --> Body Repair --> Fundamentals --> Service Information --> Aluminum Repair --> Body Straightening (Aluminum) --> Frame Straightening"

# step 1: get the IDs from available vehicles (e.g. Rogue, Rogue_HEV)
# url right before the repair content ("Available Configurations" under "Frame Straightening" page)
# 140871 <-- base_vehicle_id
# 115931 <-- tocID in 'toc' before the repair content (e.g. 'Frame Straightening')

url = f'{BASE_URL}/chilton-repair-service/toc/articlelist/140871/115931'
avail_vehicles = get_request_basic()

# step 2: get the repair content
url = f'{BASE_URL}/chilton-repair-service/toc/article'
data = {"bvid":140871,"articleIds":["330366"],"parentTocName":"Frame Straightening","parentTocId":115931}

# bvid <-- base_vehicle_id
# articleIds <-- articleIds in 'avail_vehicles'
# parentTocId <-- tocID in 'toc' before the repair content (e.g. 'Frame Straightening')


HEADERS.update(
{'Content-type':'application/json', 
    'Accept':'application/json'
})

repair_response = requests.post(url, 
    json = data,
    headers = HEADERS,
)

print(repair_response.json())

# TODO
# add repair_response and avail_vehicles toc

