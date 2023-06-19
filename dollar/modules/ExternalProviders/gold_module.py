from bs4 import BeautifulSoup
from modules.Common.cache_settings_module import  cache_settings 
import requests
import re
import time
import json
from cachetools import cached, TTLCache
from modules.Common.config_texts import irarz_endpoint, navasan_endpoint,gold_ounce_endpoint



gold_prices = {"emami_coin": 0, "bahar_coin": 0, "half_coin": 0, "quarter_coin": 0, "gerami_coin": 0,
                 "18_carat_gold": 0, "24_carat_gold": 0, "global_gold_once": 0, "global_silver_once": 0, "gold_shekel": 0}


response = requests.get(irarz_endpoint)
html_document = response.text
soup = BeautifulSoup(html_document, 'html.parser')

def get_gold_price(spanid):
    pricediv = soup.find('span', attrs={'id': re.compile(spanid)})
    result = pricediv.text
    
    if("," in result):
       result = result.replace(',', '')
    if("\n" in result):
       result = result.replace('\n', '')
    if("\t" in result):
       result = result.replace('\t', '')   
    return int(result.strip())


@cached(cache_settings['gold_all_prices'])
def get_gold_all_prices():
    timestamp = int(time.time())
    response = requests.get(navasan_endpoint+str(timestamp))
    # *10000 for convert navasan pricing system to IRR
    gold_prices["emami_coin"] = format(extract_navasan_price_with_id(response.text, "sekkeh")*1000,',')
    gold_prices["bahar_coin"] = format(extract_navasan_price_with_id(response.text, "bahar")*1000,',')
    gold_prices["half_coin"] = format(extract_navasan_price_with_id(response.text, "nim")*1000,',')
    gold_prices["quarter_coin"] = format(extract_navasan_price_with_id(response.text, "rob")*1000,',')
    gold_prices["gerami_coin"] = format(extract_navasan_price_with_id(response.text, "gerami")*1000,',')
    gold_prices["18_carat_gold"] =  format(extract_navasan_price_with_id(response.text, "18ayar"),',')
    gold_prices["24_carat_gold"] = format(get_gold_price("^geram24")/10,',')
    gold_prices["global_gold_once"] = get_gold_Ounce_Price()
    gold_prices["global_silver_once"] = get_silver_Ounce_Price()
    gold_prices["gold_shekel"] = format(get_gold_price("^mesghal")/10,',')
    return gold_prices


@cached(cache_settings['OncePrice'])
def get_gold_Ounce_Price():
    response = requests.get(gold_ounce_endpoint)
    data = response.json()
    price = data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
    return price

@cached(cache_settings['SilverOuncePrice'])
def get_silver_Ounce_Price():
    response = requests.get(gold_ounce_endpoint.replace('XAU','XAG'))
    data = response.json()
    price = data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
    return price


@cached(cache_settings['BaharCoin'])
def getBaharCoinPrice():
    timestamp = int(time.time())
    response = requests.get(navasan_endpoint+str(timestamp))
    # *10000 for convert navasan pricing system to IRt
    return extract_navasan_price_with_id(response.text, "bahar")*10000

@cached(cache_settings['Gold18'])
def getGold18Price():
    response = requests.get(irarz_endpoint)
    html_document = response.text
    soup = BeautifulSoup(html_document, 'html.parser')
    pricediv = soup.find('span', attrs={'id': re.compile("^geram18")})
    intPrice = int(int(pricediv.text.replace(',', ''))/10)
    return format(intPrice,',')







def extract_navasan_price_with_id(dirty_json, eleman_key):
    substring = 'var yesterday ='
    start_index = dirty_json.index(substring)
    truncated_string = dirty_json[:start_index]
    # Remove the "var lastrates =" and ";" from the string
    json_data = truncated_string.replace(
        "var lastrates = ", "").replace(";", "")
    lastrates_dict = json.loads("{" + json_data.split("{", 1)[1])
    # remove comma from the value
    symbol_price = lastrates_dict[eleman_key]["value"].replace(",", "")
    return int(symbol_price)
