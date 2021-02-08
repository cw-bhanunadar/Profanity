# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 21:39:20 2021

@author: bhanu
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

baseUrl = "https://www.youswear.com/index.asp?language="
languages = ["Bihari","Bangali","England","Urdu","Gujarati","Indian","Marathi","Panjabi"]

profaneWords = []
for language in languages:
    page = requests.get(baseUrl+language)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find('table', class_='table')
    rows = table.find_all('tr')
    print(language)
    for row in rows:
        td = row.find('td')
        if td is not None:
            profaneWords.append(td.text)
    
    print('completed')
        
df = pd.DataFrame(profaneWords)  
    
# saving the dataframe  
df.to_csv('youSwearWebsite.csv')  
