# CryptoCurrency-Tracker
```
5 real world applications, by using The 🐍Python 3.8.2✅ and the 💰CoinMarketCap.com API✅

📢📢📢 WHAT YOU CAN TO LEARN 📢📢📢
© To use Python for cryptorurrencys. 🐍💯 + 💰💯©
📢 I use the following Python modules... 👨‍💻👨‍🎓
🔵 os ✅
🔵 json ✅
🔵 requests ✅
🔵 datetime ✅
🔵 prettytable ✅
🔵 colorama ✅
🔵 math ✅
🔵 locale ✅
🔵 xlsxwriter ✅

🌎🌎🌎 API link https://coinmarketcap.com/ 🌎🌎🌎
```

# Synopsis
This repository contains the files and codes upon following udemy course [Python and Cryptocurrency: Build 5 Real World Applications](https://www.udemy.com/coinmarketcap/).
CoinMarketCap API endpoints are used to access live cryptocurrency data for creating 5 simple cryptocurrency applications that running in CLI fashion.

# Crypto API
CoinMarketCap API are publicly accesible as url endpoints. The API endpoints we used are recently released as v2 which are:
1. /listings/
2. /ticker/
3. /ticker{id}/
4. /global/

These endpoints are updated every 5 minutes and are restricted to no more than 30 requests per minute. Click [here](https://coinmarketcap.com/api/) for respective API usage details.

# EndPoint Overview
Endpoint Category | Description |
--- | --- | 
| /cryptocurrency/*	| Endpoints that return data around cryptocurrencies such as ordered cryptocurrency lists or price and volume data.|
| /exchange/* |	Endpoints that return data around cryptocurrency exchanges such as ordered exchange lists and market pair data.|
| /global-metrics/* |	Endpoints that return aggregate market data such as global market cap and BTC dominance.|
| /tools/*	| Useful utilities such as cryptocurrency and fiat price conversions.|
| /blockchain/*	| Endpoints that return block explorer related data for blockchains.|
| /fiat/*|	Endpoints that return data around fiats currencies including mapping to CMC IDs.|
|/partners/*	| Endpoints for convenient access to 3rd party crypto data.|
|/key/* |	API key administration endpoints to review and manage your usage.|


Endpoint paths follow a pattern matching the type of data provided

|Endpoint Path	| Endpoint Type |	Description |
--- | --- | --- |
|*/latest	| Latest Market Data |	Latest market ticker quotes and averages for cryptocurrencies and exchanges.|
|*/historical	| Historical Market Data	|Intervals of historic market data like OHLCV data or data for use in charting libraries.|
|*/info	| Metadata |	Cryptocurrency and exchange metadata like block explorer URLs and logos.|
|*/map	| ID Maps |	Utility endpoints to get a map of resources to CoinMarketCap IDs.|

# Changing the API Call
```
 #This example uses Python 2.7 and the python-request library.

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'ENTER-YOUR-KEY-HERE',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
```
# Projects


# Documentation
https://coinmarketcap.com/api/documentation/v1/
