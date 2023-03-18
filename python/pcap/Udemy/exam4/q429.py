#!/usr/bin/python3
# You are being asked to create a Python class :
# - that has one class variable initially set to 0
# - that has one constructor setting a private instance variable to a parameter passed in the constructor, and increment the class variable by one
# - that has a method that will print ABC when an object of its class is printed

class A:
    a=0
    def __init__(self, val):
        self.__b = val
        A.a += 1
    def __str__():
        return "ABC"

class A:
    a=0
    def __init__(self, val):
        self.b = val
        A.a += 1
    def __str__(self):
        return "ABC"

class A:
    a=0
    def __init__(self, val):
        self.__b = val
        A.a += 1
    def __str__(self):
        return "ABC"
(Correct)

class A:
    a=0
    def __init__(self, val):
        self.__b = val
        a += 1
    def __str__(self):
        return "ABC"


Explanation:
Please refer to the Try it Yourself section.
Try it yourself:
class A:
    a=0
    def __init__(self, val):
        self.__b = val
        A.a += 1
    def __str__(self):
        return "ABC"
 
# Class A has class variable a, initially set to 0:
print(hasattr(A,'a'))   # True
print(A.a)      # 0 
 
a1=A(2)
 
# class variable a has been incremented by 1:
print(A.a)      # 1
 
# object a1 has private instance variable __b:
print(hasattr(a1,'_A__b'))   # True
 
# when object a1 is printed, ABC is shown on the screen:
print(a1)   # ABC