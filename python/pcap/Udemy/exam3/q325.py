#!/usr/bin/python3
# Consider the code below :
class Gamma:
    def __init__(self, val):
        self.g = val
 
class Kappa(Gamma):
    K = 0
    pass
 
k1 = Kappa(1)
k2 = Kappa(2)
k3 = k1
k3.g += 1

# Explanation:
# Let's review each suggested answers:

# --> k1 is not k3  : the is and is not operators check whether two variables refer/do not 
# refer to the same object. Here k1 and k3 do refer to the same object 
# (because of assignment   k3 = k1 ). So  : k1 is k3 is True and k1 is not k3 is False.

# --> hasattr(Gamma,'K') : the hasattr() function returns True is an object 
# or a class has a specified property. Here class Gamma does not have the property K  (Kappa does).

# --> k1.g == 1 : as discussed above, k1 and k3 are two variables that refer 
# to the same object. So, any change made to k3.g will also apply to k1.g. And because of line  k3.g += 1, we have k1.g returns 2.

# -->  isinstance(k2, Gamma)  : the isinstance() function checks if an object 
# comes from a specified class. Here k2 is indeed an instance of the Gamma class, via inheritance from Kappa.

print(k1 is not k3)          # False
print(hasattr(Gamma,'K'))    # False
print(k1.g == 1)             # False
print(k1.g)                  # 2
print(isinstance(k2, Gamma)) # True