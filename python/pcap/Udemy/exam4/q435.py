#!/usr/bin/python3
# What is the expected output of the following code snippet ?

def f(x):
    def g(y): # Here we have function g() nested inside function f(). Function f() returns function g().
        return 2*x + y
    return g
 
k = f(3) # So, f(3) returns function g() that itself will return 2*3 + y  (replace x with 3 in the function definition).
         # so k is now a function or type g that is defined as the lines above
print(k(4)) # And finally k(4) will return 2*3 + 4 , i.e. 10. 

# Explanation:

# The above function is a closure.

# We have a closure in Python when  :

# - there is a nested function (function inside a function).

# - the nested function refers to a value defined in the enclosing function.

# - the enclosing function returns the nested function.