#!/usr/bin/python3
# What is the expected output of the following snippet ?

from math import factorial
 
try:
    print(factorial(-4))
except:
    print("Error #1")
except ValueError:
    print("Error #2")

# Explanation:

# The factorial() function is part of the math module and allows to compute the 
# factorial of a number. This number must be a positive integer; if not a ValueError exception is raised.

# In the above code, the unnamed except branch is placed before a named 
# xcept branch : this is not a correct syntax and the code will generate a 
# syntax error. When using multiple except branches, if using an unnamed except branch, it must be placed last.