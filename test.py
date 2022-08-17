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
# print(soup)
# print(type(soup))

# Gettig The names of the accessories
card = soup.find_all('span', {'class' : 'a-size-medium a-color-base a-text-normal'})

name = [comp.text for comp in card]
print(name)

#Getting the ratings of each accessory
rating = soup.find_all('span', {'class' : 'a-icon-alt'})
rating = [comp.text for comp in rating]
print(rating)

#Getting the total rating of each accessory
total_rating = soup.find_all('span', {'class' : 'a-size-base s-underline-text'})
total_rating = [comp.text for comp in total_rating]
print(total_rating)


#Getting the pounds side of the price
price_whole = soup.find_all('span', {'class' : 'a-price-whole'})
price_whole = [comp.text for comp in price_whole]
print(price_whole)

#Getting the pence side of the price
price_dec = soup.find_all('span', {'class' : 'a-price-fraction'})
price_dec = [comp.text for comp in price_dec]
print(price_dec)


#Getting the image of the accessory
# images = soup.find_all('img', {'class' : 's-image'})
# images = [comp.src for comp in images]
# print(images)