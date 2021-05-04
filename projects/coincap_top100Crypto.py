import json
import requests 
from datetime import datetime
from prettytable import PrettyTable
from colorama import init, deinit,Fore,Back,Style

convert = "USD"

globalURL = "https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest?convert="+convert

#from the API documentation
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'YOUR-API-KEY-HERE',
}

request = requests.get(globalURL,headers = headers)
results = request.json()
data = results['data']

# print(data)
global_cap = int(data['quote']['USD']['total_market_cap'])
global_cap_string = '{:,}'.format(global_cap)

while True:
    print()
    print('CoinMarketCap Explorer Menu')
    print('The global market cap is $ ' + global_cap_string)
    print()
    print('1 - Top 100 sorted by market cap')
    print('2 - Top 100 sorted by 24 hour change')
    print('3 - Top 100 sorted by 24 hour volume')
    print('0 - Exit')
    print()
    choice = input('What is your choice? (1-3): ')
    ticker_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?sort='
    # ticker_url = 'https://api.coinmarketcap.com/v2/ticker/?structure=array&sort='

    if choice == '1':
        ticker_url+='market_cap'
    elif choice == '2':
        ticker_url += 'percent_change_24h'
    elif choice == '3':
        ticker_url += 'volume_24h'
    else:
        break

    request = requests.get(ticker_url,headers = headers)
    results = request.json()
    print(results)
    data = results['data']

    table = PrettyTable(['Rank','Asset', 'Price', 'Market Cap', 'Volume', '1h', '24h', '7d'])
    print()
    for currency in data:
        rank = currency['cmc_rank']
        name = currency['name']
        symbol =  currency['symbol']
        quotes = currency['quote'][convert]
        market_cap = quotes['market_cap']
        hour_change = quotes['percent_change_1h']
        day_change = quotes['percent_change_24h']
        week_change = quotes['percent_change_7d']
        price = quotes['price']
        volume = quotes['volume_24h']

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

        if volume is not None:
            volume_string = '{:,}'.format(volume)

        if market_cap is not None:
            market_cap_string = '{:,}'.format(market_cap)

        table.add_row([rank,
                        name + '({})'.format(symbol),
                        '$' + str(price),
                        '$' + market_cap_string,
                        '$' + volume_string,
                        str(hour_change),
                        str(day_change),
                        str(week_change)])
    print()
    print(table)
    print()

    choice = input('Again? (y/n) :')
    if choice == 'n':
        break

deinit()
