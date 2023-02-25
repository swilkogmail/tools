#!/usr/bin/python3
# Explanation:

# Let's review each statement :

# --> Different objects of the same class always have the same sets of properties.

# This is false :  an object of one class can have different properties from another object of the same class (see below for an example).

# -->  The __dict__ variable exists for an object but not for a class.

# This is incorrect : the __dict__ variable is a property of both an object and a class.

# --> Function hasattr() can be used with either a class or an object.

# That is correct : Function hasattr() can be used to check if an object or a class has a specified property.

# --> A class variable needs at least one object (of this same class) created to be accessible.

# This is false : a class variable does not need any object of that class to be created to exist.

class Alpha:
    A=1       # this is a class variable
    def __init__(self,val):
        self.a= val
 
# a class variable does not need any object of that class to be created to exist:
print(Alpha.A)   # 1
 
myobject_1 = Alpha(2)
myobject_1.b = 0
 
myobject_2 = Alpha(1)
 
# the __dict__ variable is a property of both an object and a class:
print(myobject_1.__dict__)  # {'a': 2, 'b': 0}
print(Alpha.__dict__) # {'__module__': '__main__', 'A': 1, ..., '__doc__': None}
 
# Different objects of the same class can have different sets of properties:
print(myobject_1.__dict__)  # {'a': 2, 'b': 0}
print(myobject_2.__dict__)  # {'a': 1}
 
# Function hasattr() can be used with either a class or an object:
print(hasattr(myobject_2, 'b')) # False
print(hasattr(Alpha, 'A'))      # True