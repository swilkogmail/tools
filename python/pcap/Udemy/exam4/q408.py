#!/usr/bin/python3
# What is the expected output of the following code?

def func(x,y):
    return x/(y-4)
 
try:
    print(func(x=1,4))
except ArithmeticError:
    print("ArithmeticError")
except ZeroDivisionError:
    print("ZeroDivisionError")
except:
    print("Misc. Error")

# Explanation:

# Although the topic of this question is Exceptions, it is a trap !

# One could think that func(x=1,4) would raise a ZeroDivisionError exception and since a ZeroDivisionError 
# exception is a sub-class of the ArithmeticError exception, then ArithmeticError  would be printed out.

# However, you need to pay attention to how the function func() is called ! It is called with a 
# keyword argument (x=1) before the positional argument (4) :  this will raise a Syntax Error !

# When using a mix of positional and keyword arguments in a function, positional arguments must be placed before the keyword arguments.