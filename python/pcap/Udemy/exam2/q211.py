#!/usr/bin/python3
# What is the expected output of the following code snippet ?

class Mammal:
    def __init__(self,val):
        self.__name = val
 
class Feline(Mammal):
    pass
 
class Cat(Feline):
    __bases=[2,3]
    def __str__(self):
        return self.name
 
mycat = Cat('Garfield')

print(Cat.__bases__)
print(Cat.__bases__[0].__name__) # # __name__ is another "built-in" attribute of a class and returns the name of the corresponding class.
print(len(Cat.__bases__))


# Explanation:

# __bases__ is an attribute of a class and is a tuple that contains the direct superclasses of a 
# class - note that these are not the class names but the actual classes.

# The order of the classes in the tuple is the same as the order used in the class definition.

# __name__ is another "built-in" attribute of a class and returns the name of the corresponding class.

# So, in the above code, Cat.__bases__  is a tuple that contains Cat's superclass which is class Feline.

# This tuple has only one element (because Cat has only one direct superclass - Mammal is not a direct superclass of Cat).

# So, len(Cat.__bases__) returns 1.

# And Cat.__bases__[0].__name__  returns the name of the first class in the __bases__ tuple which is Feline.