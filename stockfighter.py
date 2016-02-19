import json
import requests

#https://www.stockfighter.io/ui/api_keys
api_key = ""
venue = "BJBEX"
stock = "ZEYF"

API_HOST = "https://api.stockfighter.io/ob/api"


url = API_HOST + "/venues/" + venue + "/stocks/" + stock + "/quote"
r = requests.get(url)
print (r.json())