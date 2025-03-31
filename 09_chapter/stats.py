"""
Simple descriptive statistics
"""

from math import sqrt

def mean(lst):
    return float(sum(lst) / len(lst))

def st_dev(lst):
    x_bar = mean(lst)
    numerator = sum((x - x_bar)**2 for x in lst)
    return sqrt((numerator / len(lst)))

def mean_st_dev(lst):
    return mean(lst), st_dev(lst)

print(mean_st_dev([8,6,7,5,3,0,9]))