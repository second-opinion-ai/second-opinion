"""Initial experiment to see if we can scrape Chilton's
"""

import json
import requests
from bs4 import BeautifulSoup


# URL of the website you want to scrape
url = 'https://appapi.chiltonlibrary.com/chilton-vehicle-service/make/2024'

TOKEN = 'eyJraWQiOiIyMTU3NDU1ODE1NjA3NzI5NjY4Mjc4Mzc4MzYwNDg3MjE2NzU5ODMiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJDaGlsdG9uTGlicmFyeS5jb20iLCJhdWQiOiJHYWxlIiwic3ViIjoic3BsX21haW4iLCJpYXQiOjE3MTI2MzE1NzAsImV4cCI6MTcxMjYzNTE3MCwidmVyIjoiMiIsImxvY2F0aW9uX2lkIjoic3BsX21haW4iLCJsb2NhdGlvbl90aXRsZSI6IlNlYXR0bGUgUHVibGljIExpYnJhcnkiLCJpbnN0aXR1dGlvbl9pZCI6InNwbCIsImluc3RpdHV0aW9uX3RpdGxlIjoiIiwiY291bnRyeSI6IlVTIiwicmVnaW9uIjoiV0EiLCJhdXRoX3R5cGUiOiJpcCIsImNsaWVudF9pcCI6IjY2LjIxMi42NS4yMTUiLCJ1YSI6IjUwOTkwODY1IiwibGFuZ19pZCI6IjEiLCJsYXVuY2hfZG9tYWluIjoiZ2FsZS5jb20iLCJhdXRoX3NlcnZlciI6Imh0dHBzOi8vaW5mb3RyYWMuZ2FsZS5jb20vZ2FsZW5ldC9zcGxfbWFpbiIsIm1lbnVfc2VydmVyIjoiaHR0cHM6Ly9saW5rLmdhbGUuY29tL2FwcHMvbWVudT91c2VyR3JvdXBOYW1lPXNwbF9tYWluIiwic2Vzc2lvbl9pZCI6IjE3MTI2MzE1NzAzOTZzcGxfbWFpbiIsInVpX3ByZWZlcmVuY2UiOiJnYWxlbmV0IiwicHJvZHVjdF9pZCI6IkNITEwiLCJleHBpcmF0aW9uIjoiMjAyNDA0MTAwMjU5MzAgR01UIiwibGljZW5zZV90b2tlbiI6bnVsbCwibGljZW5zZV9saW1pdCI6LTEsImJyYW5kaW5nX3NjcmlwdCI6Imh0dHBzOi8vYXNzZXRzLmNlbmdhZ2UuY29tL2dhbGUvYnJhbmRpbmcvY29uc29ydGlhL3dzbC5qcyIsImJyYW5kaW5nX3RleHQiOiIgIiwic2NvcGUiOiJyZWFkIn0.odTGVi5mWq1Vg3qsE5f7bZBJmUpp53-Qq3e6fvSe85YicZHw567iuBdg3xol7XkFY8oNjTDNt3hPaVzBItyyiNHAlJeFssRgGmmAnZe9g1JhA4QPmIiZcN5bmpPbS1KM9sZ4LT5tPhqqCtw-ehlXzzBOY-Mw402CraMP69n3iKVGX-Ky0apd63ycNWK-csEY4ozIOwp-qU6GfyTneGpg8hvzSmHEZk2IH8j4UL7v0lN0EtggQ9SFGweKeXfUOkFLftx9-t5mrm3jVkV7HAnbdJonluFPwcuyTJ7vVkP2z6uukYCPnvFL3SQGODZ752keOny79KjlcgbHWWAMWLg_BA'
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

r_json = repair_response.json()
# --- TODO ----
# add repair_response and avail_vehicles toc
# test json file

## need a json traversal tool
with open('/Users/linliu/dev/second-opinion/data_scraping/json_dump/json_test.json') as f:
    r_json = json.load(f)


i = 0
for lay0 in r_json[0]['elements']:
    if 'elements' in lay0.keys() and len(lay0['elements']) != 0:
            
            print (i, ': ', lay0['elements'], '\n----')
                    #print (lay1, '\n****')
    i += 1



# section 2: explore toc json
with open ('/Users/linliu/dev/second-opinion/data_scraping/json_dump/140871.json') as f:
     toc_json = json.load(f)

# need to traversal the json file till children: [], then use the tocId where children is [] for 'parentTocId' parameter in 'json = data' to request article content
     # and then insert the content back to the children as {'text': text_parsed_from_r_json}


# recursively request for and insert repair content
def assess_children (input_json):
    children_ls = input_json['children']
    if len(children_ls) == 0:
          print ('--make a request--\n')
          tocId = input_json['tocId']
          # make a request
          # process the return 
          repair_text = get_repair_text(r_json)
          # insert in the text
          input_json['children'].append({'text': repair_text})
          print (input_json)
    else:
         for h2 in children_ls:
            assess_children(h2)


assess_children(toc_json['data'][0])


def find_text_in_elements(input_json, repair_text):
    print ('\n\n iteration repair_text', repair_text)
    elements = input_json['elements']
    if elements is None:
        print ('FOUND TEXT...', input_json['text'])
        print ('.Before storing, ', repair_text)
        repair_text = repair_text + '\n' + input_json['text']
        print ('.After storing, ', repair_text)
    else:
        for item in elements:
            print ('next iteration with repair_text', repair_text)
            repair_text = find_text_in_elements(item, repair_text)
    return repair_text


def get_repair_text(r_json):
    repair_text = ''
    for item in r_json:
         if 'elements' in item.keys() and len(item['elements']) != 0:
            for lay in item['elements']:
                if lay['name'] == 'Itemizedlist':
                    repair_text = find_text_in_elements(lay, repair_text)
    return (repair_text)



a =get_repair_text(r_json)
a

