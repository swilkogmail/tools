#!/usr/bin/python3
# What is the expected output of the code snippet below ?
class Alpha:
    A=0
    def __init__(self, x): # 2
        self.k = x  # So, print(o.k)  will print  2.
 
class Kappa(Alpha):
    K=1
    def __init__(self, x):  # Omega does not have any constructor of its own so it is inheriting the constructor
                            # from Kappa since Kappa is the first super class in the Omega inheritance path, 
        self.k = x + 1      # k = (3+1) The constructor from Kappa initially sets property k with  a value of x+1
        # note that x is passed to the super() not k! therefore 
        super().__init__(x-1) # (3-1) but also calls the constructor from Alpha (super() returns a reference to the nearest superclass of the class) with parameter x-1 .
 
class Gamma:
    G = 2
    def __init__(self, x):
        self.k = x + 2
 
class Omega(Kappa,Gamma): # The Omega class is a subclass of both Kappa and Gamma.
    O = 3
 
o=Omega(3)
print(o.k)
