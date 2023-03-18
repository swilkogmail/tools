#!/usr/bin/python3
# Consider the code snippet below :

class A:
    a=1
    def __init__(self, x=0):
        self.b = x
 
class B(A):
    c = 0
    def __str__(self):
        return "B"
 
class C(B):
    d = 0
 
beta = B(3)
beta.d = 2

# Which statement regarding the above code snippet returns True ?

# Explanation:
# Let's review each suggested answers:

# --> issubclass(A, B)
# Function  issubclass(Class_1, Class_2) returns True if  Class_1 is a subclass of Class_2, and False otherwise.
# Here, A is not a subclass of B, so the above statement returns False.

# --> hasattr(B, 'a')
# Function  hasattr(obj, prop) returns True if object obj has a property prop, and False otherwise. 
# This function also works with classes. Here, class B has indeed a class variable a inherited from class A. So the above statement returns True.

# --> isinstance(beta, C)
# Function  isinstance(obj, Class) returns True if object obj comes from class Class, and False otherwise. 
# Here, object beta does not come from class C .So the above statement returns False.

#  --> 'c' in beta.__dict__.keys()
# __dict__ is a built-in property of an object - it is a dictionary and includes all instance 
# variables of that object (and their values). Class variables are not included. So 'c' being a class variable, 
# it is not included in beta.__dict__ and the above statement returns False.