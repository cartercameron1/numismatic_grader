import yfinance as yf
import requests 


#urls:
jm_url = 'https://www.jmbullion.com'
xe_url = 'https://www.xe.com/'
apmex_url = 'https://www.apmex.com/silver-price'


#TODO change accesor dicitonary access to .get() 

#returns a dictionary containing the silver price from different sources and markets amoung other relevant info
def get_price():
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
    jm = requests.get(jm_url)
    if jm.status_code == 200:
        jm.encoding = 'utf-8'
        print(jm.text)
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
apmex = requests.get(apmex_url)
apmex.encoding = 'utf-8'

print(get_price())
