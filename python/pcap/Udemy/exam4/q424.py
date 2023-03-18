#!/usr/bin/python3
# What is the expected output of the following code ?

class B:
    a=0
    def __init__(self, x=0):
        self.b = x
        B.a +=1
 
class A(B):
    c=0
 
a = B()
# x = 0
# a = 1
b = B(2)
# x = 2
# a = 1 + 1 (2)
c = B(3)
# x = 3
# a = 2 + 1 (3)
 
print(A.a)

# Topic : inheritance, class variable

# Explanation:

# Variable a defined in class B is a class variable. B's constructor increments B.a by 1. So, after 
# 3 objects of class B are created (a, b, c), B.a has a value of 3. Class A being a subclass of B, it inherits its class variable a.

# So, A.a returns 3.
# it doesn't need mangling as it's not a private variable