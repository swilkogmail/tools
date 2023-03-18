#!/usr/bin/python3
# You want to find the square root of 576. You created the following code:

# Line 1
sqrt=(576,)
result = s(sqrt[0])
print(result)

# Explanation:
# Function sqrt() from the math module is needed to find the square root of 576.
# The math module is not available by default, it needs to be imported.
# from math import sqrt  would import the sqrt() function from the math module- 
# however the name sqrt is already used in the code to defined variable : sqrt=(576,) which is a tuple (yes, this is done to confuse you !).
# And it looks like the code is using s() as an alias for function sqrt() to avoid the duplicate name.
# So, correct line addition would be :
# from math import sqrt as s  which would import function sqrt() from math module and use s() as an alias for sqrt()