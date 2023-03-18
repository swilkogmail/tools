#!/usr/bin/python3
# What is the expected output of the following code snippet ?

class Alpha:
    x = 0
    def set(self,x):
        return x+1
 
class Beta:
    x = 1
 
class Kappa(Beta, Alpha): # Class Kappa is a subclass of both Beta and Alpha and, as such, inherits methods and properties from both.
    def set(self,x):
        return x+2
 
k = Kappa() 
print(k.set(k.x))

# Explanation:

# As per MRO rules, to find any object/class property, Python looks for it as per the following order :

# 1/ inside the object itself;

# 2/ inside all classes involved in the object's inheritance line from bottom to top;

# 3/ if there is more than one class on a particular inheritance path, Python scans them from left to right;

# 4/ if both of the above fail, the AttributeError exception is raised.

# Object k is an instance of Kappa - it inherits class variable x  from Beta since Beta is the first 
# class in the Kappa definition (from left to right as per above rules). So, after k has been created, k.x has a value of 1.

# Now, method set() is defined in both Kappa and Alpha.  But the method defined in Kappa overrides the one from Alpha. So, k.set(k.x) returns kx.+2, which is 3.