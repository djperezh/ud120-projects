#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
"""

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

enron_data = pickle.load(open("../final_project/final_project_dataset_unix.pkl", "rb"))
print("Total people: " + str(len(enron_data)))

# Filter dictionary by keeping elements whose keys are divisible by 2
# data[person_name]["poi"]==1
#poi = dict(filter(lambda data: data[0]["poi"] == True, enron_data.items()))

poi = {key: value for (key, value) in enron_data.items() if value["poi"] == True }
print(len(poi.keys()))


# poi_names = list(filter(lambda data: data["poi"] == True, enron_data.keys()))
# print(poi_names)

print(enron_data["PRENTICE JAMES"]["total_stock_value"])

print(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])

print(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])

print(enron_data["SKILLING JEFFREY K"]["total_payments"])
print(enron_data["FASTOW ANDREW S"]["total_payments"])
print(enron_data["LAY KENNETH L"]["total_payments"])


quatified_salary = {key: value for (key, value) in enron_data.items() if value["salary"] != "NaN" }
print(len(quatified_salary.keys()))

known_email = {key: value for (key, value) in enron_data.items() if value["email_address"] != "NaN" }
print(len(known_email.keys()))

unknown_total_payments = {key: value for (key, value) in enron_data.items() if value["total_payments"] == "NaN" }
print(len(unknown_total_payments.keys()))
print(str(100 * len(unknown_total_payments.keys())/len(enron_data)))

poi_unknown_total_payments = {key: value for (key, value) in poi.items() if value["total_payments"] == "NaN" }
print(len(poi_unknown_total_payments.keys()))
print(str(100 * len(poi_unknown_total_payments.keys())/len(poi)))