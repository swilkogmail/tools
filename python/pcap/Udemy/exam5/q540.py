#!/usr/bin/python3
# Which statement below is true ? (check all that apply)

# Explanation:

# Please refer to the section below for details on each suggested answers.

# Try it yourself:

# function tuple() creates a tuple :
x = tuple(('12', 2, "ABC"))
print(type(x))     # <class 'tuple'>
 
# A tuple with one element can be created with or without parenthesis
X = 1,    # or : X = (1,)
print(type(x))     # <class 'tuple'>
 
# A tuple is immutable, so attempting to insert an element will raise an exception:
X = (1, ('e', 'f'), (6,5), 'H')
X.insert(0, '2')    # Exception
print(len(X))
 
# method count() will return the number of times a specific element exists in a tuple:
X = (5, 3, 5, 1, 8)
print(X.count(5))    # 2