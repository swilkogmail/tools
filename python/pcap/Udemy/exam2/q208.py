#!/usr/bin/python3
# What is the expected output of the following code snippet ?

class R:
    def __init__(self):
        self.T = 1 
    def r(self): # method r is defined in both classes that forms inheritence from T so left to right  R wins
        print('r')
 
class S:
    def __init__(self):
        self.T = 2
    def r(self):
        print('s')
 
class T(R, S):
    def t(self):
        self.r()
 
t = T() # Object t is an instance from class T which is a subclass from R and S 
        # (in that order as defined in the class definition for T : class T(R,S)).
t.t()

Explanation:

# Object t inherits methods and properties from both classes R and S. 
# However, method r() is defined in both classes  R and S. In this case of multiple 
# inheritance, the Python's MRO (Method Resolution Order) rule will use 
# the order in which class T inherits from R and S and will take the definition 
# of the method/property found in the first class, reading from left to right in 
# the class definition. In the above case, method r() from class R will be used 
# (because in class T(R,S)  R is the first class with the r() method when reading from left to right).