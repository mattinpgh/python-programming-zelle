# Redo programming exercise 2 from chapter 3, but use functions
# to compute the area of a pizza and the cost per square inch
from math import pi

def pizza_area(radius):
    return pi * (radius ** 2)

def cost_per_square_inch(cost, radius):
    return cost / pizza_area(radius)

print(cost_per_square_inch(20, 10))
