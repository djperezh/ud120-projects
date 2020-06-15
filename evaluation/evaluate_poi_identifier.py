#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset_unix.pkl", "rb") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

print(len(labels))

### your code goes here 
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)

clf = tree.DecisionTreeClassifier(min_samples_split=40)
clf.fit(features_train, labels_train)
pr = clf.predict(features_test)
accuracy = accuracy_score(labels_test, pr)
print("accuracy: " + str(accuracy))
print("# of features:" + str(len(features_train[0])))

### Scikit-Learn library contains functions that can help calculate these values for us.
### To do so, use this code from the metrics package
from sklearn.metrics import classification_report, confusion_matrix, precision_score, recall_score
print(confusion_matrix(labels_test, pr))
print(classification_report(labels_test, pr))
print(precision_score(labels_test, pr))
print(recall_score(labels_test, pr))

from sklearn import metrics
import numpy as np
print('Mean Absolute Error:', metrics.mean_absolute_error(labels_test, pr))
print('Mean Squared Error:', metrics.mean_squared_error(labels_test, pr))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(labels_test, pr)))