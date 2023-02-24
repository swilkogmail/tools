#!/usr/bin/python3
# What is the expected output of the following code snippet ?

class Omega:
    A= True
    def __init__(self, x, y):
        self.a = x
        self.__b = y
    def set(self, z):
        self.c = z
 
omega= Omega(5, 3)
omega.__d = True
print(omega.__dict__)


# __dict__ is a predefined property of all Python objects : this variable is a dictionary and 
# contains the names and values of all the variables the object is currently carrying.

# A few things to remember about __dict__ for an object :

# - class variable will not appear in the __dict__ variable of an object.

# - private instance variable defined inside the class will appear in the dictionary using 
# "name mangling", i.e. : _className__variable where className is the name of the class where that private instance variable is defined.

# - private instance variable defined outside the class will appear in the dictionary as __variable

# Based on the above rules, the only correct answer is :

# {'a': 5, '_Omega__b': 3, '__d': True}
# (b is a private instance variable defined inside the class; d is a private instance variable defined 
# outside the class; variable Adoes not show up since it is a class variable).