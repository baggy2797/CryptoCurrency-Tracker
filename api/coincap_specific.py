import json
import requests

convert = 'USD'
listings_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
url_end = '&convert=' + convert

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '914cdba8-1a06-439a-8fd1-071d02e187f5',
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

####################################################################################################################################################################################################################################################################################
# import json
# import requests
# from requests.api import head

# convert = 'USD'
# listings_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
# url_end = '&convert=' + convert



# temp_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/map"
# headers = {
#     'Accepts': 'application/json',
#     'X-CMC_PRO_API_KEY': '914cdba8-1a06-439a-8fd1-071d02e187f5',
#     }


# req_temp = requests.get(temp_url,headers = headers)
# res_temp = req_temp.json()


# pairs = {}
# d = (res_temp['data'])
# for i in range(len(d)):
#     pairs[d[i]['symbol']] = (d[i]['rank'],d[i]['id'])


# request = requests.get(listings_url,headers = headers)
# result = request.json()

# data = result['data']

# ticker_url_pairs = {}
# for currency in data:
#     symbol = currency['symbol']
#     url = currency['id']
#     ticker_url_pairs[symbol] = url

# # print(ticker_url_pairs)
# # print(len(ticker_url_pairs))

# while True:

#     choice = input('Enter the ticker symbol of a cryptocurrency: ')
#     choice = choice.upper()
#     id = ticker_url_pairs.get(choice)
    
#     new_id = pairs.get(choice)
#     sSymbol = choice
#     search = new_id[1]
#     # print(id)
    
#     if search == None:
#         print('ticker not found. Please try again')
#         continue
        
#     # if id == None:
#     #     print('ticker not found. Please try again')
#     #     continue
    
#     limit = 1
#     start = search
#     ticker_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?&sort=symbol&' +'&limit=' + str(limit) + '&start=' + str(start)+ url_end
#     request = requests.get(ticker_url,headers=headers)
#     result = request.json()
    
#     print(result['data'])
    
#     # if result['data']:
#     #     temp = result['data']
    
#     # currency = result['data'][0]

#     # rank = currency['cmc_rank']
#     # name = currency['name']
#     # symbol = currency['symbol']

#     # circulating_supply = int(currency['circulating_supply'])
#     # total_supply = int(currency['total_supply'])

#     # quotes = currency['quote'][convert]
#     # market_cap = quotes['market_cap']
#     # hour_change = quotes['percent_change_1h']
#     # day_change = quotes['percent_change_24h']
#     # week_change = quotes['percent_change_7d']
#     # price = quotes['price']
#     # volume = quotes['volume_24h']

#     # volume_string = '{:,}'.format(volume)
#     # market_cap_string = '{:,}'.format(market_cap)
#     # circulating_supply_string = '{:,}'.format(circulating_supply)
#     # total_supply_string = '{:,}'.format(total_supply)

#     # print(str(rank) + ': ' + name + ' (' + symbol + ')')
#     # print('Market cap: \t\t$' + market_cap_string)
#     # print('Price: \t\t\t$' + str(price))
#     # print('24h Volume: \t\t$' + volume_string)
#     # print('Hour change: \t\t' + str(hour_change) + '%')
#     # print('Day change: \t\t' + str(day_change) + '%')
#     # print('Week change: \t\t' + str(week_change) + '%')
#     # print('Total supply: \t\t' + total_supply_string)
#     # print('Circulating supply: \t' + circulating_supply_string)
#     # print('Percentage of coins in circulation: ' + str(int(circulating_supply / total_supply * 100)))
#     # print()

#     choice = input('Again? (y/n): ')

#     if choice == 'n':
#         break

# # string
# # Optionally calculate market quotes by CoinMarketCap ID instead of symbol. This option is identical to convert outside of ID format. Ex: convert_id=1,2781 would replace convert=BTC,USD in your query. This parameter cannot be used when convert is used.

# # Optionally calculate market quotes in up to 120 currencies at once by passing a comma-separated list of cryptocurrency or fiat currency symbols. Each additional convert option beyond the first requires an additional call credit. A list of supported fiat options can be found here. Each conversion is returned in its own "quote" object.