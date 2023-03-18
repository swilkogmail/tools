#!/usr/bin/python3
# What is the expected output of the following code?

import math
 
def my_func(x,y):
    z = math.trunc(x) + math.ceil(x) - math.floor(y)
    return z
 
print(my_func(-1.6,-3.2))

# ceil(x) : returns the smallest integer greater than or equal to x.
# floor(x) : returns the largest integer less than or equal to x.
# trunc(x) : returns the value of x truncated to an integer.

# math.trunc(-1.6) returns -1
# math.ceil(-1.6) returns -1
# math.floor(-3.2) returns -4
# and my_func(-1.6,-3.2) returns 2 (-1 -1 -(-4) = 2)

print(math.trunc(1.9))
print(math.trunc(1.2))
print(math.ceil(-1.6))