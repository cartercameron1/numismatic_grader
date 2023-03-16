import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

#data urls
USA_COINBOOK_URL = 'https://www.usacoinbook.com/coins/dimes/mercury/'



#relevant functions

#takes year and mint location and converts it to a format readable by the data fram
def to_column(_year, _mint):
    formated_string = str(_year) + ' ' + _mint.upper()
    return formated_string




#generates a pandas datafram of all mercury dimes
def generate_frame(html = requests.get(USA_COINBOOK_URL)):

    if html.status_code == 404:
        print('status code 404')

    soup = bs(html.text, features='lxml')

    tables = soup.find_all('table')

    table = soup.find('table', class_='footable')

    df = pd.DataFrame(columns=['Year', 'Details', 'Mintage', 'G', 'VG', 'F', 'VF', 'EF', 'AU', 'MS', 'MS65', 'PR', 'For Sale'])

    #see https://medium.com/geekculture/web-scraping-tables-in-python-using-beautiful-soup-8bbc31c5803e

    for row in table.tbody.find_all('tr'):
        columns = row.find_all('td')

        if columns != []:
            year = columns[0].text.strip()
            details = columns[1].text.strip()
            mintage = columns[2].text.strip()
            g = columns[3].text.strip()
            vg = columns[4].text.strip()
            f = columns[5].text.strip()
            vf = columns[6].text.strip()
            ef = columns[7].text.strip()
            au = columns[8].text.strip()
            ms = columns[9].text.strip()
            ms65 = columns[10].text.strip()
            pr = columns[11].text.strip()
            sale = ms65 = columns[12].text.strip()

        #TODO change to pandas.concat

        df = df.append({'Year': year, 'Details': details,'Mintage': mintage, 'G': g, 'VG': vg, 'F': f,'EF': ef, 'AU': au, 'MS':ms, 'MS65': ms65 , 'PR': pr, 'For Sale': sale}, ignore_index=True)

    return df.set_index('Year')





#returns the current year price given year and mint location parameter optional third parameter for condition
def coin_price(_year, _mint, df = generate_frame(), _condition = 'G'):

    try:
        coin = to_column(_year, _mint)
    except:
        print('invalid parameters to_columnt(int, char)')
        return '1'

    return df.at[coin, _condition]

print(generate_frame())
