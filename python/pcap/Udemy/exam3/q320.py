#!/usr/bin/python3
# Explanation:
# A class constructor (method __init__() in a class) is invoked automatically when an object of the class is instantiated.
# A few things to remember regarding class constructors:
# - a class constructor needs at least one parameter (self)
# - a class constructor cannot return a value
# - a class constructor cannot be invoked directly from inside its class
# - a class constructor can be invoked from inside a subclass
# Based on the above, the only correct statement from the suggested answers is :
# A class constructor can be invoked directly from any of the subclasses.
# Try it yourself:
# small code snippet to show a few of the above statements
class Class1:
    def __init__(self,val):    
        self.x = val
        #return self.x   # if you uncomment this will raise an exception when creating an object
 
class Class2(Class1):
    def __init__(self,val):
        Class1.__init__(self,val)  # calling Class1 constructor within a subclass
 
a = Class1(2)
b = Class2(3)
print(b.x)        # 3