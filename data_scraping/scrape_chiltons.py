"""Initial experiment to see if we can scrape Chilton's
"""

import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = 'https://app.chiltonlibrary.com/home?id_token=eyJraWQiOiIyMTU3NDU1ODE1NjA3NzI5NjY4Mjc4Mzc4MzYwNDg3MjE2NzU5ODMiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJDaGlsdG9uTGlicmFyeS5jb20iLCJhdWQiOiJHYWxlIiwic3ViIjoiZ2FpbnN0b2Z0ZWNoIiwiaWF0IjoxNzA4MzA4MzQ1LCJleHAiOjE3MDgzMTE5NDUsInZlciI6IjIiLCJsb2NhdGlvbl9pZCI6ImdhaW5zdG9mdGVjaCIsImxvY2F0aW9uX3RpdGxlIjoiR2VvcmdpYSBJbnN0aXR1dGUgT2YgVGVjaG5vbG9neSIsImluc3RpdHV0aW9uX2lkIjoiZ2Vvcmdpb3QiLCJpbnN0aXR1dGlvbl90aXRsZSI6IiIsImNvdW50cnkiOiJVUyIsInJlZ2lvbiI6IkdBIiwiYXV0aF90eXBlIjoic2hpYmJvbGV0aCIsImNsaWVudF9pcCI6Ijk5LjI2LjE0MC4yMTciLCJ1YSI6IjQxOTQ5OTM1NyIsImxhbmdfaWQiOiIxIiwibGF1bmNoX2RvbWFpbiI6ImdhbGUuY29tIiwiYXV0aF9zZXJ2ZXIiOiJodHRwczovL2luZm90cmFjLmdhbGUuY29tL2dhbGVuZXQvZ2FpbnN0b2Z0ZWNoIiwibWVudV9zZXJ2ZXIiOiJodHRwczovL2xpbmsuZ2FsZS5jb20vYXBwcy9tZW51P3VzZXJHcm91cE5hbWU9Z2FpbnN0b2Z0ZWNoIiwic2Vzc2lvbl9pZCI6IjE3MDgzMDgzNDU1NDZnYWluc3RvZnRlY2giLCJ1aV9wcmVmZXJlbmNlIjoiZ2FsZW5ldCIsInByb2R1Y3RfaWQiOiJDSExMIiwiZXhwaXJhdGlvbiI6IjIwMjQwMjIwMDIwNTQ1IEdNVCIsImxpY2Vuc2VfdG9rZW4iOm51bGwsImxpY2Vuc2VfbGltaXQiOi0xLCJicmFuZGluZ19zY3JpcHQiOiIgIiwiYnJhbmRpbmdfdGV4dCI6IiAiLCJzY29wZSI6InJlYWQifQ.sMw7vzL0p0kZWTKPjtgrutsIg31mTzVuB6fQl6BCRCl9kVGEs5Mo1fafi_ma7N7JB-R44Uh8WfzrsHgyWfP8DZyLIM8ERzeafVwo-OGP0AY1LY_mNkAPfy6qdXxj96suJNsaDyT-UL6txxBKAxu8lUiTv0SiNizbhzDiGVp5edX6LAC434aRNDihU8qgK0Mkp1lEOO-CZBUPTTY1q32rNzy6gx7rJR7J1yUNTvOYd1YGO2D721Lwy1hPqG_gFtvjSLUdLBPUzQgBXMoqTDpDT9ppHOZqYbqtnOiUW7jUYA9K_VUrVv0_13AkBzHPAnibJGR2lRgwd8ZcWXAyhct2GA'


HEADERS = {
    "Referer": "https://google.com",
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"
}

# Send a GET request to the website
response = requests.get(url, headers=HEADERS)

print(response.text)
print(response)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    print(soup)