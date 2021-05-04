import json
import requests

while True:
    ticker_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?'

    limit = 10
    start = 1
    sort = 'name'
    convert = 'USD'

    choice = input("Do you want to enter any custom parameters? (y/n): ")

    if choice == 'y':
        limit = input('What is the custom limit?: ')
        start = input('What is the custom start number?: ')
        sort = input('What do you want to sort by?: ')
        convert = input('What is your local currency?: ')

    

    ticker_url += '&limit=' + str(limit) + '&sort=' + sort + '&start=' + str(start) + '&convert=' + convert
    
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'YOUR-API-KEY-HERE',
    }

    request = requests.get(ticker_url,headers = headers)
    results = request.json()

    
    
    
    data = results['data']

    if sort == "rank":
        def sortByRank(start,limit,fetchedResults):
            holder = {}
            for key,value in fetchedResults.items():
                if int(value["cmc_rank"]) <int(start) or int(value["cmc_rank"]) >int(start)+int(limit):continue
                else:holder[key] = value
            return holder
    
    print(results)
    
    

    for currency in data:
        rank = currency['cmc_rank']
        name = currency['name']
        symbol = currency['symbol']

        circulating_supply = int(currency['circulating_supply'])
        total_supply = int(currency['total_supply'])

        quotes = currency['quote'][convert]
        market_cap = quotes['market_cap']
        hour_change = quotes['percent_change_1h']
        day_change = quotes['percent_change_24h']
        week_change = quotes['percent_change_7d']
        price = quotes['price']
        volume = quotes['volume_24h']

        volume_string = '{:,}'.format(volume)
        market_cap_string = '{:,}'.format(market_cap)
        circulating_supply_string = '{:,}'.format(circulating_supply)
        total_supply_string = '{:,}'.format(total_supply)

        print(str(rank) + ': ' + name + ' (' + symbol + ')')
        print('Market cap: \t\t$' + market_cap_string)
        print('Price: \t\t\t$' + str(price))
        print('24h Volume: \t\t$' + volume_string)
        print('Hour change: \t\t' + str(hour_change) + '%')
        print('Day change: \t\t' + str(day_change) + '%')
        print('Week change: \t\t' + str(week_change) + '%')
        print('Total supply: \t\t' + total_supply_string)
        print('Circulating supply: \t' + circulating_supply_string)
        try:
            print('Percentage of coins in circulation: ' + str(int(circulating_supply / total_supply * 100)))
        except ZeroDivisionError:
            continue
        print()

    choice = input('Again? (y/n): ')

    if choice == 'n':
        break


# def sortByRank(start,limit,fetchedResults):
#     holder = {}
#     for key,value in fetchedResults.items():
#         if int(value["rank"]) <int(start) or int(value["rank"]) >int(start)+int(limit):continue
#         else:holder[key] = value
#     return holder

# def sortById(start,limit,fetchedResults):
#     holder= {}
#     for key,value in fetchedResults.items():
#         if key < int(start) or key > int(start)+int(limit):continue
#         else:holder[key] = value
#     return dict(sorted(holder.items()))
