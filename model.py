import numpy as np
import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv("news.csv")
labels = df["label"]

x_train = df["text"]
y_train = labels

tfidf_vectorizer=TfidfVectorizer(stop_words='english')
tfidf_train=tfidf_vectorizer.fit_transform(x_train) 

pac=PassiveAggressiveClassifier(max_iter=50)
pac.fit(tfidf_train,y_train)

print("""
--------------------------------------------
the model is ready                         |
___________________________________________|
""")

def predict(message) : 
    vectMessage = tfidf_vectorizer.transform(pd.Series([message]))
    prediction = pac.predict(vectMessage)
    return prediction[0]
