import math
import nltk, re, pprint
from nltk import word_tokenize, sent_tokenize
import datetime

def get_julian_datetime(date):
 
    # Ensure correct format
    if not isinstance(date, datetime.datetime):
        raise TypeError('Invalid type for parameter "date" - expecting datetime')
    elif date.year < 1801 or date.year > 2099:
        raise ValueError('Datetime must be between year 1801 and 2099')

    # Perform the calculation
    julian_datetime = 367 * date.year - int((7 * (date.year + int((date.month + 9) / 12.0))) / 4.0) + int(
        (275 * date.month) / 9.0) + date.day + 1721013.5 + (
                          date.hour + date.minute / 60.0 + date.second / math.pow(60,
                                                                                  2)) / 24.0 - 0.5 * math.copysign(
        1, 100 * date.year + date.month - 190002.5) + 0.5

    return julian_datetime

def wordCount(text):
    wordDict = {}
    for sentence in text:
        for entry in sentence:
            keyTitle = entry[1]
            if keyTitle not in wordDict:
                wordDict[keyTitle] = 1
            else:
                count = wordDict[keyTitle]
                count = count + 1
                wordDict[keyTitle] = count
    return wordDict

def meanLengthSentence(text):
    total_length = 0
    for sent in text:
        total_length = total_length+len(sent)
    return total_length / len(text)

def preprocess(text):
    sentences = sent_tokenize(text)
    sentences = [word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    return sentences

def percentage(count, total):
    return 100*count / total

def lexical_diversity(text):
    return len(set(text)) / len(text)

