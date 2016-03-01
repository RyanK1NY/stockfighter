exec(open("stockfighter.py").read())

#https://www.stockfighter.io/ui/api_keys
f = open('stockfighter_api.txt')
api_key = f.read()

#On level page
account = "SE12159077"

test = None
stock = "LRC"
venue = "RUHEX"

if test:
    stock = "FOOBAR"
    venue = "TESTEX"

trader = Trader(api_key, account, stock, venue)
trader.orderbook()
order_size = 10000
orders = int(20000/order_size)
#for x in range(1,orders):
#    trader.buy(9710, order_size, "immediate-or-cancel")
trader.buy(9650, 4533, "limit")
