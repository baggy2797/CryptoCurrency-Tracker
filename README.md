# CryptoCurrency-Tracker

<img align ="center" src ="https://user-images.githubusercontent.com/26450952/116924701-3bfb6d00-ac26-11eb-91ed-e4a40b0644a8.gif" >

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

🌎🌎🌎 API link :  https://coinmarketcap.com/api/ 🌎🌎🌎
```
<img src="https://img.shields.io/badge/BTC-Bitcoin-brightgreen"><img src="https://img.shields.io/badge/ETH-Ethereum-red"><img src="https://img.shields.io/badge/BNB-Binance%20Coin-orange"><img src="https://img.shields.io/badge/XRP-XRP-lightgrey"><img src="https://img.shields.io/badge/DOGE-DogeCoin-yellow"><img src="https://img.shields.io/badge/USDT-Tether-yellowgreen"><img src="https://img.shields.io/badge/LTC-LiteCoin-green"><img src="https://img.shields.io/badge/other-other-blue">


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

Herein, just change the headers by putting in the API key you generate for your account from https://pro.coinmarketcap.com/login

![Screen Shot 2021-05-03 at 15 06 34](https://user-images.githubusercontent.com/26450952/116922591-98a95880-ac23-11eb-9081-44632acc54ca.jpg)


Update the header as :

```
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'ENTER-YOUR-NEWLY-GENERATED-API-KEY-HERE',
}
```

# Creating a Virtual Environment
The venv module provides support for creating lightweight “virtual environments” with their own site directories, optionally isolated from system site directories. Each virtual environment has its own Python binary (which matches the version of the binary that was used to create this environment) and can have its own independent set of installed Python packages in its site directories.

For creating one Follow the steps here : https://docs.python.org/3/library/venv.html


# Projects


# Documentation
https://coinmarketcap.com/api/documentation/v1/
