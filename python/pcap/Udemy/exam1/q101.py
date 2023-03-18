#!/usr/bin/python3
# What is the expected output of the following code if the user enters 2 for a, 3 for b and 2 for c ?

a = input("Enter a:")
b = input("Enter b:")
c = input("Enter c:")
print(a**b**c)

# Explanation:

# input() returns a string. So variables a, b and c are strings.

# The ** operator (exponentiation) does not support string as operand.

# The above code will result in a TypeError exception.

# To fix the code, the result of the input() would need to be converted to an integer or a float - for example:

# a = int(input("Enter a:"))