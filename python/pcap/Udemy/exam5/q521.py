#!/usr/bin/python3
# Explanation:

# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.

# The syntax is : range(start, stop, step) where :

# - start (optional) : An integer number specifying at which position to start. Default is 0

# - stop (required): An integer number specifying at which position to stop (not included).

# - step (optional) : An integer number specifying the incrementation. Default is 1

x = range(5)
 
for n in x:
  print(n, end=', ')    #  0, 1, 2, 3, 4, 
print('\n--------')
 
x = range(2,2,1)
 
for n in x:
  print(n, end=', ')    # empty sequence
print('\n--------')
 
x = range(5,2,-2)
 
for n in x:
  print(n, end=', ')    # 5,3,
print('\n--------')
 
x = range(-2,6,2)
 
for n in x:
  print(n, end=', ')    # -2, 0, 2, 4,
print('\n--------')