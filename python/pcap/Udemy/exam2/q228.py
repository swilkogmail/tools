#!/usr/bin/python3
# What is the expected output of the following code ?

class Gamma:
    def __init__(self, val):
        self.name = val
    def __str__(self):
        return "I am " + self.name + " from Gamma"
 
class Delta:
    def __init__(self, val):
        self.name = val
    def __str__(self):
        return "I am " + self.name + " from Delta"
 
class Beta(Gamma, Delta):
    def __str__(self):
        return super().__str__()
 
class Omega(Beta):
    omega = 3
    pass
 
o = Omega("omega")
print(o)

# Explanation:
# o is an instance of the Omega class, which is a subclass of Beta which 
# itself is a subclass of both Gamma and Delta.
# The result of print(o) will depend on whether or not object o has a custom __str__() 
# method defined. As a reminder __str__() is a built-in method of an object and 
# will return a string with the object's class name and some hexadecimal numbers (
# ex : <__main__.Omega object at 0x7f18090ef890>). If a custom __str__() is defined 
# for a class, then printing an object from that class will return whatever string i
# s defined in the custom method  __str__().
# As the Omega class is a subclass of Beta , Omega inherits the methods and properties 
# defined in Beta (unless they have been overridden in Omega). In particular Omega i
# nherits the __str__() method defined in Beta. This method returns super().__str__().  super() 
# is a reference to the direct superclass of Beta - Beta has two superclasses : Gamma and Delta. 
# But Gamma is defined first (as in class Beta(Gamma, Delta):). So super().__str__()  is equivalent to Gamma.__str__(self)
# which returns "I am " + self.name + " from Gamma".
# So, print(o)  will print : I am omega from Gamma