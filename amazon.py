#Importing the necessary libraries and modules
from urllib.request import Request, urlopen
import requests
from bs4 import BeautifulSoup
import csv
import re
import pandas as pd
import numpy as np
from time import sleep
from random import randint
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://www.amazon.co.uk/'
driver.get(url)

def get_url(search_term):
    temp1 = 'https://www.amazon.co.uk/s?k={}&ref=nb_sb_ss_pltr-ranker-retrain-acsession-opsacceptance_3_17'
    temp = 'https://www.amazon.co.uk/s?k={}&ref=nb_sb_ss_pltr-ranker-retrain-acsession-opsacceptance_2_6'
    search_term = search_term.replace(' ', '+')
    return temp1.format(search_term)


url = get_url('smart tv')
url1 = get_url('computer accessory')

url = 'https://www.amazon.ca/Sony-WF-1000XM3-Industry-Canceling-Wireless/product-reviews/B07T81554H/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
# Option 1
r = requests.get('http://localhost:8050/render.html', params = {'url': url, 'wait' : 2})
# Option 2
# r = requests.get(url)

# Parsing the HTML content
soup = BeautifulSoup(r.text, 'html.parser')

# Getting desired data from our parsed soup
reviews = soup.find_all('div', {'data-hook': 'review'})

# Initialize list
data = []

# For every item in review, scrape the following and store as a list called review
for item in reviews:
    review = {
    'product': soup.title.text.replace('Amazon.ca:Customer reviews: ', '').strip(), 
    'title': item.find('a', {'data-hook': 'review-title'}).text.strip(),
    'date': item.find('span', {'data-hook': 'review-date'}).text.strip(),
    'rating': float(item.find('i', {'data-hook': 'review-star-rating'}).text.replace('out of 5 stars', '').strip()),
    'text': item.find('span', {'data-hook': 'review-body'}).text.strip(),
    }
    data.append(review)  

# Save results to a dataframe, then export as CSV
df = pd.DataFrame(data)
df.to_csv(r'sony-headphones.csv', index=False)