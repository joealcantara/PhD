from nltk.book import *
# import random

# random.seed('1')

text6.similar("knights", num=50)

test1 = "enchanter made angnor back keepers snows gorge brain strength britons number dragon castle lady court glory union decision kingdom tale bosom yes nick roar one battle blood tops capital bridge son zoot ways manner book ferocity doors name cave dingo keeper the king case army two"


test2 = "enchanter made strength bridge bosom glory the name book dragon tale dingo nick cave britons army zoot ferocity capital union king roar brain lady ways angnor tops court battle snows keeper decision kingdom son one yes blood case number manner gorge keepers castle doors back one"

words1 = test1.split()
words2 = test2.split()

print('Length of test1', len(words1))
print('Length of test2', len(words2))

intersect = set(words1) & set(words2)
print(sorted(intersect))
print(len(intersect))

import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils

