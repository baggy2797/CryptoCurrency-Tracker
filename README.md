# CryptoCurrency-Tracker

<h1 align="center">Welcome to CryptoTracker 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://twitter.com/bhaditya" target="_blank">
    <img alt="Twitter: bhaditya" src="https://img.shields.io/twitter/follow/bhaditya.svg?style=social" />
  </a>
</p>


<img align ="center" src ="https://user-images.githubusercontent.com/26450952/116924701-3bfb6d00-ac26-11eb-91ed-e4a40b0644a8.gif" >

```
5 real world applications, by using The 🐍Python 3.8.2✅ and the 💰CoinMarketCap.com API✅

📢📢📢 WHAT TO LEARN 📢📢📢
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
<img src="https://img.shields.io/badge/BTC-Bitcoin-brightgreen?link=https://coinmarketcap.com/"><img src="https://img.shields.io/badge/ETH-Ethereum-red?link=https://coinmarketcap.com/"><img src="https://img.shields.io/badge/BNB-Binance%20Coin-orange?link=https://coinmarketcap.com/"><img src="https://img.shields.io/badge/XRP-XRP-lightgrey?link=https://coinmarketcap.com/"><img src="https://img.shields.io/badge/DOGE-DogeCoin-yellow?link=https://coinmarketcap.com/"><img src="https://img.shields.io/badge/USDT-Tether-yellowgreen?link=https://coinmarketcap.com/"><img src="https://img.shields.io/badge/LTC-LiteCoin-green?link=https://coinmarketcap.com/"><img src="https://img.shields.io/badge/other-other-blue?link=https://coinmarketcap.com/">


# Synopsis
This repository contains the files and codes upon following udemy course [Python and Cryptocurrency: Build 5 Real World Applications](https://www.udemy.com/coinmarketcap/).
CoinMarketCap API endpoints are used to access live cryptocurrency data for creating 5 simple cryptocurrency applications that running in CLI fashion.

# Why learn the CoinMarketCap API?

- It contains most up-to-date cryptocurrency information.
- Using the API is a breeze once you learn these tools.
- Many global currencies such as GBP and JPY are supported and used here.
- The CoinMarketCap API v2 is an improvement upon an API which is already great.

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

# Note :![tenor](https://user-images.githubusercontent.com/26450952/116926194-1a9b8080-ac28-11eb-9391-78166dfc853f.gif)

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

# Installing the required libraries

After creating the virtual environment, all we need to do is install the required libraries into the folder where the /api and /projects are stored. Move to the directory where the projects and api are stored and then start installing the libraries:

Upgrade Pip first:
```
$ python -m pip --version
pip X.Y.Z from .../site-packages/pip (python X.Y)
```

pip is just a PyPI package like any other; you could use it to upgrade itself the same way you would upgrade any package:
```
pip install --upgrade pip
```
On Windows the recommended command is:
```
python -m pip install --upgrade pip
```
Then start with the libraries:
```
pip install os 
pip install json 
pip install requests 
pip install datetime 
pip install prettytable 
pip install colorama
pip install math 
pip install locale 
pip install xlsxwriter 
```


# Projects
Sr.No. |Project Description|
---|---|
1|[A Real-Time Price Alert App](https://github.com/baggy2797/CryptoCurrency-Tracker/blob/main/projects/coincap_cryptoalert.py)|
2|[A Cryptocurrency Portfolio App](https://github.com/baggy2797/CryptoCurrency-Tracker/blob/main/projects/coincap_cryptocurrencyportfolio.py)|
3|[Store Real-Time Information on 1000 Cryptocurrencies in Excel Using Python](https://github.com/baggy2797/CryptoCurrency-Tracker/blob/main/projects/coincap_excelwriter.py)|
4|[Predict The Future Values of the Top 100 Cryptocurrencies](https://github.com/baggy2797/CryptoCurrency-Tracker/blob/main/projects/coincap_futurevalues.py)|
5|[A Top 100 Cryptocurrency Ranking App](https://github.com/baggy2797/CryptoCurrency-Tracker/blob/main/projects/coincap_top100Crypto.py)|

[Click Me for all the projects!](https://github.com/baggy2797/CryptoCurrency-Tracker/tree/main/projects)

## Project Description

### [A Real-Time Price Alert App](https://github.com/baggy2797/CryptoCurrency-Tracker/blob/main/projects/coincap_cryptoalert.py)
Get notified when cryptocurrencies hit certain prices in USD. You can keep this program running in the background. Your computer will shout things like, 'Litecoin hit $1200!'.

### [A Cryptocurrency Portfolio App](https://github.com/baggy2797/CryptoCurrency-Tracker/blob/main/projects/coincap_cryptocurrencyportfolio.py)
Track all of your crypto assets with ease. See the total value of all your crypto assets combined along with detailed information about each one. Positive and negative values are color coated green and red.

### [Store Real-Time Information on 1000 Cryptocurrencies in Excel Using Python](https://github.com/baggy2797/CryptoCurrency-Tracker/blob/main/projects/coincap_excelwriter.py)
Learn to store cryptocurrency information inside of excel workbooks using Python.

### [Predict The Future Values of the Top 100 Cryptocurrencies](https://github.com/baggy2797/CryptoCurrency-Tracker/blob/main/projects/coincap_futurevalues.py)
Explore what the price of cryptocurrencies will be if the global market cap hits certain levels (such as world stock market levels)

### [A Top 100 Cryptocurrency Ranking App](https://github.com/baggy2797/CryptoCurrency-Tracker/blob/main/projects/coincap_top100Crypto.py)
Sort by rank, daily percentage change, or daily volume. Positive and negative values are color coated green and red.

# Documentation
https://coinmarketcap.com/api/documentation/v1/

## Author

👤 **Aditya Nitin Bhagwat**

* Website: baggy2797.github.io
* Twitter: [@bhaditya](https://twitter.com/bhaditya)
* Github: [@baggy2797](https://github.com/baggy2797)
* LinkedIn: [@adibhagwat](https://linkedin.com/in/adibhagwat)

## Show your support

Give a ⭐️ if this project helped you!

***
