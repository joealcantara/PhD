import numpy as np 
import pandas as pd 
import matplotlib as plt

train = pd.read_csv('~/Documents/Data/HomeCredit/application_train.csv')
test = pd.read_csv('~/Documents/Data/HomeCredit/application_test.csv')

pd.set_option('display.max_colwidth', -1)
# print(train.head())
# print('-' * 40)
# print(test.head())

print(list(train))