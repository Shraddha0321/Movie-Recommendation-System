# -*- coding: utf-8 -*-
"""Movie_Recommender.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xw98V7xZOX8yvkwfQ2l6-Kbp1BM0-Um3
"""

import pandas as pd

df = pd.read_csv("/content/sample_data/spotify_millsongdata.csv")

df.head(5)

df.tail(5)

df.shape

df.isnull().sum()

df.drop('link', axis=1).reset_index(drop=True)

df.head(10)

df['text'][0]

#df = df.sample(5000)

df.shape

#Text Cleaning bb/Text Preprocessing
df['text'] = df['text'].str.lower().replace(r'^\w\s', '').replace(r'\n', '',regex = True)#

df

import nltk
nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

def tokenization(txt):
    tokens = nltk.word_tokenize(txt)
    stemming = [stemmer.stem(w) for w in tokens]
    return " ".join(stemming)

df['text'] = df['text'].apply(lambda x: tokenization(x))

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

tfidvector = TfidfVectorizer(analyzer='word',stop_words='english')
matrix = tfidvector.fit_transform(df['text'])
similarity = cosine_similarity(matrix)

similarity[0]

token("you are beautiful, beauty")

df['text'].apply(lambda x: token(x))

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

tfidvector = TfidfVectorizer(analyzer='word',stop_words='english')
matrix = tfidvector.fit_transform(df['text'])
similarity = cosine_similarity(matrix)

similarity[0]

df[df['song'] == 'Crying Over You']

def recommendation(song_df):
    idx = df[df['song'] == song_df].index[0]
    distances = sorted(list(enumerate(similarity[idx])),reverse=True,key=lambda x:x[1])

    songs = []
    for m_id in distances[1:21]:
        songs.append(df.iloc[m_id[0]].song)

    return songs

recommendation('Crying Over You')



