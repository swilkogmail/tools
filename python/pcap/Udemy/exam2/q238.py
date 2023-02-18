#!/usr/bin/python3
# What is the expected output of the following snippet ?

try:
    raise Exception
except Exception as e:
    print(type(e.args))

# Explanation:

# The syntax except Exception_Name as an exception_object: intercepts an object carrying information about a pending exception. 
# The object's property named args is a tuple and stores all arguments passed to the object's constructor.