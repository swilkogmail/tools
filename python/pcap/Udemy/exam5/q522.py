#!/usr/bin/python3
# Assuming the following variables have been defined as below :

x = 1
y = 0
Which of the following statements is true ?

# Explanation:

# This is all about bitwise operators :

# & does a bitwise and,

# | does a bitwise or,

# ^ does a bitwise xor,

# << does a bitwise left shift.

x=1
y=0
 
z = x & y
print(z)    # 0
 
z = x | y
print(z)    # 1
 
z = x ^ y
print(z)    # 1
 
z = y << x
print(z)    # 0