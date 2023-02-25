#!/usr/bin/python3
# What is the expected output of the following code ?
x = 'abcdef'
print(x[::-3]*2)

# Using indexing syntax can be used to slice a string :
# string[start:end:step]
# start: Starting index where the slicing of object starts.
# stop: Ending index where the slicing of object stops.
# step: It is an optional argument that determines the increment between each index for slicing.
# string[::-3] will return every 3 characters starting at the end of the string (because the step is a negative number ) until the start of the string.
# So, if x = 'abcdef', x[::-3] will return fc .
# The * operator is valid between a string and an integer.
# 2*'fc' will return fcfc