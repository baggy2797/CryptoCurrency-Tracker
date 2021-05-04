import json
import requests
from datetime import datetime
import os
import time
from requests.api import head
# from prettytable import PrettyTable
# from colorama import init, deinit, Fore, Back, Style

# initialise colorama on Window platforms
# init()
convert = 'USD'
listing_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?convert='+convert
# listings_url = 'https://api.coinmarketcap.com/v2/listings/?convert=' + convert
url_end = '?structure=array&convert_id=' + convert

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'YOUR-API-KEY-HERE',
}

request = requests.get(listing_url,headers = headers)
results = request.json()
data = results['data']

ticker_url_pairs = {}
for currency in data:
    symbol = currency['symbol']
    url = currency['id']
    name = currency['name']
    # print(url)
    ticker_url_pairs[symbol] = (url,name)

limit = len(ticker_url_pairs)
start = 1
print()
print('ALERTS TRACKING...')
print()

already_hit_symbols = []

while True:
    with open('alerts.txt') as inp:
        for line in inp:
            ticker,amount = line.split()
            ticker = ticker.upper()
            ticker_url = ticker_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?&' +'&convert=USD'
            ticker_url += '&limit=' + str(limit) + '&start=' + str(start)
            request = requests.get(ticker_url,headers= headers)
            result = request.json()
            # request = requests.get(ticker_url)
            # results = request.json()
            currency = result['data']
            # print(currency[0]['name'])
            for i in range(len(currency)):
                if currency[i]['symbol'] == ticker:
                    search = currency[i]
            
            # currency = results['data'][0]
            name = search['name']
            last_updated = search['last_updated']
            symbol = search['symbol']
            quotes = search['quote'][convert]
            price = quotes['price']

            if float(price) >= float(amount) and symbol not in already_hit_symbols:
                os.system('say ' + name + ' hit ' + amount) #for mac platform
                # windowspeak.Speak(name + ' hit ' + amount) #for window platform
                # last_updated_string = datetime.fromtimestamp(last_updated).strftime('%B %d, %Y at %I:%M%p')
                print(name + ' hit ' + amount + ' on ' + last_updated)
                already_hit_symbols.append(symbol)
    print("...")
    time.sleep(6)
