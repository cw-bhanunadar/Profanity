from profanity_check import predict
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import seaborn as sns
import numpy as np

test = pd.read_csv('./data/test_data.csv')
names = test['Name']
actual = test['Is_spam']

predicted = predict(names)
cf_matrix = confusion_matrix(actual, predicted, labels=[1,0])


group_names = ['True Neg','False Pos','False Neg','True Pos']
group_counts = ["{0:0.0f}".format(value) for value in
                cf_matrix.flatten()]
group_percentages = ["{0:.2%}".format(value) for value in
                     cf_matrix.flatten()/np.sum(cf_matrix)]
labels = [f"{v1}\n{v2}\n{v3}" for v1, v2, v3 in
          zip(group_names,group_counts,group_percentages)]
labels = np.asarray(labels).reshape(2,2)
sns.heatmap(cf_matrix, annot=labels, fmt='', cmap='Blues')

matrix = classification_report(actual,predicted,labels=[1,0])
print('Classification report : \n',matrix)

"""
                  precision  recall   f1-score  support

           1       0.77      1.00      0.87     20061
           0       1.00      0.69      0.82     19964

    accuracy                           0.85     40025
   macro avg       0.88      0.85      0.84     40025
weighted avg       0.88      0.85      0.84     40025

"""