import nltk, re, pprint
from nltk import word_tokenize

from urllib import request
url = "http://www.gutenberg.org/files/2554/old/8crmp10.txt"
response = request.urlopen(url)
raw = response.read().decode('ISO-8859-1')
print(type(raw))
print(len(raw))
print(raw[:75])

tokens = word_tokenize(raw)
print(type(tokens))
print(len(tokens))
print(tokens[:10])