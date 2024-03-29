import re
import numpy as np
import pandas as pd
import nltk


df = pd.read_csv('FLAT.csv', encoding_errors = 'ignore')
df['detail'] = df['comment']
df.head()

df['detail'] = df['detail'].str.lower()
df.tail()

clean_word = ['a', 'about', 'above', 'after', 'again', 'ain', 'all', 'am', 'an',
             'and','any','are', 'as', 'at', 'be', 'because', 'been', 'before',
             'being', 'below', 'between','both', 'by', 'can', 'd', 'did', 'do',
             'does', 'doing', 'down', 'during', 'each','few', 'for', 'from',
             'further', 'had', 'has', 'have', 'having', 'he', 'her', 'here',
             'hers', 'herself', 'him', 'himself', 'his', 'how', 'i', 'if', 'in',
             'into','is', 'it', 'its', 'itself', 'just', 'll', 'm', 'ma',
             'me', 'more', 'most','my', 'myself', 'now', 'o', 'of', 'on', 'once',
             'only', 'or', 'other', 'our', 'ours','ourselves', 'out', 'own', 're','s', 'same', 'she', "shes", 'should', "shouldve",'so', 'some', 'such',
             't', 'than', 'that', "thatll", 'the', 'their', 'theirs', 'them',
             'themselves', 'then', 'there', 'these', 'they', 'this', 'those',
             'through', 'to', 'too','under', 'until', 'up', 've', 'very', 'was',
             'we', 'were', 'what', 'when', 'where','which','while', 'who', 'whom',
             'why', 'will', 'with', 'won', 'y', 'you', "youd","youll", "youre",
             "youve", 'your', 'yours', 'yourself', 'yourselves']
cleaner = set(clean_word)
def cleaning(text):
    return " ".join([word for word in str(text).split() if word not in cleaner])

df['detail'] = df['detail'].apply(lambda text: cleaning(text))
df.head()

import string
english_punctuations = string.punctuation
punctuations_list = english_punctuations
def cleaning_punctuations(text):
    translator = str.maketrans('', '', punctuations_list)
    return text.translate(translator)
df['detail']= df['detail'].apply(lambda x: cleaning_punctuations(x))
df.tail()

def cleaning_repeating_char(text):
    return re.sub(r'(.)1+', r'1', text)
df['detail'] = df['detail'].apply(lambda x: cleaning_repeating_char(x))
df.tail()

def cleaning_URLs(data):
    return re.sub('((www.[^s]+)|(https?://[^s]+))',' ',data)
df['detail'] = df['detail'].apply(lambda x: cleaning_URLs(x))
df.tail()

def cleaning_numbers(data):
    return re.sub('[0-9]+', '', data)
df['detail'] = df['detail'].apply(lambda x: cleaning_numbers(x))
df.tail()

from nltk.tokenize import word_tokenize
df['detail'] = df['detail'].apply(lambda x: word_tokenize(x))
df.head()

st = nltk.PorterStemmer()
def stemming_on_text(data):
    text = [st.stem(word) for word in data]
    return data
df['detail'] = df['detail'].apply(lambda x: stemming_on_text(x))
df.head()

lm = nltk.WordNetLemmatizer()
def lemmatizer_on_text(data):
    text = [lm.lemmatize(word) for word in data]
    return data
df['detail'] = df['detail'].apply(lambda x: lemmatizer_on_text(x))
df.head()

print(df.to_string())