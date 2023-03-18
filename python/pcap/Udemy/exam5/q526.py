#!/usr/bin/python3
# What is the expected output of the following code?

x = {(1, 2): 1, (2, 3): 2}
print(x[1, 2])

# Explanation:

# x is a dictionary and each of its key is defined as a tuple.

# As a reminder, a tuple can be defined using parenthesis as in :

# my_tuple = (1, 2, 4, 8)

# but also without parenthesis, as in :

# my_tuple = 1, 2, 4, 8.

# x[1,2] is simply equivalent to x[(1,2)] which returns the corresponding value from the key (1,2) of the dictionary x, which is 1.

# Try it yourself:

x = {(1, 2): 1, (2, 3): 2}
print(x[1, 2])        # 1
print(x[(1, 2)])      # 1