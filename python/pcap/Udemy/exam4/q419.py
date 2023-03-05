#!/usr/bin/python3
# What is the expected output of the following code?
# print(max("I love Python!"))

# P

# 121

# y
# (Correct)

# !
# (Incorrect)

# Explanation:
# The max() function returns the maximum element of the sequence passed as an argument. 
# When the argument is a string, the Unicode/ASCII code of each character is used to find the maximum.
# In the ASCII table, symbols like !, #, $, ? have a smaller ASCII code than 
# uppercase letters A..Z and themselves have a smaller ASCII code than lowercase letters a..z.
# So, in the string "I love Python!", the lowercase letter y would be the one with the largest ASCII code - consequently:
# print(max("I love Python!"))  will return y.
