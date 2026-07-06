'''RAG: TD-IDF playground to understand the theory'''

#import math
from collections import Counter
import numpy as np
import pandas as pd


#from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer,TfidfTransformer

documents = ['problem of evil',
           'evil queen',
           'horizon problem']

# 1. Preprocessing and Tokenization
# Lowercase all text and split into individual words
tokenized_docs = [doc.lower().split() for doc in documents]
N = len(tokenized_docs)

# 2. Calculate Term Frequency (TF)
tf_dicts = []
for doc in tokenized_docs:
    word_counts = Counter(doc)
    total_words = len(doc)
    tf_dicts.append({word: count / total_words for word, count in word_counts.items()})

# 3. Calculate Inverse Document Frequency (IDF)
# 1 + log(Total Docs / Number of docs with term)
all_words = set(word for doc in tokenized_docs for word in doc)
idf_dict = {}
for word in all_words:
    # Count how many documents contain the specific word
    doc_count = sum(1 for doc in tokenized_docs if word in doc)
    idf_dict[word] = np.log(N / doc_count) +1

# 4. Calculate TF-IDF
tfidf_dicts = []
for tf_dict in tf_dicts:
    tfidf_doc = {}
    for word, tf_score in tf_dict.items():
        tfidf_doc[word] = tf_score * idf_dict[word]
    tfidf_dicts.append(tfidf_doc)

# 5. Convert to Pandas DataFrame
tfidf_df = pd.DataFrame(tfidf_dicts).fillna(0)
print(tfidf_df)

# 1. Get raw TF counts
# vec = TfidfVectorizer()
# tf_idf = vec.fit_transform(text_db)
# print(pd.DataFrame(tf_idf.toarray(),columns=vec.get_feature_names_out()))

# vec1=CountVectorizer()
# counts=vec1.fit_transform(text_db)
# print(pd.DataFrame(counts.toarray(),columns=vec1.get_feature_names_out()))

# transformer=TfidfTransformer(smooth_idf=False)
# tfidf1=transformer.fit_transform(counts.toarray())
# print(tfidf1.toarray())
# tf = counts / counts.sum(axis=1, keepdims=True)
# df = (counts > 0).sum(axis=0)
# idf = np.log(len(corpus) / df)
# tfidf = tf * idf
# print(tfidf)
# transformer=TfidfTransformer(smooth_idf=False)
# tfidf1=transformer.fit_transform(counts)
# print(tfidf1.toarray())

# 2. Get combined TF-IDF with normalization off
# tfidf_vec = TfidfVectorizer(norm='l1')
# tfidf_matrix = tfidf_vec.fit_transform(corpus)
# print("\nRaw TF-IDF Matrix:\n", tfidf_matrix.toarray())

# 3. View the IDF values themselves
# print("\nIDF Weights:\n", tfidf_vec.idf_)
