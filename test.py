import requests
from bs4 import BeautifulSoup
import csv
import re
import pandas as pd
import numpy as np
from time import sleep
from random import randint

def get_url(search_term):
    temp1 = 'https://www.amazon.co.uk/s?k={}&ref=nb_sb_ss_pltr-ranker-retrain-acsession-opsacceptance_3_17'
    temp = 'https://www.amazon.co.uk/s?k={}&ref=nb_sb_ss_pltr-ranker-retrain-acsession-opsacceptance_2_6'
    search_term = search_term.replace(' ', '+')
    return temp.format(search_term)


url = get_url('smart tv')

print(url)

header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
req = requests.get(url, headers = header).text

soup = BeautifulSoup(req, 'html5lib')
print(soup)
print(type(soup))

# card = soup.find_all('span', {'class' : 'a-size-medium a-color-base a-text-normal'})

# name = [comp.text for comp in card]
# print(name)