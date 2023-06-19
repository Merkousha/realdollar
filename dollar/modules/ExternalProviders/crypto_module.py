from bs4 import BeautifulSoup
import requests
import re
import time
from cachetools import cached
from modules.Common.cache_settings_module import cache_settings
from modules.Common.logging_config import logger


irarz_endpoint = 'https://irarz.com/'
binance_endpoint = "https://api.binance.com/api/v3/ticker/price"
MAX_RETRIES = 3
RETRY_DELAY = 5

# List of cryptocurrencies to retrieve the current prices for
currencies = ['["BTCUSDT","ETHUSDT","BUSDUSDT","BNBBUSD","USDCBUSD","XRPUSDT"]',
              '["ADABUSD","DOGEUSDT","MATICUSDT","BUSDUSDT","SOLUSDT"]', 
              '["DOTUSDT","LTCUSDT","SHIBUSDT","TRXUSDT"]']


@cached(cache_settings['crypto'])
def get_crypto_all_prices():

    # Loop through each currency and retrieve its current price

    retries = 0
    while retries < MAX_RETRIES:
        try:
            merged_json = []
            for currency in currencies:
                params = {"symbols": currency}
                response = requests.get(binance_endpoint, params=params)
                merged_json += response.json()
                symbol_price = {d['symbol']: "{:.8f}".format(
                    float(d['price'])) for d in merged_json}
            return symbol_price
        except requests.exceptions.Timeout:
            retries += 1
            logger.error('binance time out: %s',
                         f'Retrying ({retries}/{MAX_RETRIES})...')
            time.sleep(RETRY_DELAY)
    logger.error(f'Failed to make request after {MAX_RETRIES} retries')


@cached(cache_settings['TetterPrice'])
def getTetterPrice():
    response = requests.get(irarz_endpoint)
    html_document = response.text
    soup = BeautifulSoup(html_document, 'html.parser')
    pricediv = soup.find('span', attrs={'id': re.compile("usdttmn")})
    intPrice = int(int(pricediv.text.replace(',', ''))/10)
    return format(intPrice, ',')
