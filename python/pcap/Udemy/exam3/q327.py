#!/usr/bin/python3
# What will be the output of the following code ?

class Alpha:
    def __init__(self, a=2):
        self.a = a
    def set(self, a):
        self.a = a
        return a
 
a = Alpha() # object a is an instance of Alpha and is created with property a=2 by default - in others words a.a = 2 initially.
print(a.set(a.a  + 2)) # So a.set(a.a  + 2)  is the same as a.set(4) which returns 4.

# Explanation
# Knowledge Area : Object-Oriented Programming

# Topic : object, property, method

# Explanation:

# Alpha is a class with a constructor and a method (set()).



# Try it yourself:

# class Alpha:
#     def __init__(self, a=2):
#         self.a = a
#     def set(self, a):
#         self.a = a
#         return a
 
# a = Alpha()
# print(a.set(a.a  + 2))   # 4
# Question ID: Q327