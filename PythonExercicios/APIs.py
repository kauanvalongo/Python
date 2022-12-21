import requests
import json

cotacoes = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL')
cotacoes = cotacoes.json()

dolar = cotacoes['USDBRL']['bid']
euro = cotacoes['EURBRL']['bid']
bitcoin = cotacoes['BTCBRL']['bid']

print(f'1 dólar ta valendo - {dolar} ')
print(f'1 euro ta valendo - {euro} ')
print(f'1 bitcoin ta valendo - {bitcoin} ')