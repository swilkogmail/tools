#!/usr/bin/python3
# What will be the result of executing the following code?

class Robot:
    def t(self): # method t() is defined in both Robot and Droid classes.
        print('Robot')
 
class Droid:
    def t(self): # method t() is defined in both Robot and Droid classes.
        print('Droid')
 
class ProtoDroid(Droid, Robot): # ProtoDroid is a subclass of both  Robot and Droid.
    def f(self):
        self.t() # use the t() method from the Droid class (since Droid is defined before Robot - definition of ProtoDroid class (class ProtoDroid(Droid, Robot):)
 
R2D2 = ProtoDroid()
R2D2.f()

# Explanation:

# MRO : Method Resolution Order. These are the rules that drive how the Python programming language scans through the 
# upper part of a class's hierarchy to find the method it needs.

# In particular : if there is more than one class on a particular inheritance path, Python scans them from left to right.

# In the above question, method t() is defined in both Robot and Droid classes.

# ProtoDroid is a subclass of both  Robot and Droid. The call to t() within the f() method of class ProtoDroid 
# will use the MRO rules and use the t() method from the Droid class (since Droid is defined before Robot in the 
# definition of ProtoDroid class (class ProtoDroid(Droid, Robot):) when read from left to right).