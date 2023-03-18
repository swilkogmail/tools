#!/usr/bin/python3
# What is the expected output from the following code snippet ?

def sub(a, b=1):
    if a>b:
        return a-b
    else:
        return b-a
 
print(sub(a=3,4)) 

# Explanation:

# You can pass arguments to a function using the following techniques:

# - positional argument passing in which the order of arguments passed matters,

# - keyword (named) argument passing in which the order of arguments passed doesn't matter,

# - a mix of positional and keyword argument passing.

# When mixing positional and keyword arguments, it's important to remember that cardinal rule :

# Positional arguments mustn't follow keyword arguments.

# In the code above, sub(a=3,4) is a call to the sub() function using a mix of positional (4) and keyword argument (a=3).

# BUT the positional argument follows the keyword argument - so this will generates a Syntax Error.

# So, the code is erroneous.


def sub(a, b=1):
    if a>b:
        return a-b
    else:
        return b-a
 
print(sub(3,4))       # 1   (using positional arguments)
print(sub(b=4,a=3))   # 1   (using keyword arguments)
print(sub(a=3,b=4))   # 1   (using keyword arguments)
print(sub(3,b=4))     # 1   (using a mix)
#print(sub(a=3,4))     # SyntaxError