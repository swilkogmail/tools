#!/usr/bin/python3
# What is the expected output of the following code snippet ?

class Vegetable:
    pass
 
class RootVegetable(Vegetable):
    pass
 
class Potato(RootVegetable):
    pass
 
print(Potato.__bases__) # __bases__ only contains the direct superclass of the class, not all classes

# Explanation
# Knowledge Area : Object-Oriented Programming

# Topic : __bases__ property of a class

# Explanation:

# __bases__  is a predefined property of a class. It is a tuple and 
# contains the classes (not the class names) which are direct superclasses of the class.

# Direct superclass of the Potato class is : RootVegetable.

# So, correct answer is :

# (<class '__main__.RootVegetable'>,)