import json
import requests

API_HOST = "https://api.stockfighter.io/ob/api"

class Trader:
    def __init__(self, api_key, account, stock, venue):
        self.api_key = api_key
        self.account = account
        self.stock = stock
        self.venue = venue
        
    def heartbeat(self):
        url = API_HOST + "/heartbeat"
        r = requests.get(url)
        print(r.text)
    
    def check_venue(self):
        url = API_HOST + "/venues/" + self.venue +"/heartbeat"
        r = requests.get(url)
        print(r.text)
    
    def stocks_in_venue(self):
        url = API_HOST + "/venues/" + self.venue + "/stocks"
        r = requests.get(url)
        print(r.text)
  
    def orderbook(self):
        url = API_HOST + "/venues/" + self.venue + "/stocks/" + self.stock
        r = requests.get(url)
        print(r.text)
        
    def quote(self):
        url = API_HOST + "/venues/" + self.venue + "/stocks/" + self.stock + "/quote"
        r = requests.get(url)
        self.save_results(r.text)
        print(r.text)
    
    def buy(self, price, quantity, order_type):
        price = int(price)
        quantity = int(quantity)
        url = API_HOST + "/venues/" + self.venue + "/stocks/" + self.stock + "/orders"
        headers = {"X-Starfighter-Authorization" : self.api_key}
        order = {
            "account" : self.account,
            "venue" : self.venue,
            "symbol" : self.stock,
            "price" : price,  #25000 = $250.00 -- probably ludicrously high
            "qty" : quantity,
            "direction" : "buy",
            "orderType" : order_type  # See the order docs for what a limit order is
        }
        order = json.JSONEncoder().encode(order)
        r = requests.post(url, headers = headers, data = order)
        self.save_results(r.text)
        print(r.text)
        print ("Buy order successful")
        
    def order_status(self, order_id = ""):
        order_id = str(order_id)
        url = API_HOST + "/venues/" + self.venue + "/stocks/" + self.stock + "/orders/" + order_id
        headers = {"X-Starfighter-Authorization" : self.api_key}
        r = requests.get(url, headers = headers)
        self.save_results(r.text)
        print(r.text)
        
    def all_orders(self):
        url = API_HOST + "/venues/" + self.venue + "/accounts/" + self.account + "/stocks/" + self.stock + "/orders/"
        headers = {"X-Starfighter-Authorization" : self.api_key}
        r = requests.get(url, headers = headers)
        self.save_results(r.text)
        print(r.text)
        
    def cancel_order(self, order_id):
        order_id = str(order_id)
        url = API_HOST + "/venues/" + self.venue + "/stocks/" + self.stock + "/orders/" + order_id
        r = requests.delete(url)
        print ("Order deleted")
            
            
            
    def save_results(self, data):
        f = open('stock_results.json', 'w')
        f.write(str(data))
        f.close()
        
#https://www.stockfighter.io/ui/api_keys
f = open('stockfighter_api.txt')
api_key = f.read()

#On level page
account = "GBR15244395"

test = None
stock = "SFCM"
venue = "EXFEX"

if test:
    stock = "FOOBAR"
    venue = "TESTEX"

trader = Trader(api_key, account, stock, venue)
trader.quote()

trader.buy(30, 1000, "fill-or-kill")
