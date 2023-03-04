#!/usr/bin/python3
# What is the expected output of the following code?
class Alpha:
    def __init__(self, val):
        self.x = val
        # - then in the first superclass of Beta, which is Alpha : there is a constructor defined here and Python will use it when creating object k.
        # So, when object k is created, k.x has a value of 1.
 
class Beta(Alpha):
    # - then in the Beta class (which is the first class listed from left to right in the Kappa definition)  - there is none
    pass
 
class Gamma:
    def __init__(self, val):
        self.x = val+1
 
class Omega(Gamma):
    def __init__(self, val):
        super().__init__(val+1)
 
class Kappa(Beta,Omega):
    # The Kappa class does not have a constructor of its own - but it is inheriting a 
    # constructor from one of its superclass - the problem is : which one ?  The MRO rules answer this question.
    # As per MRO rule, Python will try to find a constructor :
    # - first in the Kappa class itself (there is none)
    pass
 
k=Kappa(1)
print(k.x)

# Explanation:
# This question is about multiple inheritance and the MRO rules.
# The mro(Class) function returns a list of types the class Class is derived from, in the 

# The mro(Class) function returns a list of types the class Class is derived from, in the order they are searched for methods. 
# Refer to the example below to confirm the order in which Python will search for a constructor method for class Kappa.
print(Kappa.mro())