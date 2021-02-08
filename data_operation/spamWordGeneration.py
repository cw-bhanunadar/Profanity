# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 12:36:05 2021

@author: bhanu
"""

from RandomWordGenerator import RandomWord
import pandas as pd

words =[]
for i in range(0,50000):
    word = RandomWord(max_word_size=9,constant_word_size=False)
    words.append(word.generate())

df = pd.DataFrame(words)
df.to_csv("spamWordCreation.csv")