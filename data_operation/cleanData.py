# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 16:39:39 2021

@author: bhanu
"""

import pandas as pd

"""data = pd.read_csv('bad_spam_word_list.csv') 
data = pd.read_excel('good_name.xlsx');
data['Is_spam'] = 0
data.to_csv('good_name_list.csv')"""

good_names = pd.read_csv('good_name_list.csv')
bad_names = pd.read_csv('bad_spam_word_list.csv')

data_set = good_names.append(bad_names)

data_set = data_set.sample(frac=1)

data_set.to_csv("data_set.csv")