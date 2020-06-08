#!/usr/bin/python

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    tmp = []
    cleaning_percentage = len(predictions) * .10

    for index in range(len(predictions)):
        diff = predictions[index] - net_worths[index]
        square_error = diff**2
        tmp.append((square_error, index))
    
    tmp.sort()
    
    for index in range(len(tmp) - int(cleaning_percentage)):
        error, i = tmp[index]
        cleaned_data.append((ages[i], net_worths[i], error))

    # print(cleaned_data)

    return cleaned_data

