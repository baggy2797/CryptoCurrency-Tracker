import requests
import json
from requests.auth import HTTPBasicAuth
from datetime import datetime

# get data from globalURL
globalURL = "https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest"

#from the API documentation
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'YOUR-API-KEY-HERE',
}

request = requests.get(globalURL,headers = headers)
results = request.json()

print(json.dumps(results,sort_keys=True,indent =4))

active_currencies = results['data']['active_cryptocurrencies']
active_markets = results['data']['active_market_pairs']
bitcoin_percentage = results['data']['btc_dominance']
last_updated = results['data']['last_updated']
global_cap = int(results['data']['quote']['USD']['total_market_cap'])
global_volume = int(results['data']['quote']['USD']['total_volume_24h'])

active_currency_str = '{:,}'.format(active_currencies)
active_market_str = '{:,}'.format(active_markets)
bitcoin_percent_str = '{:,}'.format(bitcoin_percentage)
global_cap_str = '{:,}'.format(global_cap)
global_vol_str = '{:,}'.format(global_volume)


# last_updated_string = datetime.fromtimestamp(last_updated).strftime('%B %d, %Y at %I:%M%p')

print()
print('There are currently ' + active_currency_str + ' active cryptocurrencies and ' + active_market_str + ' active markets.')
print()
print('The global cap of all cryptos is '+ global_cap_str + ' and the 24h global volume is ' + global_vol_str + '.')
print()
print("Bitcoin's total percentage of the global cap is " + bitcoin_percent_str + '%.')
print()
print('The information was last updated on ' + last_updated + '.')
