import requests
import json
import lxml.html

token = "602e1dc3-57fa-4398-9769-5fba4d9faf42"
shared_secret = "Hello1@t!%here"
url = "https://data.dol.gov/get/SweatToilAllRegions"
headers = {
    'X-API-KEY': token,
    'Aceept': 'application/json',
    'Limit':'1'
}
response = requests.get(url, headers = headers)
import code
code.interact(local=locals())
print(response.text)
