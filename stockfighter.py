import json
import requests

#https://www.stockfighter.io/ui/api_keys
api_key = ""

#On level page
account = ""
venue = "VWTEX"
stock = "CUUM"


API_HOST = "https://api.stockfighter.io/ob/api"

#Quotes Url
#url = API_HOST + "/venues/" + venue + "/stocks/" + stock + "/quote"

#Orders Url
url = API_HOST + "/venues/" + venue + "/stocks/" + stock + "/orders"

headers = {"X-Starfighter-Authorization" : api_key}

order = {
    "account" : account,
    "venue" : venue,
    "symbol" : stock,
    "price" : 4000,  #$40.00 -- probably ludicrously high
    "qty" : 100,
    "direction" : "buy",
    "orderType" : "market"  # See the order docs for what a limit order is
}

order = json.JSONEncoder().encode(order)

r = requests.post(url, headers = headers, data = order)
print (r.text)
#f = open('stock_results.json', 'w')
#f.write(str(r.json()))
#f.close()
#print (r.json())
