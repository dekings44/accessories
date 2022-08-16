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
    temp = 'https://www.amazon.co.uk/s?k={}&ref=nb_sb_ss_pltr-ranker-retrain-acsession-opsacceptance_2_6'
    search_term = search_term.replace(' ', '+')
    return temp.format(search_term)


url = get_url('smart tv')
url1 = get_url('computer accessory')

print(url)
print(url1)
# header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

# link = 'https://www.amazon.co.uk/iPhone-Charger-Cable-Lightning-Compatible/dp/B08F2NDB39?ref_=Oct_d_oup_d_560800&pd_rd_w=TtYu9&content-id=amzn1.sym.cf168abf-8d77-4933-98b1-3151f5974581&pf_rd_p=cf168abf-8d77-4933-98b1-3151f5974581&pf_rd_r=29D7F0H9VJZ4XKR3P81Q&pd_rd_wg=AsMvu&pd_rd_r=dc5ed78e-9d5d-434b-955b-92b1aeaaa3b5&pd_rd_i=B08F2NDB39'
# req = requests.get(link, headers = header).text
# soup = BeautifulSoup(req, 'html5lib')

# content = soup.find_all('div', {'id' : 'productTitle'})

# print(content)