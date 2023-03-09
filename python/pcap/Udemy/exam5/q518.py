#!/usr/bin/python3
# Explanation:

# -> "The result of the // operator is always an integer" : this is false - if one operand is a float, the result will be a float. For example

# -> "The exponentiation operator uses the left-sided binding" : this is false - The exponentiation operator uses the right-sided binding.

# -> "A unary operator is an operator with only one operand" : this is true ! Example of unary operator : -5  , or + 14

# -> "The right argument of the % operator can be zero" : this is false. This will raise a ZeroDivisionError exception.

# "The result of the // operator is always an integer" : this is FALSE.
x= 5//2.0
print(x)            # 2.0
print(type(x))      # <class 'float'>
 
# "The exponentiation operator uses the left-sided binding" : this is FALSE.
print(2**2**3)      # 256
print(2**8)         # 256
 
# "The right argument of the % operator can be zero" : this is FALSE.
print(2 % 0)        # ZeroDivisionError