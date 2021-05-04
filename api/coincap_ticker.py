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
    'X-CMC_PRO_API_KEY': '914cdba8-1a06-439a-8fd1-071d02e187f5',
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












# import json
# import requests

# ticker_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'

# limit = 100
# start = 1
# sort = 'id'
# convert = 'USD'


# choice = input("Do you want to enter any custom parameters? (y/n): ")

# if choice == 'y':
#     limit = input('What is the custom limit?: ')
#     start = input('What is the custom start number?: ')
#     sort = input('What do you want to sort by?: ')
#     convert = input('What is your local currency?: ')

# ticker_url += '?&limit=' + str(limit) + '&sort=' + sort + '&start=' + str(start) + '&symbol=' + convert
# print(ticker_url)
# headers = {
#     'Accepts': 'application/json',
#     'X-CMC_PRO_API_KEY': '914cdba8-1a06-439a-8fd1-071d02e187f5',
# }

# request = requests.get(ticker_url,headers= headers)
# result = request.json()


# print(json.dumps(result,sort_keys=True,indent=4))

# import http.client
# import json
# import time
# import zlib


# def replace_nulls(json_elem):
# 	if isinstance(json_elem, list):
# 		return [replace_nulls(elem) for elem in json_elem]
# 	elif isinstance(json_elem, dict):
# 		return {key: replace_nulls(value) for key, value in json_elem.items()}
# 	else:
# 		return '0' if json_elem is None else json_elem

# class CoinMarketCap(object):
# 	def __init__(self, api_key):
# 		self.api_key = api_key
# 		self.cache   = {'global':dict(), 'ticker':dict()}
# 		self.last    = {'global':0     , 'ticker':0     }

# 	def _api(self, _endpoint):
# 		conn = http.client.HTTPSConnection('pro-api.coinmarketcap.com', timeout=15)
# 		conn.request('GET', '/v1/' + _endpoint, headers={'Accept':'application/json', 'Accept-Encoding':'deflate, gzip', 'X-CMC_PRO_API_KEY':self.api_key})
# 		response = zlib.decompress(conn.getresponse().read(), 16+zlib.MAX_WBITS).decode('utf-8').replace(': null', ': "0"')
# 		conn.close()
# 		return json.loads(response)['data']

# 	def _global(self):
# 		if time.time() - self.last['global'] < 300:
# 			return self.cache['global']
# 		else:
# 			data = self._api('global-metrics/quotes/latest')
# 			self.cache['global'] = {
# 				'cryptocurrencies' : data['active_cryptocurrencies'],
# 				'exchanges'        : data['active_exchanges'],
# 				'btc_dominance'    : int(data['btc_dominance']),
# 				'eth_dominance'    : int(data['eth_dominance']),
# 				'market_cap'       : int(data['quote']['USD']['total_market_cap']),
# 				'volume'           : int(data['quote']['USD']['total_volume_24h'])
# 			}
# 			self.last['global'] = time.time()
# 			return self.cache['global']

# 	def _ticker(self):
# 		if time.time() - self.last['ticker'] < 300:
# 			return self.cache['ticker']
# 		else:
# 			data = replace_nulls(self._api('cryptocurrency/listings/latest?limit=5000'))
# 			self.cache['ticker'] = dict()
# 			for item in data:
# 				self.cache['ticker'][item['id']] = {
# 					'name'       : item['name'],
# 					'symbol'     : item['symbol'],
# 					'slug'       : item['slug'],
# 					'rank'       : item['cmc_rank'],
# 					'price'      : float(item['quote']['USD']['price']),
# 					'percent'    : {'1h':float(item['quote']['USD']['percent_change_1h']), '24h':float(item['quote']['USD']['percent_change_24h']), '7d':float(item['quote']['USD']['percent_change_7d'])},
# 					'volume'     : int(float(item['quote']['USD']['volume_24h'])),
# 					'market_cap' : int(float(item['quote']['USD']['market_cap']))
#                     # 'circulating_supply' : 
# 				}
# 			self.last['ticker'] = time.time()
# 			return self.cache['ticker']



# # print(sortById(start,limit,fetchedResults))

# # print(sortByRank(start,limit,fetchedResults))





# # print(type(fetchedResults))

# import json
# # import requests

# while True:
#     # ticker_url = 'https://api.coinmarketcap.com/v2/ticker/?structure=array'
#     flag = 0
    
#     coinmarketcap = CoinMarketCap('914cdba8-1a06-439a-8fd1-071d02e187f5')
#     fetchedResults = coinmarketcap._ticker()
    
#     limit = 10
#     start = 1
#     sort = 'rank'
#     convert = 'USD'

#     choice = input("Do you want to enter any custom parameters? (y/n): ")

#     if choice == 'y':
#         limit = input('What is the custom limit?: ')
#         start = input('What is the custom start number?: ')
#         sort = input('What do you want to sort by?: ')
#         # convert = input('What is your local currency?: ')
    
#     if sort =="rank":
#         data = sortByRank(start,limit,fetchedResults)
#         # print(data)
#     elif sort == "id":
#         data = sortById(start,limit,fetchedResults)
#         # print(data)
#     else:
#         print("Enter 'id' or 'rank' as the sorting condition")
#         flag = 1
    
#     if flag == 0:
#         # data = results['data']

#         print(type(data))
        # for key,value in data.items():
            
        #     rank = currency['rank']
        #     name = currency['name']
        #     symbol = currency['symbol']
        #     circulating_supply = int(currency['circulating_supply'])
        #     total_supply = int(currency['total_supply'])

        #     quotes = currency['quotes'][convert]
        #     market_cap = quotes['market_cap']
        #     hour_change = quotes['percent_change_1h']
        #     day_change = quotes['percent_change_24h']
        #     week_change = quotes['percent_change_7d']
        #     price = quotes['price']
        #     volume = quotes['volume_24h']

        #     volume_string = '{:,}'.format(volume)
        #     market_cap_string = '{:,}'.format(market_cap)
        #     circulating_supply_string = '{:,}'.format(circulating_supply)
        #     total_supply_string = '{:,}'.format(total_supply)

        #     print(str(rank) + ': ' + name + ' (' + symbol + ')')
        #     print('Market cap: \t\t$' + market_cap_string)
        #     print('Price: \t\t\t$' + str(price))
        #     print('24h Volume: \t\t$' + volume_string)
        #     print('Hour change: \t\t' + str(hour_change) + '%')
        #     print('Day change: \t\t' + str(day_change) + '%')
        #     print('Week change: \t\t' + str(week_change) + '%')
        #     print('Total supply: \t\t' + total_supply_string)
        #     print('Circulating supply: \t' + circulating_supply_string)
        #     print('Percentage of coins in circulation: ' + str(int(circulating_supply / total_supply * 100)))
        #     print()

        # choice = input('Again? (y/n): ')

        # if choice == 'n':
        #     break
        
        
# "name""symbol""date_added""market_cap""market_cap_strict""price""circulating_supply""total_supply""max_supply""num_market_pairs""volume_24h""percent_change_1h""percent_change_24h""percent_change_7d""market_cap_by_total_supply_strict""volume_7d""volume_