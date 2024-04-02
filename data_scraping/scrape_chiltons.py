"""Initial experiment to see if we can scrape Chilton's
"""

import json
import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
# url = 'https://app.chiltonlibrary.com/home?id_token=eyJraWQiOiIyMTU3NDU1ODE1NjA3NzI5NjY4Mjc4Mzc4MzYwNDg3MjE2NzU5ODMiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJDaGlsdG9uTGlicmFyeS5jb20iLCJhdWQiOiJHYWxlIiwic3ViIjoiZ2FpbnN0b2Z0ZWNoIiwiaWF0IjoxNzA4MzA4MzQ1LCJleHAiOjE3MDgzMTE5NDUsInZlciI6IjIiLCJsb2NhdGlvbl9pZCI6ImdhaW5zdG9mdGVjaCIsImxvY2F0aW9uX3RpdGxlIjoiR2VvcmdpYSBJbnN0aXR1dGUgT2YgVGVjaG5vbG9neSIsImluc3RpdHV0aW9uX2lkIjoiZ2Vvcmdpb3QiLCJpbnN0aXR1dGlvbl90aXRsZSI6IiIsImNvdW50cnkiOiJVUyIsInJlZ2lvbiI6IkdBIiwiYXV0aF90eXBlIjoic2hpYmJvbGV0aCIsImNsaWVudF9pcCI6Ijk5LjI2LjE0MC4yMTciLCJ1YSI6IjQxOTQ5OTM1NyIsImxhbmdfaWQiOiIxIiwibGF1bmNoX2RvbWFpbiI6ImdhbGUuY29tIiwiYXV0aF9zZXJ2ZXIiOiJodHRwczovL2luZm90cmFjLmdhbGUuY29tL2dhbGVuZXQvZ2FpbnN0b2Z0ZWNoIiwibWVudV9zZXJ2ZXIiOiJodHRwczovL2xpbmsuZ2FsZS5jb20vYXBwcy9tZW51P3VzZXJHcm91cE5hbWU9Z2FpbnN0b2Z0ZWNoIiwic2Vzc2lvbl9pZCI6IjE3MDgzMDgzNDU1NDZnYWluc3RvZnRlY2giLCJ1aV9wcmVmZXJlbmNlIjoiZ2FsZW5ldCIsInByb2R1Y3RfaWQiOiJDSExMIiwiZXhwaXJhdGlvbiI6IjIwMjQwMjIwMDIwNTQ1IEdNVCIsImxpY2Vuc2VfdG9rZW4iOm51bGwsImxpY2Vuc2VfbGltaXQiOi0xLCJicmFuZGluZ19zY3JpcHQiOiIgIiwiYnJhbmRpbmdfdGV4dCI6IiAiLCJzY29wZSI6InJlYWQifQ.sMw7vzL0p0kZWTKPjtgrutsIg31mTzVuB6fQl6BCRCl9kVGEs5Mo1fafi_ma7N7JB-R44Uh8WfzrsHgyWfP8DZyLIM8ERzeafVwo-OGP0AY1LY_mNkAPfy6qdXxj96suJNsaDyT-UL6txxBKAxu8lUiTv0SiNizbhzDiGVp5edX6LAC434aRNDihU8qgK0Mkp1lEOO-CZBUPTTY1q32rNzy6gx7rJR7J1yUNTvOYd1YGO2D721Lwy1hPqG_gFtvjSLUdLBPUzQgBXMoqTDpDT9ppHOZqYbqtnOiUW7jUYA9K_VUrVv0_13AkBzHPAnibJGR2lRgwd8ZcWXAyhct2GA'
url = 'https://appapi.chiltonlibrary.com/chilton-vehicle-service/make/2024'

TOKEN = 'eyJraWQiOiIyMTU3NDU1ODE1NjA3NzI5NjY4Mjc4Mzc4MzYwNDg3MjE2NzU5ODMiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJDaGlsdG9uTGlicmFyeS5jb20iLCJhdWQiOiJHYWxlIiwic3ViIjoic3BsX21haW4iLCJpYXQiOjE3MTE2Nzc1ODcsImV4cCI6MTcxMTY4MTE4NywidmVyIjoiMiIsImxvY2F0aW9uX2lkIjoic3BsX21haW4iLCJsb2NhdGlvbl90aXRsZSI6IlNlYXR0bGUgUHVibGljIExpYnJhcnkiLCJpbnN0aXR1dGlvbl9pZCI6InNwbCIsImluc3RpdHV0aW9uX3RpdGxlIjoiIiwiY291bnRyeSI6IlVTIiwicmVnaW9uIjoiV0EiLCJhdXRoX3R5cGUiOiJpcCIsImNsaWVudF9pcCI6IjY2LjIxMi42NS4yMTUiLCJ1YSI6IjUwOTkwODY1IiwibGFuZ19pZCI6IjEiLCJsYXVuY2hfZG9tYWluIjoiZ2FsZS5jb20iLCJhdXRoX3NlcnZlciI6Imh0dHBzOi8vaW5mb3RyYWMuZ2FsZS5jb20vZ2FsZW5ldC9zcGxfbWFpbiIsIm1lbnVfc2VydmVyIjoiaHR0cHM6Ly9saW5rLmdhbGUuY29tL2FwcHMvbWVudT91c2VyR3JvdXBOYW1lPXNwbF9tYWluIiwic2Vzc2lvbl9pZCI6IjE3MTE2Njg3MzA1NzZzcGxfbWFpbiIsInVpX3ByZWZlcmVuY2UiOiJnYWxlbmV0IiwicHJvZHVjdF9pZCI6IkNITEwiLCJleHBpcmF0aW9uIjoiMjAyNDAzMjkyMzMyMTAgR01UIiwibGljZW5zZV90b2tlbiI6bnVsbCwibGljZW5zZV9saW1pdCI6LTEsImJyYW5kaW5nX3NjcmlwdCI6Imh0dHBzOi8vYXNzZXRzLmNlbmdhZ2UuY29tL2dhbGUvYnJhbmRpbmcvY29uc29ydGlhL3dzbC5qcyIsImJyYW5kaW5nX3RleHQiOiIgIiwic2NvcGUiOiJyZWFkIn0.rdscK3PensoS-00Net9vRU4d1f3tEsAaICK3WklfMEjmM7p_ryVZ-B1zXO8B--CENs_SX6sTjk_j9A_VdgmRACIw1hcgj3XSkPXzcaoX9BUBGhu2uHIFu_03x7IN-DJ8Sat4dPJLqEqbr2F6r_zRHSt7xav9AIx5MgXwsV3-c8ns6tRtFokilBnkctzRGt8R0kPdmf69AHg67-ZeZeNiyoU_BLTogRNAjLo0QW7wrAJ-vf0BsoSptED2TcCZsYCw9-6A51NMZ2ALneOmzq128BvNclgefwr5NR_2PMe8N0HRmVkADybpjS15Kpb4_95B6aTj3KMSk7gP7pOn9VjyAA'
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

# with open (f"/Users/linliu/dev/second-opinion/data_scraping/json_dump/{base_vehicle_id}.json", "w") as fo:
#      json.dump(toc, fo, ensure_ascii = False) 



# examples of scraping repair content under "Body Exterior, Doors, Roof & Vehicle Security --> Body Repair --> Fundamentals --> Service Information --> Aluminum Repair --> Body Straightening (Aluminum) --> Frame Straightening"

# step 1: get the IDs from available vehicles (e.g. Rogue, Rogue_HEV)
# url right before the repair content ("Available Configurations" under "Frame Straightening" page)
# 140871 <-- base_vehicle_id
# 115931 <-- tocID in 'toc' before the repair content (e.g. 'Frame Straightening')

url = f'{BASE_URL}/chilton-repair-service/toc/articlelist/140871/115931'
avail_vehicles = get_request_basic()
print (avail_vehicles)

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

# --- TODO ----
# add repair_response and avail_vehicles toc
# test json file

## need a json traversal tool
with open('/Users/linliu/dev/second-opinion/data_scraping/json_dump/json_test.json') as f:
    r_json = json.load(f)


i = 0
for lay0 in r_json[0]['elements']:
    if 'elements' in lay0.keys() and len(lay0['elements']) != 0:
            print (i, ': ', lay0, '\n----')
            #print (lay1, '\n****')
    i += 1



# section 2: explore toc json
with open ('/Users/linliu/dev/second-opinion/data_scraping/json_dump/140871.json') as f:
     toc_json = json.load(f)

# need to traversal the json file till children: [], then use the tocId where children is [] for 'parentTocId' parameter in 'json = data' to request article content
     # and then insert the content back to the children as {'text': text_parsed_from_r_json}

lay1_labels = []
for item in toc_json['data']:
     lay1_labels.append(lay1['label'])

len(lay1_labels) # should be 18


# recursively request for and insert repair content
def assess_children (input_json):
    children_ls = input_json['children']
    if len(children_ls) == 0:
          print ('--make a request--\n')
          tocId = input_json['tocId']
          # make a request
          # process the return 
          
          # insert in the text
          input_json['children'].append({'text': repair_response})
          print (input_json)
    else:
         for h2 in children_ls:
            assess_children(h2)


assess_children(toc_json['data'][0])

