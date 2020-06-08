#!/usr/bin/python

"""
    Starter code for the regression mini-project.
    
    Loads up/formats a modified version of the dataset
    (why modified?  we've removed some trouble points
    that you'll find yourself in the outliers mini-project).
    Draws a little scatterplot of the training/testing data
    You fill in the regression code where indicated:
"""    


import sys
import pickle

"""
NOTE: for Picke files in Python > 3.5
pikle files must be unix format () otherwise you will get the following error:
"the STRING opcode argument must be quoted"

In order to convert the file, you can create a script like the one described in this link:
https://stackoverflow.com/questions/45368255/error-in-loading-pickle

Or you can just run one of the commands described in this link in your terminal:
https://stackoverflow.com/questions/2613800/how-to-convert-dos-windows-newline-crlf-to-unix-newline-lf-in-a-bash-script/19702943#19702943

in my case I run it directly on my Bash:
$ awk '{ sub("\r$", ""); print }' email_authors.pkl > email_authors_unix.pkl
"""

sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from dos2unix import dos2unix

dictionary = pickle.load( open("../final_project/final_project_dataset_modified_unix.pkl", "rb") )

### list the features you want to look at--first item in the 
### list will be the "target" feature
features_list = ["bonus", "salary"]
# features_list = ["bonus", "long_term_incentive"]

dos2unix("python2_lesson06_keys.pkl", "python2_lesson06_keys_unix.pkl")
data = featureFormat( dictionary, features_list, remove_any_zeroes=True, sort_keys = '../tools/python2_lesson06_keys_unix.pkl')
target, features = targetFeatureSplit( data )

### training-testing split needed in regression, just like classification
from sklearn.model_selection import train_test_split
feature_train, feature_test, target_train, target_test = train_test_split(features, target, test_size=0.5, random_state=42)
train_color = "b"
test_color = "r"



### Your regression goes here!
### Please name it reg, so that the plotting code below picks it up and 
### plots it correctly. Don't forget to change the test_color above from "b" to
### "r" to differentiate training points from test points.
from sklearn.linear_model import LinearRegression
reg = LinearRegression().fit(feature_train, target_train)
pr = reg.predict(feature_train)

print("Score: " + str(reg.score(feature_train, target_train)))
# print(reg.score(feature_test, target_test))
print("Slope (coef_): ")
print(reg.coef_)
print("Intercept: " + str(reg.intercept_))
print("Predictions: ")
print(pr)

### draw the scatterplot, with color-coded training and testing points
import matplotlib.pyplot as plt
for feature, target in zip(feature_test, target_test):
    plt.scatter( feature, target, color=test_color ) 
for feature, target in zip(feature_train, target_train):
    plt.scatter( feature, target, color=train_color ) 

### labels for the legend
plt.scatter(feature_test[0], target_test[0], color=test_color, label="test")
plt.scatter(feature_test[0], target_test[0], color=train_color, label="train")




### draw the regression line, once it's coded
try:
    plt.plot( feature_test, reg.predict(feature_test) )
except NameError:
    pass


# sneak peak for next lesson: remove outliers improve the Score (slope is lower)
reg.fit(feature_test, target_test)
print("Slope (coef_): ")
print(reg.coef_)
print("Intercept: " + str(reg.intercept_))


plt.plot(feature_train, reg.predict(feature_train), color="b") 

plt.xlabel(features_list[1])
plt.ylabel(features_list[0])
plt.legend()
plt.show()