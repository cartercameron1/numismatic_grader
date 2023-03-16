import yfinance as yf
import requests


#urls:
JM_URL = 'https://www.jmbullion.com'
XE_URL = 'https://www.xe.com/'
APMEX_URL = 'https://www.apmex.com/silver-price'


#TODO change accesor dicitonary access to .get() 

#returns a dictionary containing the silver price from different sources and markets amoung other relevant info
def get_silver_price():
    silver_info = {
            "comex futures": 0,
            'jm price': 0
            }

    #updates silver futers price
    try:
        silver_futures = yf.Ticker("SI=F")
        silver_info["comex futures"] = silver_futures.info['ask']
    except:
        print('unable to fetch comex futres')

    #update silver price from jm bullion
    try:
        silver_info['jm price'] = get_jm_price()
    except:
        print('unable to fetch jm bullion price')

    return silver_info



#TODO clean all the jm_price up


#request for price from jmbullion
def get_jm_price():
    jm = requests.get(JM_URL)
    if jm.status_code == 200:
        jm.encoding = 'utf-8'
        location = jm.text.find('Silver Ask')
        jm_price = jm.text[location:(location+47)]
        jm_price = jm_price[-5:]
        jm_price = float(jm_price)
        return jm_price
    elif jm.status_code == 404:
        print('JM bullion not found')
    return 0
#TODO Sadik use the jm model and do the same things for the following two sources
#mid market rate from XE

#prices from apmex

#TODO fix this warning
apmex = requests.get(APMEX_URL)
apmex.encoding = 'utf-8'

