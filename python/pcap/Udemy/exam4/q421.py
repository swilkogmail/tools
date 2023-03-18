#!/usr/bin/python3
# Question 13: Correct
# What is the expected output of the following code ?
class X:
    def __init__(self,val):
        self.__x = val + 1
 
class Y(X):
    def __init__(self,val):
        X.__init__(self,val+1)
 
y= Y(1)
print(y.__x) # should be print(y._X__x)

# Explanation:
# Class Y is a subclass of X , so instances of Y inherit properties from class X.
# Property x is defined as a private instance variable (double underscore notation).
# Referring to this private instance variable outside of the class requires the use of name mangling : _X__x.
# So, print(y.__x) will raise an AttributeError exception.
# Correct code should have been : print(y._X__x)
# Try it yourself:
# class X:
#     def __init__(self,val):
#         self.__x = val + 1
 
# class Y(X):
#     def __init__(self,val):
#         X.__init__(self,val+1)
 
# y= Y(1)
# #print(y.__x)    # AttributeError exception
# print(y._X__x)   # 3