#!/usr/bin/python3
# What is the expected output of the following snippet ?

x = 3
y = 2
z = 3
 
def my_func(x,y,z=1):
    return(x**y**z)
 
print(my_func(x=2,y,z))

# Explanation:

# Function my_func() takes three parameters (x,y,z). Those three parameters are 
# unrelated to the variables x, y and z defined outside of the function.

# The call to the function my_func()  in the last line of the code (my_func(x=2,y,z)) 
# is done using both keyword argument passing (x=2) and positional argument passing (y,z)  - 
# mixing those two methods of argument passing is acceptable provided that positional arguments does NOT follow keyword arguments.

# So, my_func(x=2,y,z)  would raise a runtime exception since the positional arguments follow the keyword argument (x=2).

# There are valid ways to call the function -  see below for examples.

# Try it yourself:

x = 3
y = 2
z = 3
 
def my_func(x,y,z=1):
    return(x**y**z)
 
print(my_func(x=2,y,z))        # SyntaxError: positional argument follows keyword argument
 
print(my_func(2,y,z))          # 256
 
print(my_func(2,y=y,z=z))      # 256 
 
print(my_func(2,y=y))          # 4