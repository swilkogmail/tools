#!/usr/bin/python3
# What is the expected output of the following code?

x = 'France'
 
def func(x):
    return x[:-3]
# The function func() takes a string a returns it MINUS the last three characters.
# When executing this function twice on string 'France', the resulting string will be an empty string.

try:
    for i in range(3):
        x = func(x)
        assert x
        # assert expression  will evaluate the expression and if the expression meets one of the following criteria, then an AssertionError will be raised :
            # - expression evaluates to False
            # - expression evaluates to 0
            # - expression evaluates to an empty string
            # - expression evaluates to None
        # So, in the try: branch above, an AssertionError will be raised since at one point x will become an empty string and assert x will raise the exception.
        # So : Error 3  will be printed.
    print(x)    
except IndexError:
    print("Error 1")
except LookupError:
    print("Error 2")
except:
    print("Error 3")



