import os
import sys

import nltk
import pickle
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from numpy import ndarray


from src.exception import CustomException
from sklearn.base import BaseEstimator, TransformerMixin
from src.logger import logging

class Stem(BaseEstimator, TransformerMixin):
    def fit(self, X):
        return self
    
    def transform(self, X):
        corpus = []
        ps = PorterStemmer()
        for i in range(0, len(X)):
            review = re.sub('[^a-zA-z]', ' ', X[i])
            review = review.lower()
            review = review.split()
            review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
            review = ' '.join(review)
            corpus.append(review)
        return corpus

class ToArray(BaseEstimator, TransformerMixin):
    def fit(self, X):
        return self
    
    def transform(self, X):
        return X.toarray()


def save_object(file_path, obj):
    try:
        file_dir = os.path.dirname(file_path)
        os.makedirs(file_dir, exist_ok=True)
        logging.info('Created folder')
        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)


def load_object(file_path):
    try:
        with open(file_path, 'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        raise CustomException(e, sys)