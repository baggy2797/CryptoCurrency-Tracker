import json
import requests

listings_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '914cdba8-1a06-439a-8fd1-071d02e187f5',
}


request = requests.get(listings_url,headers= headers)
result = request.json()


print(json.dumps(result, sort_keys=True, indent=4))

data = result['data']

for currency in data:
    rank = currency['id']
    name = currency['name']
    symbol = currency['symbol']
    print(str(rank) + ': ' + name + '({})'.format(symbol))
