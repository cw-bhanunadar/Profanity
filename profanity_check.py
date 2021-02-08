import numpy as np
import joblib

vectorizer = joblib.load('data/vectorizer.joblib')
model = joblib.load('data/model.joblib')

def _get_profane_prob(prob):
  return prob[1]

def predict(texts):
  return model.predict(vectorizer.transform(texts))

def predict_prob(texts):
  return np.apply_along_axis(_get_profane_prob, 1, model.predict_proba(vectorizer.transform(texts)))
