# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 12:20:48 2021

@author: bhanu
"""
from sklearn.model_selection import train_test_split
import pandas as pd

data = pd.read_csv('data_set.csv')
train, test = train_test_split(data, test_size=0.2)
train.to_csv("train_data.csv")
test.to_csv("test_data.csv")