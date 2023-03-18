#!/usr/bin/python3
# What is the output of the following snippet if the user enters two lines containing 5 and 1 respectively ?

x = input()
y = input()
print (x + y)

# Explanation:

# The input() function always return a string. So x and y are strings.

# The +  operator on two strings is allowed and concatenates the strings.

# Try it yourself:

# x = input("enter x:")        # enter 5
# print(type(x))               # <class 'str'>
 
# y = input("enter y:")        # enter 1
# print(type(y))               # <class 'str'>
 
# print (x + y)                # 51