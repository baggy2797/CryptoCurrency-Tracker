import json
import requests

convert = 'USD'
listings_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
url_end = '&convert=' + convert

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'YOUR-API-KEY-HERE',
}


request = requests.get(listings_url,headers= headers)
result = request.json()
# print(result)
data = result['data']

ticker_url_pairs = {}
for currency in data:
    symbol = currency['symbol']
    url = currency['id']
    name = currency['name']
    ticker_url_pairs[symbol] = (url,name)

# print(ticker_url_pairs)
# print(len(ticker_url_pairs))

limit = len(ticker_url_pairs)
start = 1
# sort = 'name'









#get the specific cryptocurrency data from ticker symbol

while True:

    choice = input('Enter the ticker symbol of a cryptocurrency: ')
    choice = choice.upper()
    id = ticker_url_pairs.get(choice)
    if id == None:
        print('ticker not found. Please try again')
        continue

#     ticker_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?&sort=name' +'&convert=USD'
#     ticker_url += '&limit=' + str(limit) + '&start=' + str(start)

        
    ticker_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?&' +'&convert=USD'
    ticker_url += '&limit=' + str(limit) + '&start=' + str(start)
    request = requests.get(ticker_url,headers= headers)
    result = request.json()
    
    currency = result['data']
    # print(currency[0]['name'])
    for i in range(len(currency)):
        if currency[i]['symbol'] == choice:
            search = currency[i]

    rank = search['cmc_rank']
    name = search['name']
    symbol = search['symbol']

    circulating_supply = int(search['circulating_supply'])
    total_supply = int(search['total_supply'])

    quotes = search['quote'][convert]
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
    print('Percentage of coins in circulation: ' + str(int(circulating_supply / total_supply * 100)))
    print()

    choice = input('Again? (y/n): ')

    if choice == 'n':
        break
