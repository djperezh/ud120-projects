#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
### your code goes here ###
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
#########################################################
clf = SVC(kernel = "rbf", C = 10000.)

# fcount  = int(len(features_train)/100)
# lcout = int(len(labels_train)/100)
# print(str(fcount))
# print(str(lcout))
# features_train = features_train[:fcount]
# labels_train = labels_train[:lcout]

t0 = time()
clf.fit(features_train, labels_train)
print("training time:", round(time()-t0, 3), "s")

t0 = time()
pr = clf.predict(features_test)
print("prediction time:", round(time()-t0, 3), "s")

print("pr[10]: " + str(pr[10]))
print("pr[26]: " + str(pr[26]))
print("pr[50]: " + str(pr[50]))

result = len(list(filter(lambda x: x == 1, pr)))
print("Mails from Cris: " + str(result) + "/" + str(len(pr)))

accuracy = accuracy_score(labels_test, pr)
print("accuracy: " + str(accuracy))