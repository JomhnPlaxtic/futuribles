#! usr/bin/env python3
# coding: utf-8

import pandas as pd

dataframe = pd.read_csv('futuribles_articles.csv', sep=";", encoding='ISO-8859-1')


i = 0
li = []
while i < len(dataframe):
    li.append(i)
    i += 1

print(li)

dataframe.index[li]

print(dataframe)
