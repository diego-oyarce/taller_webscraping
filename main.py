from bs4 import BeautifulSoup
import requests
import unicodedata
import pandas as pd

#webpage url
url =  'https://www.ensenachile.cl/testimonios/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)
#Encontrar los div que tienen class 'item-res' y 'i-res'
divs = soup.find_all('div',{'class':['col-md-6']})
for div in divs:
    #find all the enclosing a tags
    print(div)