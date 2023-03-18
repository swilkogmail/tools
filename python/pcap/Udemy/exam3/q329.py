#!/usr/bin/python3
# What is the expected output of the following code snippet ?
class Z:
    def __init__(self, z):
        self.z = z
 
z = Z('z')
print(hasattr(z,'Z'))
print(isinstance(z,Z))


# hasattr()  is a function that returns True if a specified object or class 
# has a particular property, and returns False otherwise (syntax is hasattr(object or class, property)).
# isinstance()  is a function that returns True if an object comes 
# from an indicated class, and returns False otherwise (syntax is isinstance(Object, Class) ).
# In the above question hasattr(z,'Z')  returns False since object z has no property Z (z does have a property z though (note the lower case)).
# isinstance(z,Z)  returns True since object z comes from the class Z.
# So the following answer is correct :
False
True

# Try it yourself:

class Z:
    def __init__(self, z):
        self.z = z
 
z = Z('z')
print(hasattr(z,'Z'))    # False
print(isinstance(z,Z))   # True