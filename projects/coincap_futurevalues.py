import math
import json
import requests
import locale # add a comma to a large number (every third decimal place)
from prettytable import PrettyTable

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

global_url = 'https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest'
ticker_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

#from the API documentation
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'YOUR-API-KEY-HERE',
}


request = requests.get(global_url,headers= headers)
result = request.json()
data = result['data']
global_cap = int(data['quote']['USD']['total_market_cap'])

table = PrettyTable(['name',
                    'ticker',
                    '% of total global cap',
                    'Current',
                    '7.7T (Gold)',
                    '36.8T (Narrow Money)',
                    '73T (World Stock  markets)',
                    '90.4T (Broad Money)',
                    '217T (Real Estate)',
                    '544T (Derivatives)'])

request = requests.get(ticker_url,headers=headers)
result = request.json()
data =  result['data']

for currency in data:
    name = currency['name']
    ticker = currency['symbol']
    percentage_of_global_cap = float(currency['quote']['USD']['market_cap'])/float(global_cap)

    current_price = round(float(currency['quote']['USD']['price']),2)
    available_supply = float(currency['total_supply'])

    trillion7price = round(77*(10**12)* percentage_of_global_cap/available_supply,2)
    trillion36price = round(36.8*(10**12)* percentage_of_global_cap/available_supply,2)
    trillion73price = round(73*(10**12)* percentage_of_global_cap/available_supply,2)
    trillion90price = round(90.4*(10**12)* percentage_of_global_cap/available_supply,2)
    trillion217price = round(217*(10**12)* percentage_of_global_cap/available_supply,2)
    trillion544price = round(544*(10**12)* percentage_of_global_cap/available_supply,2)

    percentage_of_global_cap_string = str(round(percentage_of_global_cap*100,2)) + '%'
    current_price_string = '$' + str(current_price)
    trillion7price_string = '$' + locale.format_string('%.2f',trillion7price,True)
    trillion36price_string = '$' + locale.format_string('%.2f',trillion36price,True)
    trillion73price_string = '$' + locale.format_string('%.2f',trillion73price,True)
    trillion90price_string = '$' + locale.format_string('%.2f',trillion90price,True)
    trillion217price_string = '$' + locale.format_string('%.2f',trillion217price,True)
    trillion544price_string = '$' + locale.format_string('%.2f',trillion544price,True)

    table.add_row([name,
                    ticker,
                    percentage_of_global_cap_string,
                    current_price_string,
                    trillion7price_string,
                    trillion36price_string,
                    trillion73price_string,
                    trillion90price_string,
                    trillion217price_string,
                    trillion544price_string])

print()
print(table)
print()
