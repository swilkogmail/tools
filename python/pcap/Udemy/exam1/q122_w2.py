#!/usr/bin/python3
# What is the expected output of the following code snippet ?

from math import sqrt as root
 
def my_root(x):
    try:
        return root(x)
    except:
        print('Function Error !')
        raise
 
x=-2
try:
    assert x + 2, "Wrong input !" # will raise an AssertionError  if x+2  returns 0 along with the message "Wrong input !".
    print(my_root(x))
except Exception as e:
    print(e)
else:
    print('All good !')

x=-4
try:
    assert x + 2, "Wrong input !" 
    print(my_root(x))
except Exception as e:  # will raise 'Function Error !' from the function and then print the raised error.
    print(e)
else:
    print('All good !')

x=4
try:
    assert x + 2, "Wrong input !"  # all good
    print(my_root(x))
except Exception as e:
    print(e)
else:
    print('All good !')