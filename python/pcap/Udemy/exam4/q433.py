#!/usr/bin/python3
# What is the output of the following snippet ?

from math import factorial
 
def myfunc(x):
    for i in range(x):
        yield factorial(i+1)
 
y = [x for x in myfunc(4)]
 
print(y)

# Explanation:

# The yield statement can be used only inside functions. The yield statement suspends the  
# function execution and causes the function to return the yield's argument as a result. 
# Such a function cannot be invoked in a regular way – its only purpose is to be used as a generator.

# A generator can be used to produce a list within a list comprehension.

# In the above question, function myfunc generates a sequence of factorials.

# Statement y = [x for x in myfunc(4)]   is a list comprehension which is a way to create a list from an expression.

# Using the myfunc(4) as the generator, [x for x in myfunc(4)]  will return each yield's 
# argument from myfunc(4) as a list element . The resulting list is : [1, 2, 6, 24] .