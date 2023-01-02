import numpy as np
import pandas as pd
import itertools, pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix


pac = pickle.load(open("model.pickle", "rb"))
tfidf_vectorizer = pickle.load(open("vecto.pickle", "rb"))



def predict(message) : 
    vectMessage = tfidf_vectorizer.transform(pd.Series([message]))
    prediction = pac.predict(vectMessage)
    return prediction[0]

