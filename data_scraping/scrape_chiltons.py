"""Initial experiment to see if we can scrape Chilton's
"""

import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
# url = 'https://app.chiltonlibrary.com/home?id_token=eyJraWQiOiIyMTU3NDU1ODE1NjA3NzI5NjY4Mjc4Mzc4MzYwNDg3MjE2NzU5ODMiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJDaGlsdG9uTGlicmFyeS5jb20iLCJhdWQiOiJHYWxlIiwic3ViIjoiZ2FpbnN0b2Z0ZWNoIiwiaWF0IjoxNzA4MzA4MzQ1LCJleHAiOjE3MDgzMTE5NDUsInZlciI6IjIiLCJsb2NhdGlvbl9pZCI6ImdhaW5zdG9mdGVjaCIsImxvY2F0aW9uX3RpdGxlIjoiR2VvcmdpYSBJbnN0aXR1dGUgT2YgVGVjaG5vbG9neSIsImluc3RpdHV0aW9uX2lkIjoiZ2Vvcmdpb3QiLCJpbnN0aXR1dGlvbl90aXRsZSI6IiIsImNvdW50cnkiOiJVUyIsInJlZ2lvbiI6IkdBIiwiYXV0aF90eXBlIjoic2hpYmJvbGV0aCIsImNsaWVudF9pcCI6Ijk5LjI2LjE0MC4yMTciLCJ1YSI6IjQxOTQ5OTM1NyIsImxhbmdfaWQiOiIxIiwibGF1bmNoX2RvbWFpbiI6ImdhbGUuY29tIiwiYXV0aF9zZXJ2ZXIiOiJodHRwczovL2luZm90cmFjLmdhbGUuY29tL2dhbGVuZXQvZ2FpbnN0b2Z0ZWNoIiwibWVudV9zZXJ2ZXIiOiJodHRwczovL2xpbmsuZ2FsZS5jb20vYXBwcy9tZW51P3VzZXJHcm91cE5hbWU9Z2FpbnN0b2Z0ZWNoIiwic2Vzc2lvbl9pZCI6IjE3MDgzMDgzNDU1NDZnYWluc3RvZnRlY2giLCJ1aV9wcmVmZXJlbmNlIjoiZ2FsZW5ldCIsInByb2R1Y3RfaWQiOiJDSExMIiwiZXhwaXJhdGlvbiI6IjIwMjQwMjIwMDIwNTQ1IEdNVCIsImxpY2Vuc2VfdG9rZW4iOm51bGwsImxpY2Vuc2VfbGltaXQiOi0xLCJicmFuZGluZ19zY3JpcHQiOiIgIiwiYnJhbmRpbmdfdGV4dCI6IiAiLCJzY29wZSI6InJlYWQifQ.sMw7vzL0p0kZWTKPjtgrutsIg31mTzVuB6fQl6BCRCl9kVGEs5Mo1fafi_ma7N7JB-R44Uh8WfzrsHgyWfP8DZyLIM8ERzeafVwo-OGP0AY1LY_mNkAPfy6qdXxj96suJNsaDyT-UL6txxBKAxu8lUiTv0SiNizbhzDiGVp5edX6LAC434aRNDihU8qgK0Mkp1lEOO-CZBUPTTY1q32rNzy6gx7rJR7J1yUNTvOYd1YGO2D721Lwy1hPqG_gFtvjSLUdLBPUzQgBXMoqTDpDT9ppHOZqYbqtnOiUW7jUYA9K_VUrVv0_13AkBzHPAnibJGR2lRgwd8ZcWXAyhct2GA'
url = 'https://appapi.chiltonlibrary.com/chilton-vehicle-service/make/2024'

HEADERS = {
    # "Referer": "https://google.com",
    # "Accept-Language": "en-US,en;q=0.9",
    # "User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"
    "Authorization": "Bearer eyJraWQiOiIyMTU3NDU1ODE1NjA3NzI5NjY4Mjc4Mzc4MzYwNDg3MjE2NzU5ODMiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJDaGlsdG9uTGlicmFyeS5jb20iLCJhdWQiOiJHYWxlIiwic3ViIjoiZ2FpbnN0b2Z0ZWNoIiwiaWF0IjoxNzA5MzkyNjQ5LCJleHAiOjE3MDkzOTYyNDksInZlciI6IjIiLCJsb2NhdGlvbl9pZCI6ImdhaW5zdG9mdGVjaCIsImxvY2F0aW9uX3RpdGxlIjoiR2VvcmdpYSBJbnN0aXR1dGUgT2YgVGVjaG5vbG9neSIsImluc3RpdHV0aW9uX2lkIjoiZ2Vvcmdpb3QiLCJpbnN0aXR1dGlvbl90aXRsZSI6IiIsImNvdW50cnkiOiJVUyIsInJlZ2lvbiI6IkdBIiwiYXV0aF90eXBlIjoic2hpYmJvbGV0aCIsImNsaWVudF9pcCI6IjEzMC40NC4xNDkuMTYiLCJ1YSI6IjE2OTEyMTQ1IiwibGFuZ19pZCI6IjEiLCJsYXVuY2hfZG9tYWluIjoiZ2FsZS5jb20iLCJhdXRoX3NlcnZlciI6Imh0dHBzOi8vaW5mb3RyYWMuZ2FsZS5jb20vZ2FsZW5ldC9nYWluc3RvZnRlY2giLCJtZW51X3NlcnZlciI6Imh0dHBzOi8vbGluay5nYWxlLmNvbS9hcHBzL21lbnU_dXNlckdyb3VwTmFtZT1nYWluc3RvZnRlY2giLCJzZXNzaW9uX2lkIjoiMTcwOTM5MjY0OTYxMGdhaW5zdG9mdGVjaCIsInVpX3ByZWZlcmVuY2UiOiJnYWxlbmV0IiwicHJvZHVjdF9pZCI6IkNITEwiLCJleHBpcmF0aW9uIjoiMjAyNDAzMDMxNTE3MjkgR01UIiwibGljZW5zZV90b2tlbiI6bnVsbCwibGljZW5zZV9saW1pdCI6LTEsImJyYW5kaW5nX3NjcmlwdCI6IiAiLCJicmFuZGluZ190ZXh0IjoiICIsInNjb3BlIjoicmVhZCJ9.Ql32KsUXuNlDDZLl7-jHm5oowQ4Wuphomu6aQI4CqoCsvqVb3V-b1GNRptqyGfCkfvcIwsFlKe3iKkoJOmFFk2Kbd0TUqZL3wgzU42w6t8IgT9nonZjB6C5as0s22VTcfnDiYFAr7m_VZqGRt6RfNu6B4MkBkVp7-djVpUyQCzROG42I5Meoh7CRrY_iKMuNFRk7aXlyaark8YCXQFFGWJRkzsIY_NyVDat3_EpNDTCyOVv8jaWzVv9UD8I0nFwVdqzn-t4rkLpLJ-v2rlqVeSLo90SnC1vz6Iy7EVYX5DnFp_wYZwdeeLZziu6t37G3081xEmmoInr_QCK-away7A"
}


url = 'https://appapi.chiltonlibrary.com/chilton-vehicle-service/make/2017'
def get_makes():
    # Send a GET request to the website
    response = requests.get(url, headers=HEADERS)
    makes = [x['make'] for x in response.json()['makes']]
    assert 'Nissan' in makes
    return makes
print(get_makes())

url = 'https://appapi.chiltonlibrary.com/chilton-vehicle-service/model/2017/Nissan'
def get_models():
    # Send a GET request to the website
    response = requests.get(url, headers=HEADERS)
    models = [x['model'] for x in response.json()['models']]
    assert 'Rogue' in models
    return models
print(get_models())

url = 'https://appapi.chiltonlibrary.com/chilton-vehicle-service/basevehicle'
def get_car_base():
    request_payload = {
        'make': 'Nissan',
        'model': 'Rogue',
        'year': 2017
    }
    # Send a GET request to the website
    response = requests.post(url, json=request_payload, headers=HEADERS)
    return response.json()
base_vehicle_id = get_car_base()['baseVehicleId']

url = f'https://appapi.chiltonlibrary.com/chilton-repair-service/toc/{base_vehicle_id}'
def get_table_of_contents():
    # Send a GET request to the website
    response = requests.get(url, headers=HEADERS)
    return response.json()
print(get_table_of_contents())