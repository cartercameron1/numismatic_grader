import time
import requests
from numismatic_value_scraper import coin_price
from silver_price_scraper import get_silver_price
from mercury_scrapy import check_price
from mercury_scrapy import check_time
from mercury_scrapy import mercury_url

#TODO add a variable to loop so you can break under certain conditions an dyou can tell
#TODO add some sort of coin identifier if there are two coins you have to make it two coins worth of silver and so forth
while True:
    data_request = requests.get(mercury_url)
    silver_dictionary = get_silver_price()
    if check_time():
        print("true")
        if  check_price(data_request) < silver_dictionary['jm price']:
            print('deal')
    else:
        print('false')

    time.sleep(15)
