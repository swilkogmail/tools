#!/usr/bin/python3
# What is the expected output of the following code ?

y = 'R2D2'
def my_func(x):
    global y
    y = x
    return y
 
x = 'Yoda'
my_func('C3PO')
print(y)

# Explanation:

# When you create a variable inside a function, that variable has a local scope, and can only be used inside that function.

# With the  global keyword, the scope of that variable will be extended to outside the function too.

# The call to my_func('C3PO')  will assign 'C3PO' to the global variable y and print(y) will return C3PO.