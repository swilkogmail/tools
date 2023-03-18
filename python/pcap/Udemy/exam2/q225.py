#!/usr/bin/python3

# What is the expected output of the following code?

class A:
    X = 2 # - class variables are not included
    def __init__(self, a, b): # 'x': 5
        self.x = a + b
        self.__y = a - b # '_A__y': 1 - private instance variables are included - if they have been defined within the class, name mangling is used to refer to them
 
a = A(3,2)
a.__z = 0 # - '__z': 0 instance variables defined outside of the class are included - if they are private, name mangling is not needed to refer to them
print(a.__dict__)

# Explanation:

# __dict__  is a "built-in" property of an object : it is a dictionary that 
# includes the name of the object's variables (as key) and their corresponding values.

# A few things to remember about __dict__ for an object :

# Based on the above, the only possible answer is :

# {'x': 5, '_A__y': 1, '__z': 0}
