url='https://kodesh.snunit.k12.il/i/t/t0101.htm'

from bs4 import BeautifulSoup as bs
# import pandas as pd
# pd.set_option('display.max_colwidth', 500)
import time
import requests
import random


page = requests.get(url)
# print(page)
soup = bs(page.content)
arr=soup.find_all(class_='mainTxt')

data=[]
data.extend([i.text for i in soup.find_all(class_='mainTxt')])
for i in data:
  print(i)
 