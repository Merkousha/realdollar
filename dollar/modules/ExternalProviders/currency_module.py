from bs4 import BeautifulSoup
import json
import time
import requests
import re
from cachetools import cached, TTLCache
from modules.Common.cache_settings_module import  cache_settings 
from modules.Common.config_texts import irarz_endpoint, navasan_endpoint



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

@cached(cache_settings['BazarDollar'])
def getBazarDollarPrice():
    timestamp = int(time.time())
    response = requests.get(navasan_endpoint+str(timestamp))
    intPrice = extract_navasan_price_with_id(response.text, "usd_sell")
    return intPrice



def get_navasan_dollar_price():
    timestamp = int(time.time())
    response = requests.get(navasan_endpoint+str(timestamp))
    intPrice = extract_navasan_price_with_id(response.text, "usd_sell")
    return intPrice


@cached(cache_settings['UAEDirham'])
def getUAEDirhamPrice():
    timestamp = int(time.time())
    response = requests.get(navasan_endpoint+str(timestamp))
    intPrice = extract_navasan_price_with_id(response.text, "aed_sell")
    return format(intPrice,',')


@cached(cache_settings['TurkeyLear'])
def getTurkeyLearPrice():
    response = requests.get(irarz_endpoint)
    html_document = response.text
    soup = BeautifulSoup(html_document, 'html.parser')
    pricediv = soup.find('span', attrs={'id': re.compile("^price_try")})
    intPrice = int(int(pricediv.text.replace(',', ''))/10)
    return format(intPrice,',')


@cached(cache_settings['EuroPrice'])
def getEuroPrice():
    response = requests.get(irarz_endpoint)
    html_document = response.text
    soup = BeautifulSoup(html_document, 'html.parser')
    pricediv = soup.find('span', attrs={'id': re.compile("^price_eur")})
    intPrice = int(int(pricediv.text.replace(',', ''))/10)
    return format(intPrice,',')


@cached(cache_settings['PoundPrice'])
def getPoundPrice():
    response = requests.get(irarz_endpoint)
    html_document = response.text
    soup = BeautifulSoup(html_document, 'html.parser')
    pricediv = soup.find('span', attrs={'id': re.compile("^price_gbp")})
    intPrice = int(int(pricediv.text.replace(',', ''))/10)
    return format(intPrice,',')


@cached(cache_settings['harat_dollar'])
def get_harat_dollar_price():
    response = requests.get(irarz_endpoint)
    html_document = response.text
    soup = BeautifulSoup(html_document, 'html.parser')
    pricediv = soup.find('span', attrs={'id': re.compile("^afghan_usd")})
    intPrice = int(int(pricediv.text.replace(',', ''))/10)
    return intPrice


@cached(cache_settings['iri_gov_dollar'])
def iri_gov_dollar_price():
    response = requests.get(irarz_endpoint)
    html_document = response.text
    soup = BeautifulSoup(html_document, 'html.parser')
    pricediv = soup.find('span', attrs={'id': re.compile("^bank_usd")})
    intPrice = int(int(pricediv.text.replace(',', ''))/10)
    return intPrice


@cached(cache_settings['iri_gov_euro'])
def iri_gov_euro_price():
    response = requests.get(irarz_endpoint)
    html_document = response.text
    soup = BeautifulSoup(html_document, 'html.parser')
    pricediv = soup.find('span', attrs={'id': re.compile("^bank_eur")})
    intPrice = int(int(pricediv.text.replace(',', ''))/10)
    return intPrice

@cached(cache_settings['iraq_dinar'])
def iraq_dinar_price():
    response = requests.get(irarz_endpoint)
    html_document = response.text
    soup = BeautifulSoup(html_document, 'html.parser')
    pricediv = soup.find('span', attrs={'id': re.compile("^price_iqd")})
    intPrice = int(int(pricediv.text.replace(',', ''))/10)
    return intPrice


@cached(cache_settings['kuwait_dinar'])
def kuwait_dinar_price():
    response = requests.get(irarz_endpoint)
    html_document = response.text
    soup = BeautifulSoup(html_document, 'html.parser')
    pricediv = soup.find('span', attrs={'id': re.compile("^price_kwd")})
    intPrice = int(int(pricediv.text.replace(',', ''))/10)
    return intPrice


@cached(cache_settings['canada_dollar'])
def canada_dollar_price():
    response = requests.get(irarz_endpoint)
    html_document = response.text
    soup = BeautifulSoup(html_document, 'html.parser')
    pricediv = soup.find('span', attrs={'id': re.compile("^price_cad")})
    intPrice = int(int(pricediv.text.replace(',', ''))/10)
    return intPrice


@cached(cache_settings['australia_dollar'])
def australia_dollar_price():
    response = requests.get(irarz_endpoint)
    html_document = response.text
    soup = BeautifulSoup(html_document, 'html.parser')
    pricediv = soup.find('span', attrs={'id': re.compile("^price_aud")})
    intPrice = int(int(pricediv.text.replace(',', ''))/10)
    return intPrice


cached(cache_settings['russia_rubl'])
def russia_rubl_price():
    response = requests.get(irarz_endpoint)
    html_document = response.text
    soup = BeautifulSoup(html_document, 'html.parser')
    pricediv = soup.find('span', attrs={'id': re.compile("^price_rub")})
    intPrice = int(int(pricediv.text.replace(',', ''))/10)
    return intPrice


cached(cache_settings['china_yuann'])
def china_yuann_price():
    response = requests.get(irarz_endpoint)
    html_document = response.text
    soup = BeautifulSoup(html_document, 'html.parser')
    pricediv = soup.find('span', attrs={'id': re.compile("^price_cny")})
    intPrice = int(int(pricediv.text.replace(',', ''))/10)
    return intPrice    

cached(cache_settings['saudi_rial'])
def saudi_rial_price():
    response = requests.get(irarz_endpoint)
    html_document = response.text
    soup = BeautifulSoup(html_document, 'html.parser')
    pricediv = soup.find('span', attrs={'id': re.compile("^price_sar")})
    intPrice = int(int(pricediv.text.replace(',', ''))/10)
    return intPrice  

cached(cache_settings['omman_rial'])
def omman_rial_price():
    response = requests.get(irarz_endpoint)
    html_document = response.text
    soup = BeautifulSoup(html_document, 'html.parser')
    pricediv = soup.find('span', attrs={'id': re.compile("^price_omr")})
    intPrice = int(int(pricediv.text.replace(',', ''))/10)
    return intPrice  
