import nltk
import pandas as pd
from nltk.stem.porter import *
from nltk.stem import WordNetLemmatizer
from collections import Counter

tokens = []
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()


def get_tokens(text):
    token = nltk.word_tokenize(text)
    return token


def stems(text):
    return stemmer.stem(text)


def lemmas(text):
    return lemmatizer.lemmatize(text)


data = pd.read_csv('merged_file.csv')

for i in range(200):
    tokens.extend(get_tokens(lemmas(stems(data['Purpose'][i]))))

tokens_freq = Counter(tokens)
print(tokens_freq.most_common(10))
