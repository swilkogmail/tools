#!/usr/bin/python3
# What is the expected output of the following code snippet ?

def f(x):
    def g(y):
        return x * y
    return g
 
k = f(4) # So, f(4) returns function g() that itself will return 4*y  (replace x with 4 in the function definition).
    # def g(4):
    #     return x * 4
    # return g # return the function
print(k(4))
# at this point k is of type function(g) so we in effect call it with 4, i.e.
    # def g(4):
    #     return 4 * 4

# Explanation:

# The above function is a closure.

# We have a closure in Python when  :

# - there is a nested function (function inside a function).

# - the nested function refers to a value defined in the enclosing function.

# - the enclosing function returns the nested function.

# Here we have function g() nested inside function f(). Function f() returns function g().

# So, f(4) returns function g() that itself will return 4*y  (replace x with 4 in the function definition).

# And finally k(4) will return 4*4 , i.e. 16. 