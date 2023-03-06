#!/usr/bin/python3
# What is the expected output of the following snippet ?

from math import ceil
 
def func(g,x):
    return g(x) + 1
    
print(func(lambda x: ceil(x),3.2))

# Explanation:

# Here a lambda function is being used as a parameter of function func(). This lambda 
# function returns ceil(x) where ceil() is a function from the math module that returns the smallest integer greater than or equal to variable x .

# So, func(lambda x: ceil(x),3.2) will return ceil(3.2) + 1 i.e : 4 + 1 --> 5