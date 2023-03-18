#!/usr/bin/python3
# Consider the code below :
class Lambda():
    L=2
    def __init__(self, x = 0):
        self.l = x + 1
        self.__m = x
    def set(self, y = 2):
        self.k = y + 1
    
class Omega(Lambda):
    M=2
    def __str__(self):
        return str(super().L)
 
m = Omega()
m.__n=3
print(m.__dict__)

# Which statement related to the above code is correct ?

# Explanation:
# Let's review each suggested answer:
# --> (1) hasattr(m,'k') returns True
# hasattr(object,'prop')  will return True if object has property 'prop' and will return False otherwise.
# Statement (1) is False since for object m to get property 'k' set, the method set() needs to be called - it was not called in the above code.

# --> (2) print(m)  prints  1  on the screen
# method __str__() defined in class Omega allows to customize the string that is printed when an object of the Omega class 
# is printed (via print() ). As per the definition of __str__() in Omega, str(super().L)  
# is returned. super() is a reference to the direct superclass of the current class, i.e. Lambda and Lambda.
# L  has a value of 2 ( L is a class variable). The str() function converts the integer 2 to the string '2'. So print(m)  will print 2 , not 1.

# --> (3) m.__dict__  is a dictionary with 2 elements
# __dict__ is a dictionary and it is a property available for all objects : it contains the instance 
# variables of that object along with their values (the class variables are not included).
# So, how many property does object m has ?
# It has property 'l', and private property 'm', both defined within 
# the Lambda class; and private property 'n' defined outside of a class. So, that's 3 properties, not 2.

# --> (4) isinstance(m, Lambda)  returns True
# isinstance(obj, Class) is a function that will return True if obj is an instance of class Class, and False otherwise.
# Object m is indeed an instance of class Lambda via inheritance from class Omega. So, this was the correct answer.