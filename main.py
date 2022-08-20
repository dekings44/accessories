#importing the libraries needed 
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint

#Declaring the headers 
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

#declaring the list of empty variables, So that we can append the data overall

acc_name = []
rating = []
total_rating=[]
price_whole=[]
price_dec =[]


#creating an array of values and passing it in the url for dynamic webpages
pages = np.arange(1,20,1)

#the whole core of the script
for page in pages:
    page = requests.get("https://www.amazon.co.uk/s?k=computer+accessory&page="+str(page)+"&crid=35AY920YDA85G&qid=1660999890&sprefix=%2Caps%2C71&ref=sr_pg_2")
    soup = BeautifulSoup(page.text, 'html.parser')
    acc_data = soup.findAll('div', attrs = {'data-component-type': 's-search-result'})
    sleep(randint(2,8))
    for store in acc_data:
        name = store.find('span', {'class' : 'a-size-medium a-color-base a-text-normal'}).text
        acc_name.append(name)
        
        acc_rating = store.find('span', {'class' : 'a-icon-alt'})
        rating.append(acc_rating)
        
        acc_total_rating = store.find('span', {'class' : 'a-size-base s-underline-text'})
        total_rating.append(acc_total_rating)
        
        acc_price_whole = store.find('span', {'class' : 'a-price-whole'})
        price_whole.append(acc_price_whole)
        
        acc_price_dec = store.find('span', {'class' : 'a-price-fraction'})
        price_dec.append(acc_price_dec)
        
        
#creating a dataframe 
acc_list = pd.DataFrame({ "Name": acc_name, "Rating" : rating, "Total Rating": total_rating, "Price Pounds": price_whole, "Price Pence" : price_dec})

print(acc_list.head())
print(len(acc_list))

acc_list.to_csv('amazon.csv', index = None)
