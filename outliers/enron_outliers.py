#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset_unix.pkl", "rb") )
data_dict.pop( "TOTAL", 0 )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

# data_dict.sort()
tmp = []
for (key, value) in data_dict.items():
    # if (value['salary'] != "NaN" and value['bonus'] != "NaN" and value['exercised_stock_options'] != "NaN"):
        # tmp.append((key, (value['salary']/1000000, value['bonus']/1000000)))
        # print(key)

    # sneak peek for next lesson
    # if (value['exercised_stock_options'] != "NaN"):
    #     tmp.append(value['exercised_stock_options'])

    if (value['salary'] != "NaN"):
        tmp.append(value['salary'])

tmp.sort()
print(tmp)