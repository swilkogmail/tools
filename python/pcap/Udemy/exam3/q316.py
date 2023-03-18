#!/usr/bin/python3
# What is the expected output of the following code?

def my_func(x,y):
    return x / y
 
try:
    my_func(5,0)
except:
    print("General issue")
except ValueError:
    print("ValueError")
except ArithmeticError:
    print("ArithmeticError")

# Explanation:
# When using multiple except branches, if using an unnamed except: branch, that branch must be placed last - if not, a syntax error will be generated.