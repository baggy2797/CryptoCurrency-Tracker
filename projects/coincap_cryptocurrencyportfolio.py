import json
import requests
from datetime import datetime

from requests.api import head
from prettytable import PrettyTable
from colorama import init, deinit, Fore, Back, Style

# initialise colorama on Window platforms
init()
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


print()
print("MY PORTFOLIO")
print()

limit = len(ticker_url_pairs)
start = 1
portfolio_value = 0.00
last_updated = 0

table = PrettyTable(['Asset','Amount Owned', convert + ' Value', 'Price', '1h', '24h', '7d'])

with open('portfolio.txt') as inp:
    for line in inp:
        ticker, amount = line.split()
        ticker = ticker.upper()
        # print(ticker)
        # # ticker_url = 'https://api.coinmarketcap.com/v2/ticker/'+ str(ticker_url_pairs[ticker]) +'/' + url_end
        # # request = requests.get(ticker_url,headers = headers)
        # # results = request.json()

        ticker_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?&' +'&convert=USD'
        ticker_url += '&limit=' + str(limit) + '&start=' + str(start)
        request = requests.get(ticker_url,headers= headers)
        result = request.json()
        
        currency = result['data']
        # print(currency[0]['name'])
        for i in range(len(currency)):
            if currency[i]['symbol'] == ticker:
                search = currency[i]
        
        # print(search)

        rank  = search['cmc_rank']
        name = search['name']
        last_updated = search['last_updated']
        symbol = search['symbol']
        quotes = search['quote'][convert]
        hour_change = quotes['percent_change_1h']
        day_change = quotes['percent_change_24h']
        week_change = quotes['percent_change_7d']
        price = quotes['price']

        value = float(price)*float(amount)
        value_string = '{:,}'.format(round(value,2))

        portfolio_value += value

        if hour_change is not None:
            if hour_change > 0:
                hour_change = Back.GREEN + str(hour_change) + '%' + Style.RESET_ALL
            else:
                hour_change = Back.RED + str(hour_change) + '%' + Style.RESET_ALL

        if day_change is not None:
            if day_change > 0:
                day_change = Back.GREEN + str(day_change) + '%' + Style.RESET_ALL
            else:
                day_change = Back.RED + str(day_change) + '%' + Style.RESET_ALL

        if week_change is not None:
            if week_change > 0:
                week_change = Back.GREEN + str(week_change) + '%' + Style.RESET_ALL
            else:
                week_change = Back.RED + str(week_change) + '%' + Style.RESET_ALL

        table.add_row([name + ' ({})'.format(symbol),
                        str(amount),
                        '$' + value_string,
                        '$' + str(price),
                        str(hour_change),
                        str(day_change),
                        str(week_change)])
        
print(table)
print()

portfolio_value_string = '{:,}'.format(round(portfolio_value,2))
# last_updated_string = datetime.fromtimestamp(last_updated).strftime('%B %d, %Y at %I:%M%p')

print('Total porfolio value: ' + Back.GREEN + '$' + portfolio_value_string + Style.RESET_ALL)
print()
print('API Results Last Updated on ' + last_updated)
print()

#de-initialise colorama on Window platforms
deinit()

