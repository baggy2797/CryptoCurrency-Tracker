import xlsxwriter
import requests
import json

start = 1
row = 1

crypto_workbook = xlsxwriter.Workbook('cryptocurrencies.xlsx')
crypto_sheet = crypto_workbook.add_worksheet()

crypto_sheet.write('A1', 'Name')
crypto_sheet.write('B1', 'Symbol')
crypto_sheet.write('C1', 'Market Cap')
crypto_sheet.write('D1', 'Price')
crypto_sheet.write('E1', '24H Volume')
crypto_sheet.write('F1', 'Hour Change')
crypto_sheet.write('G1', 'Day Change')
crypto_sheet.write('H1', 'Week Change')


#from the API documentation
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '914cdba8-1a06-439a-8fd1-071d02e187f5',
}


for i in range(10):
    ticker_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?&start=' + str(start)
    request = requests.get(ticker_url,headers = headers)
    results = request.json()
    # print(results)
    data = results['data']

    for currency in data:
        rank = currency['cmc_rank']
        name = currency['name']
        symbol = currency['symbol']
        quotes = currency['quote']['USD']
        market_cap = quotes['market_cap']
        hour_change = quotes['percent_change_1h']
        day_change = quotes['percent_change_24h']
        week_change = quotes['percent_change_7d']
        price = quotes['price']
        volume = quotes['volume_24h']

        crypto_sheet.write(row,0,name)
        crypto_sheet.write(row,1,symbol)
        crypto_sheet.write(row,2,str(market_cap))
        crypto_sheet.write(row,3,str(price))
        crypto_sheet.write(row,4,str(volume))
        crypto_sheet.write(row,5,str(hour_change))
        crypto_sheet.write(row,6,str(day_change))
        crypto_sheet.write(row,7,str(week_change))

        row +=1

    start += 100

crypto_workbook.close()