import requests
from bs4 import BeautifulSoup
from numismatic_value_scraper import coin_price
from silver_price_scraper import get_silver_price


#TODO add error handling


mercury_url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=mercury+dime&_sacat=0&_sop=1'

#think about getting rid of the default paramter
def ending_soonest(_results = requests.get(mercury_url)):

    html = BeautifulSoup(_results.text, "html.parser")

    search = 'class="s-item__time-left">'

    location = str(html).find(search)


    time = str(html)[location+len(search):(location+len(search)+3)]

    return time.strip()


#two optional parameters defualt fetches from ebay, second number of minutes left
def check_time(_time = ending_soonest(), _time_constraint = 10):
    if _time[-1:] == 's':
        return True
    elif _time[-1:] == 'm':
        if int(_time[0:-1]) < _time_constraint:
            return True
    else:
        return False


'''
put this function on the back plate and make a dedicated check price function come back to this when your ready to make a function that combines all these functions
def check_price(_results = requests.get(mercury_url),_number_of_coins = 1, _time_constraint = 1):
    html = BeautifulSoup(_results.text, "html.parser")

    if check_time(ending_soonest(_results),1) == False:
        print('works')
        return None
    return 0
'''
#pass the requests.get function in from function above
def check_price(_results):
    html = BeautifulSoup(_results.text, "html.parser")

    search = 'class="s-item__price">$'

    #location = str(html).find(search)
    location = find_string(str(html),search)

#TODO clean this up with the numbers make more dynamic
    price = str(html)[location+23:(location+27)]

    return float(price)
#see https://www.geeksforgeeks.org/python-ways-to-find-nth-occurrence-of-substring-in-a-string/
def find_string(txt, str1):
	return txt.find(str1, txt.find(str1)+1)

