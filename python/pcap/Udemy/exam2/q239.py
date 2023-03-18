#!/usr/bin/python3
# What is the expected output of the following snippet ?

def func(x,y):
    return x/y
 
try:
    func(3,0)
except: # this could be used although needs to be the last entry in the expept block
    print("Error 1")
except ZeroDivisionError:
    print("Error 2")
except BaseException:
    print("Error 3")

# Explanation:

# In a try-except branches, if there are multiple except branches, including one 
# unnamed except branch (one without an exception name), this unnamed 
# branch must be the last branch. Not following this rule will cause a syntax error.

# Other syntax rules to remember :

# - you cannot have 2 except branches with the same exception name.

# - you cannot use an except branch without a try branch preceding it.