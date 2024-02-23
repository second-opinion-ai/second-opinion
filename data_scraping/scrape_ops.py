from urllib.parse import urlencode

import requests

SCRAPEOPS_API_KEY = os.environ.get("SCRAPEOPS_API_KEY")

def get_scrapeops_url(url):

    payload = {'api_key': SCRAPEOPS_API_KEY, 'url': url}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url

url_ = "https://link.gale.com/apps/CHLL"
r = requests.get(get_scrapeops_url(url_))
print(r.text)
