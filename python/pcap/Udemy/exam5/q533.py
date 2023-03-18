#!/usr/bin/python3
# Consider the function below :

def myfunc(x,y=0):
    return x+y

# Explanation:

# The function is defined with two parameters : x and y.

# Only y is given a default value (y=0). That means that the function myfunc may be called without 
# specifying a value for parameter y ( in this case the function will use its default value (y=0)).

# x is not given a default value. So any call to function myfunc must specify a value for x.

# In conclusion :

# -> The function may be invoked with exactly one argument (x)

# -> The function may be invoked with exactly two arguments (x and y).